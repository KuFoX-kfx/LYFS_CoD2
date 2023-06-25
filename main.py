#python 3.8.8
#pyuic5 gui.ui -o gui.pyui_as

#import my api
from DB_api import DB_api
from WEB_api import WEB_api
#import files with gui
from gui import Ui_MainWindow
from AS_dlg import Ui_Dialog
from SS_dlg import Ui_SS
db = DB_api('DB.db')
web = WEB_api()
#import lib
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, QObject, pyqtSignal
import sys
import os
from sqlite3 import Error
import subprocess
import threading
import time
import pythonping




#Init App
app = QtWidgets.QApplication(sys.argv)
STRT = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(STRT)
STRT.show()

AS_dlg = QtWidgets.QDialog()
ui_as = Ui_Dialog()
ui_as.setupUi(AS_dlg)

CS_dlg = QtWidgets.QDialog()
ui_ss = Ui_SS()
ui_ss.setupUi(CS_dlg)

#MessageBox init
msgBox = QtWidgets.QMessageBox()
msgBox.setText("Are You Sure?")
msgBox.setWindowTitle("STRT_Confirm")
msgBox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
msgBox.setDefaultButton(QtWidgets.QMessageBox.No)
msgBox.setEscapeButton(QtWidgets.QMessageBox.No)


#Functions


def MS_Add():
    try:
        ui_as.LE_IP.clear()
        ui_as.LE_name.clear()
        AS_dlg.exec()
    except Exception as ex:
        QtWidgets.QMessageBox.critical(msgBox, "STRT_Error", "Error: " + str(ex), QtWidgets.QMessageBox.Ok)
        
def AddServer():
    try:
        db.DB_AddServer(ui_as.LE_IP.displayText(), ui_as.LE_name.displayText())
        RFRSHserver()
    except Exception as ex:
        QtWidgets.QMessageBox.critical(msgBox, "STRT_Error", "Error: " + str(ex), QtWidgets.QMessageBox.Ok)
        
def Connect():
    PTG = db.DB_GetPTG()
    IP = db.DB_GetIP(ui.CMBX_server.currentText())
    try:
        os.system(str('"' + PTG[0]) + '"' + " +connect " + str(IP[0]))
    except Exception as ex:
        QtWidgets.QMessageBox.critical(msgBox, "STRT_Error", "Error: " + str(ex), QtWidgets.QMessageBox.Ok)
    
def ui_PTG():
    PTG = QtWidgets.QFileDialog.getOpenFileName(parent=None, caption="Open EXE file", filter="EXE files (*.exe *.lnk)")[0]
    db.DB_PTG(PTG)
    
def MS_SFC():
    ui_ss.PRGBR_IntCHK.setValue(IntCHK_fast())
    CS_dlg.exec()


def RFRSHserver():
    if ui.CMBX_server.count() > 0 : 
        ui.CMBX_server.clear()
    ui.CMBX_server.addItems(list(map(str, db.DB_GetServers())))

    
def RemServer():
    try:
        ret = msgBox.exec_()
        if ret == QtWidgets.QMessageBox.No:
            pass
        elif ret == QtWidgets.QMessageBox.Yes:
            db.DB_DelServer(str(ui.CMBX_server.currentText()))
            RFRSHserver()
    except Exception as ex:
        QtWidgets.QMessageBox.critical(msgBox, "STRT_Error", "Error: " + str(ex), QtWidgets.QMessageBox.Ok)

def Refresh():
    try:
        if ui.CMBX_server.count() > 0 : 
            ui.LBL_E_IP.setText(db.DB_GetIP(ui.CMBX_server.currentText())[0])
            CO = web.GetPlayers(("https://www.game-state.com/" + db.DB_GetIP(ui.CMBX_server.currentText())[0])).split('/')[-2]
            MO = web.GetPlayers(("https://www.game-state.com/" + db.DB_GetIP(ui.CMBX_server.currentText())[0])).split('/')[-1]
            ui.LBL_E_name.setText(web.GetName("https://www.game-state.com/" + db.DB_GetIP(ui.CMBX_server.currentText())[0]))
            ui.LBL_E_map.setText(web.GetMap("https://www.game-state.com/" + db.DB_GetIP(ui.CMBX_server.currentText())[0]))
            ui.LBL_E_GM.setText(web.GetGM("https://www.game-state.com/" + db.DB_GetIP(ui.CMBX_server.currentText())[0]))
            ui.LBL_E_CO.setText(str(CO))
            ui.LBL_E_MO.setText(str(MO))
            ui.PRGBR_online.setMaximum(int(MO))
            ui.PRGBR_online.setValue(int(CO))
            Ping()
            ui.PRGBR_Int.setValue(IntCHK_fast())
    except Exception as ex:
        ui.LBL_E_name.setText("???")
        ui.LBL_E_map.setText("???")
        ui.LBL_E_GM.setText("???")
        QtWidgets.QMessageBox.critical(msgBox, "STRT_Error", "Error: " + str(ex), QtWidgets.QMessageBox.Ok)
        

        
