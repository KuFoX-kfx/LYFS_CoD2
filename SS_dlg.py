# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SS_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SS(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(200, 100)
        self.RDBTN_1 = QtWidgets.QRadioButton(Dialog)
        self.RDBTN_1.setEnabled(False)
        self.RDBTN_1.setGeometry(QtCore.QRect(10, 0, 151, 21))
        self.RDBTN_1.setCheckable(True)
        self.RDBTN_1.setObjectName("RDBTN_1")
        self.RDBTN_2 = QtWidgets.QRadioButton(Dialog)
        self.RDBTN_2.setGeometry(QtCore.QRect(10, 20, 151, 21))
        self.RDBTN_2.setObjectName("RDBTN_2")
        self.RDBTN_3 = QtWidgets.QRadioButton(Dialog)
        self.RDBTN_3.setGeometry(QtCore.QRect(10, 40, 151, 21))
        self.RDBTN_3.setObjectName("RDBTN_3")
        self.RDBTN_4 = QtWidgets.QRadioButton(Dialog)
        self.RDBTN_4.setEnabled(False)
        self.RDBTN_4.setGeometry(QtCore.QRect(10, 60, 151, 21))
        self.RDBTN_4.setCheckable(True)
        self.RDBTN_4.setObjectName("RDBTN_4")
        self.PRGBR_1 = QtWidgets.QProgressBar(Dialog)
        self.PRGBR_1.setGeometry(QtCore.QRect(170, 0, 16, 16))
        self.PRGBR_1.setMaximum(1)
        self.PRGBR_1.setProperty("value", 0)
        self.PRGBR_1.setTextVisible(False)
        self.PRGBR_1.setOrientation(QtCore.Qt.Vertical)
        self.PRGBR_1.setObjectName("PRGBR_1")
        self.PRGBR_2 = QtWidgets.QProgressBar(Dialog)
        self.PRGBR_2.setGeometry(QtCore.QRect(170, 20, 16, 16))
        self.PRGBR_2.setMaximum(1)
        self.PRGBR_2.setProperty("value", 0)
        self.PRGBR_2.setTextVisible(False)
        self.PRGBR_2.setOrientation(QtCore.Qt.Vertical)
        self.PRGBR_2.setObjectName("PRGBR_2")
        self.PRGBR_3 = QtWidgets.QProgressBar(Dialog)
        self.PRGBR_3.setGeometry(QtCore.QRect(170, 40, 16, 16))
        self.PRGBR_3.setMaximum(1)
        self.PRGBR_3.setProperty("value", 0)
        self.PRGBR_3.setTextVisible(False)
        self.PRGBR_3.setOrientation(QtCore.Qt.Vertical)
        self.PRGBR_3.setObjectName("PRGBR_3")
        self.PRGBR_4 = QtWidgets.QProgressBar(Dialog)
        self.PRGBR_4.setGeometry(QtCore.QRect(170, 60, 16, 16))
        self.PRGBR_4.setMaximum(1)
        self.PRGBR_4.setProperty("value", 0)
        self.PRGBR_4.setTextVisible(False)
        self.PRGBR_4.setOrientation(QtCore.Qt.Vertical)
        self.PRGBR_4.setObjectName("PRGBR_4")
        self.PSHBTN_CHKS = QtWidgets.QPushButton(Dialog)
        self.PSHBTN_CHKS.setGeometry(QtCore.QRect(0, 80, 81, 20))
        self.PSHBTN_CHKS.setObjectName("PSHBTN_CHKS")
        self.PSHBTN_CHKI = QtWidgets.QPushButton(Dialog)
        self.PSHBTN_CHKI.setGeometry(QtCore.QRect(80, 80, 81, 20))
        self.PSHBTN_CHKI.setObjectName("PSHBTN_CHKI")
        self.PRGBR_IntCHK = QtWidgets.QProgressBar(Dialog)
        self.PRGBR_IntCHK.setGeometry(QtCore.QRect(170, 80, 16, 16))
        self.PRGBR_IntCHK.setMaximum(4)
        self.PRGBR_IntCHK.setProperty("value", 0)
        self.PRGBR_IntCHK.setTextVisible(False)
        self.PRGBR_IntCHK.setOrientation(QtCore.Qt.Vertical)
        self.PRGBR_IntCHK.setObjectName("PRGBR_IntCHK")
        self.PRGBR_IntCHK.raise_()
        self.RDBTN_1.raise_()
        self.RDBTN_2.raise_()
        self.RDBTN_3.raise_()
        self.RDBTN_4.raise_()
        self.PRGBR_1.raise_()
        self.PRGBR_2.raise_()
        self.PRGBR_3.raise_()
        self.PRGBR_4.raise_()
        self.PSHBTN_CHKS.raise_()
        self.PSHBTN_CHKI.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Select site for check"))
        self.RDBTN_1.setText(_translate("Dialog", "Auto(slow) (in progress)"))
        self.RDBTN_2.setText(_translate("Dialog", "game-state.com"))
        self.RDBTN_3.setText(_translate("Dialog", "gametracker.com"))
        self.RDBTN_4.setText(_translate("Dialog", "Custom (What???)"))
        self.PSHBTN_CHKS.setText(_translate("Dialog", "Check sites"))
        self.PSHBTN_CHKI.setText(_translate("Dialog", "Check Internet"))
