#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
PyQt4 Tutorials template
https://www.youtube.com/channel/UCpjNEyIUW8E8ZQ0JbYA8isw
author: Davor Afric
last edited: October 2016
"""

import sys, modBusGui_4v2
from PyQt4 import QtCore, QtGui
from pymodbus.client.sync import ModbusTcpClient


class Form(QtGui.QDialog, modBusGui_4v2.Ui_MainWindow):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.client = ModbusClient()
        self.setupUi(self)
        self.button_dummy = QtGui.QPushButton(self.centralwidget)
        self.initUi()


    def initUi(self):
        """ Initialize the GUI """

        # FIXME: requestBtn gets called on returnPressed event in any lineEdit object
        self.button_request.pressed.connect(self.readHoldingRegisters)
        """ 2016-10-23: Creating an instance of a dummy QtGui.QpushButton object before the button_request
            creation in the modBusGui_4v2.py seems to fix the problem with unexpected signals from button_request.
        """

        # self.checkBox_Connected.clicked.connect(self.connectToServer) #TODO: figure out

        self.lineEdit_IP.setText(self.client.getServerIpAddr())
        self.lineEdit_IP.returnPressed.connect(self.setIp)
        self.lineEdit_IP.returnPressed.connect(self.setText)

        self.lineEdit_port.setText(self.client.getPort())
        self.lineEdit_port.returnPressed.connect(self.setPort)
        self.lineEdit_port.returnPressed.connect(self.setText)

        self.lineEdit_regAddr.setText(self.client.getRegisterStartAddr())
        self.lineEdit_regAddr.returnPressed.connect(self.setRegAddr)
        self.lineEdit_regAddr.returnPressed.connect(self.setText)

        self.spinBox_numOfReg.setValue(self.client.getAmountReg())
        self.spinBox_numOfReg.valueChanged.connect(self.setAmountOfRegs)
        self.spinBox_numOfReg.valueChanged.connect(self.setText)

        self.action_Quit.activated.connect(QtGui.QApplication.exit)

        self.action_Anounce.activated.connect(self.anounce)


    def anounce(self):  # TODO: remove this method
        self.textBrowser.clear()
        self.textBrowser.append("IP Address:  " + self.client.getServerIpAddr())
        self.textBrowser.append("Port:  " + self.client.getPort())
        self.textBrowser.append("Starting Register:  " + self.client.getRegisterStartAddr())
        self.textBrowser.append("Amount of Registers:  " + str(self.client.getAmountReg()))
        self.textBrowser.append("-----------")

    def setIp(self):
        self.client.setServerIpAddr(unicode(self.lineEdit_IP.text()))

    def setPort(self):
        self.client.setPort(self.lineEdit_port.text())

    def setRegAddr(self):
        self.client.setRegisterStartAddr(self.lineEdit_regAddr.text())

    def setAmountOfRegs(self):
        self.client.setAmountReg(self.spinBox_numOfReg.value())

    def setText(self):
        self.lineEdit_IP.setText(self.client.getServerIpAddr())
        self.lineEdit_port.setText(self.client.getPort())
        self.lineEdit_regAddr.setText(self.client.getRegisterStartAddr())
        self.spinBox_numOfReg.setValue(self.client.getAmountReg())

    def connectToServer(self):
        self.client.connectServer()

    def readHoldingRegisters(self):
        self.client.connectServer()
        self.regResponse = self.client.readHoldingRegs()

        # Print the collected data
        self.textBrowser.clear()
        for i in range(len(self.regResponse.registers)):
            self.textBrowser.append("r_%s: " % str(i) + str(self.regResponse.getRegister(i)))

    def about(self):
        self.textBrowser.clear()
        self.textBrowser.append("This is a ")

class ModbusClient():

    def __init__(self):
        self.serverIpAddr = "192.168.5.102"  # Initial IP address is set to localhost
        self.port = 502 # Initial port is set to 502 (standard modbus port)
        self.regStartAddr = 0  # Initial starting register address
        self.amountReg = 10  # Initial number of registers to retrieve

    def connectServer(self):
        """ Connect to a modbus TCP server

        :return: VOID
        """
        self.modbusConn = ModbusTcpClient(host = self.serverIpAddr, port = self.port)

    def readHoldingRegs(self):
        """ Read the contiguous block of registers of size 'cnt', starting from the address 'addr'

        :param regAddr: INTEGER
        :param amountReg: INTEGER
        :return: OBJECT
        """
        return self.modbusConn.read_holding_registers(self.regStartAddr, self.amountReg)

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


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec_())