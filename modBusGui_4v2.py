# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modBusGui_4.ui'
#
# Created: Sun Oct 23 17:16:40 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!
#test
from PyQt4 import QtCore, QtGui

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(280, 500)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 240, 260, 200))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 40, 261, 192))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.grid_Params = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.grid_Params.setMargin(0)
        self.grid_Params.setObjectName(_fromUtf8("grid_Params"))
        self.label_port = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_port.setObjectName(_fromUtf8("label_port"))
        self.grid_Params.addWidget(self.label_port, 3, 0, 1, 1)
        self.lineEdit_IP = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_IP.setObjectName(_fromUtf8("lineEdit_IP"))
        self.grid_Params.addWidget(self.lineEdit_IP, 2, 1, 1, 1)
        self.label_IP = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_IP.setObjectName(_fromUtf8("label_IP"))
        self.grid_Params.addWidget(self.label_IP, 2, 0, 1, 1)
        self.label_regAddr = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_regAddr.setObjectName(_fromUtf8("label_regAddr"))
        self.grid_Params.addWidget(self.label_regAddr, 5, 0, 1, 1)
        self.spinBox_numOfReg = QtGui.QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_numOfReg.setObjectName(_fromUtf8("spinBox_numOfReg"))
        self.grid_Params.addWidget(self.spinBox_numOfReg, 6, 1, 1, 1)
        self.lineEdit_port = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_port.setObjectName(_fromUtf8("lineEdit_port"))
        self.grid_Params.addWidget(self.lineEdit_port, 3, 1, 1, 1)
        self.label_ReqParams = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_ReqParams.setObjectName(_fromUtf8("label_ReqParams"))
        self.grid_Params.addWidget(self.label_ReqParams, 4, 0, 1, 1)
        self.lineEdit_regAddr = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_regAddr.setObjectName(_fromUtf8("lineEdit_regAddr"))
        self.grid_Params.addWidget(self.lineEdit_regAddr, 5, 1, 1, 1)
        self.label_ConnParams = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_ConnParams.setObjectName(_fromUtf8("label_ConnParams"))
        self.grid_Params.addWidget(self.label_ConnParams, 1, 0, 1, 1)
        self.label_numOfReg = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_numOfReg.setObjectName(_fromUtf8("label_numOfReg"))
        self.grid_Params.addWidget(self.label_numOfReg, 6, 0, 1, 1)
        self.line_separator1 = QtGui.QFrame(self.gridLayoutWidget_2)
        self.line_separator1.setFrameShape(QtGui.QFrame.HLine)
        self.line_separator1.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_separator1.setObjectName(_fromUtf8("line_separator1"))
        self.grid_Params.addWidget(self.line_separator1, 1, 1, 1, 1)
        self.line_separator1_2 = QtGui.QFrame(self.gridLayoutWidget_2)
        self.line_separator1_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_separator1_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_separator1_2.setObjectName(_fromUtf8("line_separator1_2"))
        self.grid_Params.addWidget(self.line_separator1_2, 4, 1, 1, 1)

        self.button_dummy = QtGui.QPushButton(self.centralwidget)
        self.button_request = QtGui.QPushButton(self.centralwidget)
        self.button_request.setGeometry(QtCore.QRect(185, 450, 85, 27))
        self.button_request.setObjectName(_fromUtf8("button_request"))

        self.checkBox_Connected = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_Connected.setGeometry(QtCore.QRect(10, 450, 88, 22))
        self.checkBox_Connected.setObjectName(_fromUtf8("checkBox_Connected"))
        # MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 280, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        # MainWindow.setMenuBar(self.menubar)

        self.action_Anounce = QtGui.QAction(MainWindow)
        self.action_Anounce.setObjectName(_fromUtf8("action_Anounce"))
        self.action_Quit = QtGui.QAction(MainWindow)
        self.action_Quit.setObjectName(_fromUtf8("action_Quit"))

        self.action_About = QtGui.QAction(MainWindow)
        self.action_About.setObjectName(_fromUtf8("action_About"))

        self.menuFile.addAction(self.action_Anounce)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_Quit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.menuHelp.addAction(self.action_About)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Modbus client", None))
        self.label_port.setText(_translate("MainWindow", "Port number:", None))
        self.label_IP.setText(_translate("MainWindow", "IP address:", None))
        self.label_regAddr.setText(_translate("MainWindow", "Holding register address:", None))
        self.label_ReqParams.setText(_translate("MainWindow", "Request parameters", None))
        self.label_ConnParams.setText(_translate("MainWindow", "Connection parameters", None))
        self.label_numOfReg.setText(_translate("MainWindow", "No. of registers:", None))
        self.button_request.setText(_translate("MainWindow", "Request", None))
        self.checkBox_Connected.setText(_translate("MainWindow", "Connected", None))
        self.menuFile.setTitle(_translate("MainWindow", "&File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "&Help", None))
        self.action_Anounce.setText(_translate("MainWindow", "Display current setup", None))
        self.action_Quit.setText(_translate("MainWindow", "&Quit", None))
        self.action_About.setText(_translate("MainWindow", "About", None))
