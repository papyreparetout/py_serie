# -*- coding: utf-8 -*-
#
# 
import datetime
import time
import os
import platform
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
import serial.tools.list_ports
from PyQt5 import QtSerialPort
from PyQt5.QtSerialPort import QSerialPortInfo

def get_serial_ports():
    """
     Liste les ports serie disponibles avec leur description

    """
    info_list = QSerialPortInfo()
    serial_list = info_list.availablePorts()
    serial_ports = []
    for port in serial_list:
        name = port.portName()
        descr = port.description()
        serial_ports.append(name + " : "+ descr)
    return serial_ports


class Ui_Serial(object):
    def setupUi(self, Serial):
        Serial.setObjectName("Serial")
        Serial.resize(770, 650)
        font = QtGui.QFont()
        font.setPointSize(12)
        Serial.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(Serial)
        self.gridLayout.setObjectName("gridLayout")
        self.debut = QtWidgets.QPushButton(Serial)
        self.debut.setObjectName("debut")
        self.gridLayout.addWidget(self.debut, 6, 4, 2, 1)
        self.separ = QtWidgets.QLabel(Serial)
        self.separ.setText("")
        self.separ.setObjectName("separ")
        self.gridLayout.addWidget(self.separ, 9, 2, 1, 1)
        self.choixdata = QtWidgets.QSpinBox(Serial)
        self.choixdata.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.choixdata.setMinimum(7)
        self.choixdata.setMaximum(8)
        self.choixdata.setObjectName("choixdata")
        self.gridLayout.addWidget(self.choixdata, 7, 1, 1, 1)
        self.choixpar = QtWidgets.QComboBox(Serial)
        self.choixpar.setObjectName("choixpar")
        self.gridLayout.addWidget(self.choixpar, 8, 1, 1, 1)
        self.stopbit = QtWidgets.QLabel(Serial)
        self.stopbit.setObjectName("stopbit")
        self.gridLayout.addWidget(self.stopbit, 9, 0, 1, 1)
        self.choixport = QtWidgets.QComboBox(Serial)
        self.choixport.setObjectName("choixport")
        self.gridLayout.addWidget(self.choixport, 2, 1, 1, 1)
        self.envoicar = QtWidgets.QLineEdit(Serial)
        self.envoicar.setObjectName("envoicar")
        self.gridLayout.addWidget(self.envoicar, 9, 4, 1, 2)
        self.texterecu = QtWidgets.QTextEdit(Serial)
        self.texterecu.setObjectName("texterecu")
        self.gridLayout.addWidget(self.texterecu, 1, 0, 1, 6)
        self.fin = QtWidgets.QPushButton(Serial)
        self.fin.setObjectName("fin")
        self.gridLayout.addWidget(self.fin, 6, 5, 2, 1)
        self.baudrate = QtWidgets.QLabel(Serial)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.baudrate.setFont(font)
        self.baudrate.setObjectName("baudrate")
        self.gridLayout.addWidget(self.baudrate, 4, 0, 1, 1)
        self.port = QtWidgets.QLabel(Serial)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.port.setFont(font)
        self.port.setObjectName("port")
        self.gridLayout.addWidget(self.port, 2, 0, 1, 1)
        self.paritybit = QtWidgets.QLabel(Serial)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.paritybit.setFont(font)
        self.paritybit.setObjectName("paritybit")
        self.gridLayout.addWidget(self.paritybit, 8, 0, 1, 1)
        self.Recus = QtWidgets.QLabel(Serial)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Recus.setFont(font)
        self.Recus.setObjectName("Recus")
        self.gridLayout.addWidget(self.Recus, 0, 0, 1, 1)
        self.databit = QtWidgets.QLabel(Serial)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.databit.setFont(font)
        self.databit.setObjectName("databit")
        self.gridLayout.addWidget(self.databit, 7, 0, 1, 1)
        self.handshake = QtWidgets.QLabel(Serial)
        self.handshake.setObjectName("handshake")
        self.gridLayout.addWidget(self.handshake, 10, 0, 1, 1)
        self.choixhand = QtWidgets.QComboBox(Serial)
        self.choixhand.setObjectName("choixhand")
        self.gridLayout.addWidget(self.choixhand, 10, 1, 1, 1)
        self.choixstop = QtWidgets.QComboBox(Serial)
        self.choixstop.setObjectName("choixstop")
        self.gridLayout.addWidget(self.choixstop, 9, 1, 1, 1)
        self.envoi = QtWidgets.QPushButton(Serial)
        self.envoi.setObjectName("envoi")
        self.gridLayout.addWidget(self.envoi, 9, 3, 1, 1)
        self.finligne = QtWidgets.QLabel(Serial)
        self.finligne.setObjectName("finligne")
        self.gridLayout.addWidget(self.finligne, 4, 3, 1, 1)
        self.choixfinl = QtWidgets.QComboBox(Serial)
        self.choixfinl.setObjectName("choixfinl")
        self.gridLayout.addWidget(self.choixfinl, 4, 4, 1, 1)
        self.choixbaud = QtWidgets.QLineEdit(Serial)
        self.choixbaud.setObjectName("choxbaud")
        self.choixbaud.setAlignment(Qt.AlignRight)
        self.gridLayout.addWidget(self.choixbaud, 4, 1, 1, 1)

        self.retranslateUi(Serial)
        QtCore.QMetaObject.connectSlotsByName(Serial)

        # ajouts
        self.liststop = ["one", "one and half", "two"]  # 1,3,2
        self.choixstop.addItems(self.liststop)
        self.listpar = ["none", "even","odd","space", "mark"] # 0, 2, 3, 4, 5
        self.choixpar.addItems(self.listpar)
        self.listhand = ["none", "RTS/CTS","XonXoff"]  # 0, 1, 2
        self.listfinl =["CR/LF","CR","none"]
        self.choixfinl.addItems(self.listfinl)
        self.choixhand.addItems(self.listhand)
        self.choixdata.setValue(8)
        self.choixbaud.setText("9600")
        ports = get_serial_ports()
        nbport = 0
        listport = []
        for port in sorted(ports):
            listport.append(port) # + " : "+ desc)
            self.choixport.addItem(listport[nbport])
            nbport = nbport + 1
        self.debut.clicked.connect(self.debenreg)
        self.fin.clicked.connect(self.finenreg)
        self.envoi.clicked.connect(self.send)
        # fin ajouts

    def retranslateUi(self, Serial):
        _translate = QtCore.QCoreApplication.translate
        Serial.setWindowTitle(_translate("Serial", "Dialogue port serie"))
        self.debut.setText(_translate("Serial", "start"))
        self.stopbit.setText(_translate("Serial", "Stopbit"))
        self.fin.setText(_translate("Serial", "stop"))
        self.baudrate.setText(_translate("Serial", "Baud"))
        self.port.setText(_translate("Serial", "Port"))
        self.paritybit.setText(_translate("Serial", "Parity"))
        self.Recus.setText(_translate("Serial", "Recus"))
        self.databit.setText(_translate("Serial", "Data"))
        self.handshake.setText(_translate("Serial", "Handshake"))
        self.envoi.setText(_translate("Serial", "send"))
        self.finligne.setText(_translate("Serial", "car fin ligne"))
        
    def debenreg(self):
        self.outputFile = None
        stoplist = [1,3,2]
        paritelist = [0, 2, 3, 4, 5]
        handshalist = [0, 1, 2]
        finllist = [0,1,2]
        print(str(self.choixport.currentText()))
        port = self.choixport.currentText()
        self.texterecu.insertPlainText("port choisi: " + str(port)+ "\r\n")
        baud = self.choixbaud.text()
        if (baud == ""): baud = "9600"
        self.texterecu.insertPlainText("baudrate choisi: " + str(baud)+ "\r\n")
        nbdata = self.choixdata.value()
        self.texterecu.insertPlainText("data choisi: " + str(nbdata)+ "\r\n")
        parite = self.choixpar.currentText()
        indp = self.listpar.index(parite)
        indpar = paritelist[indp]
        self.texterecu.insertPlainText("parité choisi: " + str(parite)+ "\r\n")
        bitstop = self.choixstop.currentText()
        indb = self.liststop.index(bitstop)
        indbit = stoplist[indb]
        self.texterecu.insertPlainText("stop choisi: " + str(bitstop)+ "\r\n")
        handshake = self.choixhand.currentText()
        indf = self.listhand.index(handshake)
        indflow = handshalist[indf]
        self.texterecu.insertPlainText("handshake choisi: " + str(handshake)+ "\r\n")
        finligne = self.choixfinl.currentText()
        self.indfl = self.listfinl.index(finligne)
        indfinl = finllist[self.indfl]
        self.texterecu.insertPlainText("fin de ligne choisi: " + str(finligne)+ "\r\n")
        ipoint = port.find(":")
        portc = port[0:ipoint-1]
        usersystem = platform.system()
        if (usersystem != "Windows"): portc = "/dev/" + portc
        ibaud = int(baud)
    # creation fichier de stockage des donnees lues
        outputFilePath = os.path.join(os.path.dirname(__file__),
        datetime.datetime.now().strftime("%Y-%m-%dT%H.%M.%S") + ".bin")
    #ouverture du port serie
        self.serial = QtSerialPort.QSerialPort(
            portc,
            readyRead=self.receive
        )
        self.serial.setBaudRate(ibaud)
        self.serial.setDataBits(nbdata)
        self.serial.setParity(indpar)
        self.serial.setStopBits(indbit)
        self.serial.setFlowControl(indflow)
        print("baud :"+str(ibaud)+ " data :"+str(nbdata)+ " parite :"+ str(indpar)+ " stop :"+ str(indbit)+ " flow:" + str(indflow)
            + " fin ligne :"+str(self.indfl)) 
        if not self.serial.isOpen():
            if (self.serial.open(QtCore.QIODevice.ReadWrite)): 
                print("port ouvert")
 #               self.texterecu.clear()
                self.texterecu.insertPlainText("port ouvert" +"\r\n")
                self.texterecu.insertPlainText("fichier :" + str(outputFilePath)+"\r\n")
                self.outputFile = open(outputFilePath, mode='wb') 
            else: 
                print("port impossible à ouvrir")
                self.texterecu.insertPlainText("\r\n"+"port impossible à ouvrir")
                if (self.outputFile != None):
                    if (self.outputFile.open()): self.outputFile.close()
#        self.serial.close() # pour test

    def finenreg(self):
        self.serial.close()
        if (self.outputFile != None): self.outputFile.close()
        self.texterecu.insertPlainText("\r\n"+"port fermé")
        print("port fermé")
        return

    def receive(self):
        listcarf = ["\r\n","\r",""]
        while ( self.serial.atEnd() != True):
            text = self.serial.readLine().data().decode()
            print("recu :"+ str(text))
            text = text.rstrip(listcarf[self.indfl])
            self.texterecu.append(text)
            self.outputFile.write(text.encode())

    def send(self):
        listcarf = ["\r\n","\r",""]
        taenvoi = self.envoicar.text()+ listcarf[self.indfl]
        taenv = "\r\n" + "envoi: " + taenvoi
        self.serial.write(taenvoi.encode())
        self.outputFile.write(taenv.encode())
        print("envoi :"+ str(taenvoi))
        self.envoicar.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Serial = QtWidgets.QWidget()
    ui = Ui_Serial()
    ui.setupUi(Serial)
    Serial.show()
    sys.exit(app.exec_())

