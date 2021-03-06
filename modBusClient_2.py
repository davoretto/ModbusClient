#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
PyQt4 Tutorials template
https://www.youtube.com/channel/UCpjNEyIUW8E8ZQ0JbYA8isw
author: Davor Afric
last edited: October 2016
"""

import sys, modBusGui_6
from PyQt4 import QtCore, QtGui
from pymodbus.client.sync import ModbusTcpClient


class Window(QtGui.QMainWindow, modBusGui_6.Ui_MainWindow):
    """ GUI class
    """
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.client = ModbusClient()
        self.setupUi(self)
        self.initUi()


    def initUi(self):
        """ Initialize the GUI
        """

        """ Push buttons
        """
        # FIXME: requestBtn gets called on returnPressed event in any lineEdit object
        # Fixed on 2016-10-23: Creating an instance of a dummy QtGui.QpushButton object before the button_request
        #     creation in the modBusGui_4v2.py seems to fix the problem with unexpected signals from button_request.
        self.button_request.pressed.connect(self.readHoldingRegisters)
        # FIXME: maybe create an object other than Dialog ?!

        """Line edits
        """
        self.lineEdit_IP.returnPressed.connect(self.setIp)
        self.lineEdit_port.returnPressed.connect(self.setPort)
        self.lineEdit_regAddr.returnPressed.connect(self.setRegAddr)

        """ Spin boxes
        """
        self.spinBox_numOfReg.valueChanged.connect(self.setAmountOfRegs)

        """ Radio buttons
        """
        self.comboBox_ReqMethod.currentIndexChanged.connect(self.getReqMethod)

        """ Menu functionality
        """
        self.action_Quit.activated.connect(QtGui.QApplication.exit)
        self.action_Anounce.activated.connect(self.anounce)
        self.action_About.activated.connect(self.about)

        """ Status Bar
        """
        self.statusLabel = QtGui.QLabel()
        self.progressBar = QtGui.QProgressBar()
        self.myStatusBar = QtGui.QStatusBar()
        self.myStatusBar.addWidget(self.statusLabel, 1)
        self.myStatusBar.addWidget(self.progressBar, 2)
        self.setStatusBar(self.myStatusBar)
        self.showProgress(100)


        """ Show
        """
        self.updateInfo()
        self.show()


    def showProgress(self, progress):
        """ Method to show progress
        """
        self.progressBar.setValue(progress)
        if progress == 100:
            self.statusLabel.setText('Ready')
            return

    def createStatusBar(self):  #TODO: remove
        """ Method to create Status Bar
        """
        self.myStatusBar = QtGui.QStatusBar()
        self.myStatusBar.addWidget(self.statusLabel, 1)
        self.myStatusBar.addWidget(self.progressBar, 2)
        # self.myStatusBar.showMessage('Ready', 2000)
        self.setStatusBar(self.myStatusBar)

    def getReqMethod(self): # TODO: fill up
        """ Action slot
        """
        if self.comboBox_ReqMethod.currentIndex() == 0:
            print(self.comboBox_ReqMethod.currentIndex())
        elif self.comboBox_ReqMethod.currentIndex() == 1:
            print(self.comboBox_ReqMethod.currentIndex())

    def anounce(self):
        """ Action slot
        """
        self.textBrowser.clear()
        self.textBrowser.append("IP Address:  " + self.client.getServerIpAddr())
        self.textBrowser.append("Port:  " + self.client.getPort())
        self.textBrowser.append("Starting Register:  " + self.client.getRegisterStartAddr())
        self.textBrowser.append("Amount of Registers:  " + str(self.client.getAmountReg()))
        self.textBrowser.append("-----------")

    def about(self):
        """ Action slot
        """
        self.textBrowser.clear()
        self.textBrowser.append("Author: Davor Afric")
        self.textBrowser.append("Version: 0.6")
        self.textBrowser.append("Created: November 2016")
        self.textBrowser.append("-----------")

    def setIp(self):
        """ Action slot
        """
        self.client.setServerIpAddr(unicode(self.lineEdit_IP.text()))
        self.updateInfo()

    def setPort(self):
        """ Action slot
        """
        self.client.setPort(self.lineEdit_port.text())
        self.updateInfo()

    def setRegAddr(self):
        """ Action slot
        """
        self.client.setRegisterStartAddr(self.lineEdit_regAddr.text())
        self.updateInfo()

    def setAmountOfRegs(self):
        """ Action slot
        """
        self.client.setAmountReg(self.spinBox_numOfReg.value())
        self.updateInfo()

    def updateInfo(self):
        """ Action slot
        """
        self.lineEdit_IP.setText(self.client.getServerIpAddr())
        self.lineEdit_port.setText(self.client.getPort())
        self.lineEdit_regAddr.setText(self.client.getRegisterStartAddr())
        self.spinBox_numOfReg.setValue(self.client.getAmountReg())
        # self.checkBox_Connected.setChecked(self.client.getConnectionStatus())


    def connectToServerToggle(self):
        """ Action slot
        """
        if self.checkBox_Connected.isChecked():
            self.client.connectServer()
        elif (self.checkBox_Connected.isChecked() == False):
            self.client.disconnectServer()

        # self.updateInfo()


    def readHoldingRegisters(self):
        """ Action slot
        """
        self.regResponse = self.client.readHoldingRegs()

        # Print the collected data
        if self.regResponse > 0:
            self.textBrowser.clear()
            for i in range(len(self.regResponse.registers)):
                self.textBrowser.append("r%s: " % str(i) + str(self.regResponse.getRegister(i)))
        # else: print "Nothing to show."    #TODO: remove

        self.updateInfo()

class ModbusClient():

    def __init__(self):
        self.serverIpAddr = "192.168.2.35"  # Initial IP address is set to localhost
        self.port = 502 # Initial port is set to 502 (standard modbus port)
        self.regStartAddr = 0  # Initial starting register address
        self.amountReg = 10  # Initial number of registers to retrieve

    def connectServer(self):
        """ Connect to a modbus TCP server

        :return: VOID
        """
        try:
            self.modbusConn = ModbusTcpClient(host = self.serverIpAddr, port = self.port)
            # print "connectServer executed"  #TODO: remove
        except Exception:
            print "Could not connect to a modbus server."

    def disconnectServer(self):
        """ Disconnect from a modbus TCP server

        :return: VOID
        """
        try:
            self.modbusConn.close()
            # print "disconnectServer executed" #TODO: remove
        except Exception:
            # print "No connection to close."
            pass

    def readHoldingRegs(self):
        """ Read the contiguous block of registers of size 'cnt', starting from the address 'addr'

        :param regAddr: INTEGER
        :param amountReg: INTEGER
        :return: OBJECT
        """
        try:
            self.modbusConn = ModbusTcpClient(host = self.serverIpAddr, port = self.port)
        except Exception:
            print "Exception: Could not connect to a modbus server."

        try:
            return self.modbusConn.read_holding_registers(self.regStartAddr, self.amountReg)
        except Exception:
            print "Exception: Could not read modbus registers."

    def setServerIpAddr(self, ipStr):
        """ Sets the IP address of the modbus server to connect to.

        :param ipStr: STRING "0.0.0.0" -- "255.255.255.255"
        """
        if self.isValidIpV4(ipStr):
            ipStrList = ipStr.split(".")
            # ipIntList = []
            for i in range(0,4):
                ipStrList[i] = str(int(ipStrList[i]))
                # ipIntList.append(int(ipStrList[i]))
            # print ipIntList
            self.serverIpAddr = ipStrList[0] + "." + ipStrList[1] + "." + ipStrList[2] + "." + ipStrList[3]

    def setPort(self, portStr):
        """ Sets the port to a value between 0 and 65535 (modbus is normally on port 502).

        :param portStr: STRING
        :return: VOID
        """
        try:
            if 0 <= int(portStr) <= 65535: self.port = int(portStr)
            else: raise portValueError  #FIXME: Figure out exception handling
        except Exception, portValueError:
            pass

    def setRegisterStartAddr(self, regStartAddrStr):
        """ Sets the starting address of a contiguous block of registers to read from.

        :param regStartAddrStr: STRING
        :return: VOID
        """
        try:
            if 0 <= int(regStartAddrStr) <= 65535: self.regStartAddr = int(regStartAddrStr)
            else: raise registerValueError  #FIXME: Figure out exception handling
        except Exception, registerValueError:
            pass

    def setAmountReg(self, amountRegInt):
        """ Sets the amount of registers (in a contiguous block) to read from.

        :param amountRegInt: INTEGER
        :return: VOID
        """
        try:
            if 0 < amountRegInt <= 99: self.amountReg = int(amountRegInt)
            else: raise registerValueError
        except Exception, registerValueError:   #FIXME: Figure out exception handling
            pass

    def getServerIpAddr(self):  # TODO: zero suppress
        """

        :return: STRING
        """
        return self.serverIpAddr

    def getPort(self):
        """

        :return: STRING
        """
        return str(self.port)

    def getAmountReg(self):
        """

        :return: INTEGER
        """
        return self.amountReg

    def getRegisterStartAddr(self):
        """

        :return: STRING
        """
        return str(self.regStartAddr)

    def isValidIpV4(self, ip):
        """ Checks the user input of an IPv4 address

        :param ip: STRING
        :return: BOOLEAN
        """
        try:
            ips = ip.split(".") # split the string on a period
            if ips.__len__() == 4:
                for i in ips:
                    if not i.isdigit() or not (0 <= int(i) <= 255):
                        # print "error1"
                        raise ipValueError

                return True
            else:
                # print "error2"
                raise ipValueError

        except Exception, ipValueError:
            # print "error3"
            return False

    # def getConnectionStatus(self):
    #     print "----- checking..."
    #     try:
    #         if (self.modbusConn):
    #             print "Connected."
    #             return True
    #         else:
    #             print "Not connected."
    #             return False
    #     except Exception:
    #         print "no connection Exception!"
    #         return False


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    form = Window()
    sys.exit(app.exec_())