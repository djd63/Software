from epics import caget,caput
import scipy.constants as physics
import os,sys
import time
import math as m
import random as r
import numpy as np
from numpy.polynomial import polynomial as P

sys.path.append('\\\\fed.cclrc.ac.uk\\Org\\NLab\ASTeC\\Projects\\VELA\\Software\\VELA_CLARA_PYDs\\bin\\stagetim')
import VELA_CLARA_MagnetControl as mag

'''This Class contain function to use in a momentum procdure independant '''
class Functions():
	def __init__(self):
		self.n = 10 															#number of shots to average over for a given measuremnet
		self.magInit = mag.init()												#initilize magnet controllers
		self.magnets = self.magInit.virtual_VELA_INJ_Magnet_Controller()

		caput('VM-EBT-INJ-MAG-DIP-01:RIRAN', 5)									#This is a fudge: Turning on removing the noise of the magnets being used on the virtual machine
		caput('VM-EBT-INJ-MAG-QUAD-01:RIRAN', 0)
		caput('VM-EBT-INJ-MAG-HCOR-01:RIRAN', 0)
		caput('VM-EBT-INJ-MAG-HCOR-02:RIRAN', 0)
		self.magnets.switchONpsu('DIP01')
		self.magnets.switchONpsu('HCOR01')
		self.magnets.switchONpsu('HCOR02')
		self.magnets.switchONpsu('QUAD01')

		print("Momentum Functions Initialized")

	def stepCurrent(self,magnet,step):
		MAG = self.magnets.getMagObjConstRef(magnet)
		setI = self.magnets.getSI(magnet)+step
		self.magnets.setSI(magnet,setI,MAG.riTolerance,45)						# waits 45 seconds

	def getXBPM(self,bpm):														#Currently fake as I can't access this dat over the virtual machine
		x=[]
		for i in range(self.n):
			x.append(r.gauss(0.5,0.1))# added to fake a step
		return sum(x)/self.n

	def getXScreen(self, screen):												#Currently fake as I can't access this dat over the virtual machine
		x=[]
		for i in range(self.n):
			x.append(r.gauss(0.5,0.1))# added to fake a step
		return sum(x)/self.n
		x=[]
		for i in range(self.n):
			x.append(r.gauss(0.5,0.1))# added to fake a step
		return sum(x)/self.n

	def getSigmaXScreen(self, screen):
		sX=[]
		for i in range(self.n):
			sX.append(r.gauss(0.5,0.1))# added to fake a step
		return sum(sX)/self.n											#Currently fake as I can't access this dat over the virtual machine

	def isBeamOnScreen(self,screen):											#this does nothing at the moment
		return True

	def align(self, hcor, bpm, tol):
		COR = self.magnets.getMagObjConstRef(hcor)								#create a reference to the corrector
		#faux data
		x1=300*self.getXBPM(bpm)												#get the x position on the BPM
		I1=COR.siWithPol														#x1,x2,I1,I2 are point to determine a straight linear relationship (I=mx+c)
		x2=x1
		I2=0

		if (COR.riWithPol>0.0):													#determine intial step
			initialStep = -0.5
		elif (COR.riWithPol<0.0):
			initialStep = 0.5
		else:
			initialStep = 0.5
		self.stepCurrent(hcor, initialStep)										#take inital step
		x2=x1*self.getXBPM(bpm)
		I2=COR.siWithPol
		while(x2>tol):															# Algorithm loops until the current position is < the tolerance 'tol'
			I_o = (I1*x2-I2*x1)/(x2-x1)											# find the zero-crossing of straight line mde from positions at currents I1 and I2
			self.magnets.setSI(hcor,I_o,COR.riTolerance,10)						# set magnet to intercept current
			x1=x2																#Get rid of first set of position and current
			I1=I2
			I2=I_o
			x2=x2*self.getXBPM(bpm)
		print('Aligned beam using ' + hcor + ' and ' + bpm)

	'''Function to bend the Beam'''
	def bendBeam(self, dipole, bpm, screen, predictedI, tol):
		DIP = self.magnets.getMagObjConstRef(dipole)							#create a reference to the dipole

		step = predictedI/100													#1% of predicted current
		setI = 0.9*predictedI
		self.magnets.setSI(dipole,setI,DIP.riTolerance,10)						#set dipole current to 90% of predicted

		while(self.isBeamOnScreen(screen)==False):								#keep iterration of a 1% current step until beam is on screen
			stepCurrent(dipole,step)

		x_old=500																#fake start x position
		x=x*self.getXBPM(bpm)													#All BPM posiotn are fake and based of the previous position
																				#it wont stay this way for the real procedure
		while(x>tol):															#start loop that ramps up dipole current (conitines unitl x<tolerance)
			self.stepCurrent(dipole,step)
			x_old=x																# keep a note of teh last beam position to roughly predict the effect of the next step
			x=self.getXBPM(bpm)*x

			if x<(x_old-x):														#if the step size look like it is will over bend the beam, half it.
				step = step*0.5
		print('Centered beam in Spectrometer line using ' + dipole + ' and ' + bpm)
		return self.magnets.getSI(dipole)										#return the current at which beam has been centered

	''''Function to minimize Beta (one Quad, one Screen)'''
	def minimizeBeta(self,quad,screen,init_step):
		QUAD = self.magnets.getMagObjConstRef(quad)								#setup
		self.magnets.setSI(quad, 4, QUAD.riTolerance, 10)						#set a fake start current
		step  = init_step
		I3_1 = 0																#I3_1 is the first value that is 3 time the size of the inita current
		I3_2 = 0
		sX_initial =self.getSigmaXScreen(screen)
		I_initial = QUAD.siWithPol
		sX_1 = sX_initial
		I_1 = QUAD.siWithPol
		sX_2 = sX_initial
		I_2 = QUAD.siWithPol

		while (sX_2<3*sX_initial):												#step 'left', i.e reduce current
			sX_1 = sX_2
			I_1 = I_2
			self.stepCurrent(quad,-step)
			I_2 = QUAD.siWithPol
			sX_2 = self.getSigmaXScreen(screen)									#At this pot we have gone higher than 3*initial_size. Assume straight line and find prediction for 3*
		I3_1 = (3*sX_initial*(I_2 - I_1) + (sX_2*I_1 - sX_1*I_2))/(sX_2 - sX_1)

		self.stepCurrent(quad,2*(I_initial - I3_1))								#predict where the the other location of the size being 3*the initial_size and go there
		I_1 = QUAD.siWithPol
		sX_1 = self.getSigmaXScreen(screen)
		if (sX_1<3*sX_initial):
			while (sX_2<3*sX_initial):
				sX_1 = sX_2
				I_1 = I_2
				self.stepCurrent(quad,step)
				I_2 = QUAD.siWithPol
				sX_2 = self.getSigmaXScreen(screen)
		else:
			while (sX_2>3*sX_initial):
				sX_1 = sX_2
				I_1 = I_2
				self.stepCurrent(quad,-step)
				I_2 = QUAD.siWithPol
				sX_2 = self.getSigmaXScreen(screen)

		I3_2 = (3*sX_initial*(I_2 - I_1) + (sX_2*I_1 - sX_1*I_2))/(sX_2 - sX_1)

		self.magnets.setSI(quad,0.5*(I3_1 + I3_2),QUAD.riTolerance,30)			#assume minimum is half way in between these places so set magnet current to that
		print('Minimizied Beta with '+quad+' on '+screen)

	'''Fixes beam to a 0.3 times the size of the screen'''
	def fixDispersion(self,quad,screen,step_size):								#assumes beam is on screen
		sX = self.getSigmaXScreen(screen)
		sX_old = sX
		image_width = 1920 #To be used for now...
		MaximumBeamSize = 0.3*image_width
		while (sX<MaximumBeamSize):
			self.stepCurrent(quad,step_size)
			sX_old = sX
			sX = self.getSigmaXScreen(screen)
			if (sX>sX_old):
				step_size = -step_size

	'''Find Dispersion by scanning dipole'''
	def findDispersion(self,dipole,screen,centering_I,points,leveloff_threshold):
		currents = np.zeros(points)
		positions = np.zeros(points)
		DIP = self.magnets.getMagObjConstRef(dipole)
		#position of beam
		sX=0
		step = centering_I/100
		#set dipole current to 90% of centering current
		setI = 0.9*centering_I
		self.pySetSI(dipole,setI,DIP.riTolerance,10)
		I = self.screens.totalIntensity(screen)
		I_old = I/2

		while(I/I_old-1>leveloff_threshold):
			self.stepCurrent(dipole,step)
		current[0] = DIP.siWithPol
		position[0] = self.getXScreen(screen)
		I_diff = 2*(centering_I-current[0])/(point-1)

		for i in range(1,points):
			self.stepCurrent(dipole,I_diff)
			current[i] = DIP.siWithPol
			positions[i] = self.getXScreen(screen)
			if i==(point-1)/2:
				sX = self.getSigmaXScreen(screen)

		c, stats = P.polyfit(currents,positions,1,full=True)
		return c[0],sX

		print('Determinied Dispersion with '+dipole+' and '+screen)



	'''Conversion Calculations'''
	def calcMomSpread(self, dipole, Is):
		DIP = self.magnets.getMagObjConstRef( dipole )
		return (physics.c/(1000000000))*(DIP.slope*I + DIP.intercept)/m.sin(0.25*physics.pi)

	def calcMom(self, dipole, I):
		DIP = self.magnets.getMagObjConstRef( dipole )
		return (physics.c/(1000000000))*(DIP.slope*I + DIP.intercept)/m.sin(0.25*physics.pi)

	def mom2I(self, dipole, mom):
		#log.info('Converting Momentim to Current for '+ dipole)
		DIP = self.magnets.getMagObjConstRef( dipole )
		print(DIP.slope)
		return(1000000000/physics.c)*((mom*m.sin(0.25*physics.pi) - DIP.intercept))/DIP.slope
