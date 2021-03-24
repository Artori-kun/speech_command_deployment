# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Demo.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
import os
# import record_command

os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = ".\\platform\\"

CUR_CMD = -1


class Worker(QtCore.QObject):
    finished = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        QtCore.QObject.__init__(self, parent=parent)
        self.continue_run = True
        self.rec = record_command.Recorder()

    def do_work(self):
        while self.continue_run:
            cmd = self.rec.record().__next__()



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1200, 395)
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.Vietnamese, QtCore.QLocale.Vietnam))
        self.groupBox_PNgu = QtWidgets.QGroupBox(Dialog)
        self.groupBox_PNgu.setGeometry(QtCore.QRect(0, 0, 321, 331))
        self.groupBox_PNgu.setObjectName("groupBox_PNgu")
        self.Btn_Bat_PN = QtWidgets.QPushButton(self.groupBox_PNgu)
        self.Btn_Bat_PN.setGeometry(QtCore.QRect(50, 300, 89, 25))
        self.Btn_Bat_PN.setObjectName("Btn_Bat_PN")
        self.btn_Tat_PN = QtWidgets.QPushButton(self.groupBox_PNgu)
        self.btn_Tat_PN.setGeometry(QtCore.QRect(190, 300, 89, 25))
        self.btn_Tat_PN.setObjectName("btn_Tat_PN")
        self.Remcua = QtWidgets.QLabel(self.groupBox_PNgu)
        self.Remcua.setGeometry(QtCore.QRect(50, 60, 181, 231))
        self.Remcua.setStyleSheet("image: url(./anh/remcua.jpg);")
        self.Remcua.setText("")
        self.Remcua.setObjectName("Remcua")
        self.groupBox_PKhach = QtWidgets.QGroupBox(Dialog)
        self.groupBox_PKhach.setGeometry(QtCore.QRect(340, 0, 331, 331))
        self.groupBox_PKhach.setObjectName("groupBox_PKhach")
        self.btn_Bat_PK = QtWidgets.QPushButton(self.groupBox_PKhach)
        self.btn_Bat_PK.setGeometry(QtCore.QRect(40, 300, 89, 25))
        self.btn_Bat_PK.setObjectName("btn_Bat_PK")
        self.btn_Tat_PK = QtWidgets.QPushButton(self.groupBox_PKhach)
        self.btn_Tat_PK.setGeometry(QtCore.QRect(190, 300, 89, 25))
        self.btn_Tat_PK.setObjectName("btn_Tat_PK")
        self.Den_PK = QtWidgets.QLabel(self.groupBox_PKhach)
        self.Den_PK.setGeometry(QtCore.QRect(40, 140, 81, 131))
        self.Den_PK.setStyleSheet("image: url(./anh/bongden.jpg);")
        self.Den_PK.setText("")
        self.Den_PK.setObjectName("Den_PN_2")
        self.groupBox_PTam = QtWidgets.QGroupBox(Dialog)
        self.groupBox_PTam.setGeometry(QtCore.QRect(690, 0, 341, 331))
        self.groupBox_PTam.setObjectName("groupBox_PTam")
        self.btn_BatPT = QtWidgets.QPushButton(self.groupBox_PTam)
        self.btn_BatPT.setGeometry(QtCore.QRect(60, 300, 89, 25))
        self.btn_BatPT.setObjectName("btn_BatPT")
        self.btn_Tat_PT = QtWidgets.QPushButton(self.groupBox_PTam)
        self.btn_Tat_PT.setGeometry(QtCore.QRect(190, 300, 89, 25))
        self.btn_Tat_PT.setObjectName("btn_Tat_PT")
        self.Den_PT = QtWidgets.QLabel(self.groupBox_PTam)
        self.Den_PT.setGeometry(QtCore.QRect(40, 140, 181, 131))
        self.Den_PT.setStyleSheet("image: url(./anh/bongden.jpg);")
        self.Den_PT.setText("")
        self.Den_PT.setObjectName("Den_PN")
        self.btn_ghiam = QtWidgets.QPushButton(Dialog)
        self.btn_ghiam.setGeometry(QtCore.QRect(1070, 150, 89, 31))
        self.btn_ghiam.setObjectName("btn_ghiam")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox_PNgu.setTitle(_translate("Dialog", "phòng ngủ"))
        self.Btn_Bat_PN.setText(_translate("Dialog", "bật"))
        self.btn_Tat_PN.setText(_translate("Dialog", "tắt"))
        self.groupBox_PKhach.setTitle(_translate("Dialog", "phòng khách"))
        self.btn_Bat_PK.setText(_translate("Dialog", "bật"))
        self.btn_Tat_PK.setText(_translate("Dialog", "tắt"))
        self.groupBox_PTam.setTitle(_translate("Dialog", "phòng tắm"))
        self.btn_BatPT.setText(_translate("Dialog", "bật"))
        self.btn_Tat_PT.setText(_translate("Dialog", "tắt"))
        self.btn_ghiam.setText(_translate("Dialog", "Ghi âm"))

    # import test_rc

    def batden_phongtam(self, Dialog):
        self.groupBox_PTam.setStyleSheet("background-color: rgb(252, 233, 79);")


    def tatden_phongtam(self, Dialog):
        self.groupBox_PTam.setStyleSheet("background-color: rgb(238, 238, 236);")

    def batden_phongkhach(self, Dialog):
        self.groupBox_PKhach.setStyleSheet("background-color: rgb(252, 233, 79);")


    def tatden_phongkhach(self, Dialog):
        self.groupBox_PKhach.setStyleSheet("background-color: rgb(238, 238, 236);")

    def remcua_dong(self, Dialog):
        self.groupBox_PNgu.setStyleSheet("background-color: rgb(0,0,0);")

    def remcua_mo(self, Dialog):
        self.groupBox_PNgu.setStyleSheet("background-color: rgb(252, 175, 62);")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

