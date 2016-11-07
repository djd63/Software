import sys,os
os.environ["EPICS_CA_AUTO_ADDR_LIST"] = "NO"
os.environ["EPICS_CA_ADDR_LIST"] = "10.10.0.12"
os.environ["EPICS_CA_MAX_ARRAY_BYTES"] = "10000000"

sys.path.append(str(os.path.dirname(os.path.abspath(__file__)))+'\Model')
sys.path.append(str(os.path.dirname(os.path.abspath(__file__)))+'\Controller')
sys.path.append(str(os.path.dirname(os.path.abspath(__file__)))+'\View')
sys.path.append('D:\\VELA-CLARA_software\\VELA-CLARA-Controllers-New-Structure-With-Magnets\\bin\\Release')

from PyQt4 import QtGui, QtCore
import VELA_CLARA_BPM_Control as vbpmc
import VELA_CLARA_Scope_Control as vcsc
import mainModel
import mainController
import mainView

class App(QtGui.QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.bpm = vbpmc.init()
        self.scope = vcsc.init()
        self.bpmCont = self.bpm.virtual_VELA_INJ_BPM_Controller()
        self.scopeCont = self.scope.virtual_VELA_INJ_Scope_Controller()
        self.view = mainView.Ui_TabWidget()
        self.MainWindow = QtGui.QTabWidget()
        self.view.setupUi(self.MainWindow)
        self.model = mainModel.Model(self.bpmCont, self.scopeCont)
        self.controller = mainController.Controller(self.view, self.model, self.bpmCont, self.scopeCont)
        self.MainWindow.show()

if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())