def Ping():
    ui.LBL_E_Ping.setText(str(pythonping.ping(db.DB_GetIP(ui.CMBX_server.currentText())[0][:-6]).rtt_avg_ms))

def IntCHK_fast():    
    if web.IntCHK("8.8.8.8") == 0:
        return 4
    else:
        if web.IntCHK("8.8.4.4") == 0:
            return 4
        else:
            if web.IntCHK("77.88.8.8") == 0:
                return 4
            else:
                if web.IntCHK("77.88.8.1") == 0:
                    return 4
                else:
                    return 0
                
def IntCHK_full():  
    temp = 0 
    if web.IntCHK("8.8.8.8") == 0:
        temp += 1
    if web.IntCHK("8.8.4.4") == 0:
        temp += 1
    if web.IntCHK("77.88.8.8") == 0:
        temp += 1
    if web.IntCHK("77.88.8.1") == 0:
        temp += 1
    return temp

def IntPRGBR():
    ui.PRGBR_Int.setValue(0)
    ui.PRGBR_Int.setValue(IntCHK_full())

def ss_IntPRGBR():
    ui.PRGBR_Int.setValue(0)
    ui_ss.PRGBR_IntCHK.setValue(IntCHK_full())

IntPRGBR()
RFRSHserver()

#connect functions with gui
ui.MS_RS.triggered.connect(RemServer)
ui.MS_AS.triggered.connect(MS_Add)
ui.MS_PTG.triggered.connect(ui_PTG)
ui.MS_SFCO.triggered.connect(MS_SFC)
ui.PSHBTN_Connect.clicked.connect(Connect)
ui.PSHBTN_UPDSRV.clicked.connect(RFRSHserver)
ui.CMBX_server.currentIndexChanged.connect(Refresh)
ui.PSHBTN_update.clicked.connect(Refresh)
ui.PSHBTN_Ping.clicked.connect(Ping)
ui.PSHBTN_Int.clicked.connect(IntPRGBR)
ui_as.buttonBox.accepted.connect(AddServer)
ui_ss.PSHBTN_CHKI.clicked.connect(ss_IntPRGBR)
#ui_ss.RDBTN_2.clicked.connect()



#class Worker1(QThread):
#    def __init__(self, parent = None):
#            super(Worker1,self).__init__(parent)
#
#
#    def run(self, IP):
#        try:
#            if ui.CMBX_server.count() > 0 : 
#                db.DB_GetIP(ui.CMBX_server.currentText())[0]
#                web.GetPlayers(("https://www.game-state.com/" + db.DB_GetIP(ui.CMBX_server.currentText())[0])).split('/')[-2]
#                web.GetPlayers(("https://www.game-state.com/" + db.DB_GetIP(ui.CMBX_server.currentText())[0])).split('/')[-1]
#                web.GetName("https://www.game-state.com/" + db.DB_GetIP(ui.CMBX_server.currentText())[0])
#                web.GetMap("https://www.game-state.com/" + db.DB_GetIP(ui.CMBX_server.currentText())[0])
#                web.GetGM("https://www.game-state.com/" + db.DB_GetIP(ui.CMBX_server.currentText())[0])
#        except Exception as ex:
#            QtWidgets.QMessageBox.critical(msgBox, "STRT_Error", "Error: " + str(ex), QtWidgets.QMessageBox.Ok)      
#GetServerInfo = Worker1()
#ui.PSHBTN_Connect.clicked.connect(lambda:GetServerInfo.start(GetServerInfo.run("111")))


#Exit app
sys.exit(app.exec_())