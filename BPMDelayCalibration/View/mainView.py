# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled1.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import pyqtgraph, qrangeslider

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        self.TabWidget = TabWidget
        self.TabWidget.setObjectName(_fromUtf8("TabWidget"))
        self.TabWidget.resize(699, 602)
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.addToListButton = QtGui.QPushButton(self.tab)
        self.addToListButton.setGeometry(QtCore.QRect(560, 0, 91, 41))
        self.addToListButton.setObjectName(_fromUtf8("addToListButton"))
        self.bpmPVList = QtGui.QPlainTextEdit(self.tab)
        self.bpmPVList.setGeometry(QtCore.QRect(560, 80, 111, 171))
        self.bpmPVList.setObjectName(_fromUtf8("bpmPVList"))
        self.calibrateButton = QtGui.QPushButton(self.tab)
        self.calibrateButton.setGeometry(QtCore.QRect(320, 90, 221, 161))
        self.calibrateButton.setObjectName(_fromUtf8("calibrateButton"))
        #self.graphicsView = pyqtgraph.GraphicsView(self.tab)
        #self.graphicsView.setGeometry(QtCore.QRect(440, 20, 441, 261))
        #self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        #self.glayoutOutput = pyqtgraph.GraphicsLayout(border = (400,400,400))
        #self.graphicsView.setCentralItem(self.glayoutOutput)
        self.comboBox = QtGui.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(320, 10, 231, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.bpmListLabel = QtGui.QLabel(self.tab)
        self.bpmListLabel.setGeometry(QtCore.QRect(560, 50, 111, 16))
        self.bpmListLabel.setObjectName(_fromUtf8("bpmListLabel"))
        #self.graphicsView_2 = pyqtgraph.GraphicsView(self.tab)
        #self.graphicsView_2.setGeometry(QtCore.QRect(440, 290, 441, 261))
        #self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))
        #self.glayoutOutput_2 = pyqtgraph.GraphicsLayout(border = (400,400,400))
        #self.graphicsView_2.setCentralItem(self.glayoutOutput_2)
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(320, 270, 231, 131))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.newDLYVals = QtGui.QLabel(self.groupBox)
        self.newDLYVals.setGeometry(QtCore.QRect(320, 20, 191, 101))
        self.newDLYVals.setText(_fromUtf8(""))
        self.newDLYVals.setObjectName(_fromUtf8("newDLYVals"))
        self.numShots = QtGui.QPlainTextEdit(self.tab)
        self.numShots.setGeometry(QtCore.QRect(400, 50, 61, 31))
        self.numShots.setObjectName(_fromUtf8("numShots"))
        self.lowerDLYBound = QtGui.QPlainTextEdit(self.tab)
        self.lowerDLYBound.setGeometry(QtCore.QRect(430, 450, 30, 30))
        self.lowerDLYBound.setObjectName(_fromUtf8("lowerDLYBound"))
        self.upperDLYBound = QtGui.QPlainTextEdit(self.tab)
        self.upperDLYBound.setGeometry(QtCore.QRect(480, 450, 30, 30))
        self.upperDLYBound.setObjectName(_fromUtf8("upperDLYBound"))
        self.numShotsLabel = QtGui.QLabel(self.tab)
        self.numShotsLabel.setGeometry(QtCore.QRect(340, 60, 46, 13))
        self.numShotsLabel.setObjectName(_fromUtf8("numShotsLabel"))
        self.scanRangeLabel = QtGui.QLabel(self.tab)
        self.scanRangeLabel.setGeometry(QtCore.QRect(320, 450, 90, 30))
        self.scanRangeLabel.setObjectName(_fromUtf8("scanRangeLabel"))
        self.lowerBoundLabel = QtGui.QLabel(self.tab)
        self.lowerBoundLabel.setGeometry(QtCore.QRect(430, 420, 30, 30))
        self.lowerBoundLabel.setObjectName(_fromUtf8("lowerBoundLabel"))
        self.upperBoundLabel = QtGui.QLabel(self.tab)
        self.upperBoundLabel.setGeometry(QtCore.QRect(480, 420, 30, 30))
        self.upperBoundLabel.setObjectName(_fromUtf8("upperBoundLabel"))
        self.titleLabel = QtGui.QLabel(self.tab)
        self.titleLabel.setGeometry(QtCore.QRect(10, 50, 270, 150))
        self.titleLabel.setObjectName(_fromUtf8("titleLabel"))
        self.infoLabel = QtGui.QLabel(self.tab)
        self.infoLabel.setGeometry(QtCore.QRect(10, 250, 270, 100))
        self.infoLabel.setObjectName(_fromUtf8("infoLabel"))
        self.TabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab1 = QtGui.QWidget()
        self.tab1.setObjectName(_fromUtf8("tab1"))
        self.tabList = []
        self.graphicsViews = []
        self.graphicsViews_2 = []
        self.glayoutOutputs = []
        self.glayoutOutputs_2 = []

        self.retranslateUi(self.TabWidget)
        QtCore.QMetaObject.connectSlotsByName(self.TabWidget)

    def retranslateUi(self, TabWidget):
        self.TabWidget.setWindowTitle(_translate("TabWidget", "TabWidget", None))
        self.addToListButton.setText(_translate("TabWidget", "Calibrate BPM", None))
        self.calibrateButton.setText(_translate("TabWidget", "Calibrate Delays", None))
        self.comboBox.setItemText(0, _translate("TabWidget", "BPM01", None))
        self.comboBox.setItemText(1, _translate("TabWidget", "BPM02", None))
        self.comboBox.setItemText(2, _translate("TabWidget", "BPM03", None))
        self.comboBox.setItemText(3, _translate("TabWidget", "BPM04", None))
        self.comboBox.setItemText(4, _translate("TabWidget", "BPM05", None))
        self.comboBox.setItemText(5, _translate("TabWidget", "BPM06", None))
        self.bpmListLabel.setText(_translate("TabWidget", "BPM List", None))
        self.groupBox.setTitle(_translate("TabWidget", "New BPM Delay Values", None))
        self.numShots.setPlainText(_translate("TabWidget", "2", None))
        self.numShotsLabel.setText(_translate("TabWidget", "# Shots", None))
        self.scanRangeLabel.setText(_translate("TabWidget", "DLY1 Scan Range", None))
        self.lowerBoundLabel.setText(_translate("TabWidget", "Lower Bound", None))
        self.upperBoundLabel.setText(_translate("TabWidget", "Upper Bound", None))
        self.lowerDLYBound.setPlainText(_translate("TabWidget", "2", None))
        self.upperDLYBound.setPlainText(_translate("TabWidget", "10", None))
        self.newFont = QtGui.QFont("Comic Sans", 20, QtGui.QFont.Bold)
        self.titleLabel.setFont(self.newFont)
        self.titleLabel.setText(_translate("TabWidget", "VELA/CLARA Beam \nPosition Monitor \nDelay Calibrator", None))
        self.infoText = "Please select the BPMs to calibrate from the list using \nthe drop-down menu and the 'Calibrate BPM' button."
        self.infoText2 = self.infoText+"\nThe number of shots for each delay setting,\n and the range to scan over (from 0 - 511),\n can also be set."
        self.infoText3 = self.infoText2+" Click 'Calibrate delays' when \nready. The tabs generated will show the results."
        self.infoLabel.setText(_translate("TabWidget", self.infoText3, None))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab), _translate("TabWidget", "Settings", None))
        #self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab1), _translate("TabWidget", "Tab 2", None))

    def addPlotTab(self, TabWidget, pvName):
        self.pvName = pvName
        self.TabWidget = TabWidget
        self.TabWidget.setObjectName(_fromUtf8("TabWidget"))
        self.TabWidget.resize(699, 602)
        self.tab1 = QtGui.QWidget()
        self.tab1.setObjectName(_fromUtf8("tab"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab1), _translate("TabWidget", self.pvName, None))
        self.graphicsView = pyqtgraph.GraphicsView(self.tab1)
        self.graphicsView.setGeometry(QtCore.QRect(140, 20, 441, 261))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.glayoutOutput = pyqtgraph.GraphicsLayout(border = (400,400,400))
        self.graphicsView.setCentralItem(self.glayoutOutput)
        self.graphicsView_2 = pyqtgraph.GraphicsView(self.tab1)
        self.graphicsView_2.setGeometry(QtCore.QRect(140, 290, 441, 261))
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))
        self.glayoutOutput_2 = pyqtgraph.GraphicsLayout(border = (400,400,400))
        self.graphicsView_2.setCentralItem(self.glayoutOutput_2)
        self.tabList.append(self.tab1)
        self.glayoutOutputs.append(self.glayoutOutput)
        self.glayoutOutputs_2.append(self.glayoutOutput_2)
        self.TabWidget.addTab(self.tab1, _fromUtf8(self.pvName))
        self.TabWidget.setObjectName(_fromUtf8(self.pvName))
