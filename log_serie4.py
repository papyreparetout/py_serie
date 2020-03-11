# -*- coding: utf-8 -*-

# Programme permettant de recuperer les donnees emises sur une liaison serie
# interface Qt pour préciser le port et la vitesse de transmission
# Created by: PyQt5 UI code generator 5.5.1
#
# 

import datetime
import time
import os
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
import serial.tools.list_ports

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(593, 576)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 40, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(320, 30, 81, 20))
        self.label_2.setObjectName("label_2")
        self.vitesse = QtWidgets.QLineEdit(Dialog)
        self.vitesse.setGeometry(QtCore.QRect(320, 60, 91, 20))
        self.vitesse.setObjectName("vitesse")
        self.vitesse.setAlignment(Qt.AlignRight)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 130, 541, 331))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(196, 0, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.debutrec = QtWidgets.QPushButton(Dialog)
        self.debutrec.setGeometry(QtCore.QRect(114, 510, 91, 23))
        self.debutrec.setObjectName("debutrec")
        self.finrec = QtWidgets.QPushButton(Dialog)
        self.debutrec.clicked.connect(self.btndebrec)
        self.finrec.setGeometry(QtCore.QRect(350, 510, 75, 23))
        self.finrec.setObjectName("finrec")
        self.finrec.clicked.connect(self.btnfinrec)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(28, 60, 261, 22))
        self.comboBox.setObjectName("comboBox")
        ports = serial.tools.list_ports.comports(include_links=False)
        nbport = 0
        listport = []
        for port, desc, hwid in sorted(ports):
            listport.append(port + " : "+ desc)
            self.comboBox.addItem(listport[nbport])
            nbport = nbport + 1
        self.comboBox.activated.connect(self.onActivated)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Port COM"))
        self.label_2.setText(_translate("Dialog", "vitesse (baud)"))
        self.label_3.setText(_translate("Dialog", "Logger liaison série via USB"))
        self.debutrec.setText(_translate("Dialog", "Enregistrement"))
        self.finrec.setText(_translate("Dialog", "Arrêt"))

    def onActivated(self):
        print(str(self.comboBox.currentText()))
        self.plainTextEdit.insertPlainText("port choisi: " + str(self.comboBox.currentText()))

    def btndebrec(self):
        baud = 0
        port = self.comboBox.currentText()
        ipoint = port.find(":")
        portc = port[0:ipoint-1]
        baud = self.vitesse.text()
        ibaud = int(baud)
        print("port "+portc + " Vitesse "+ baud)
        print("debut enregistrement")
        self.plainTextEdit.appendPlainText(" Début d'enregistrement")
        # creation fichier de stockage des donnees lues
        outputFilePath = os.path.join(os.path.dirname(__file__),
        datetime.datetime.now().strftime("%Y-%m-%dT%H.%M.%S") + ".bin")
        self.plainTextEdit.appendPlainText(str(outputFilePath))
        time.sleep(1)
        with serial.Serial(portc, ibaud) as ser, open(outputFilePath, mode='wb') as outputFile:
            print("Logging demarre. Ctrl-C to stop.")
            print("Fichier résultat : "+outputFilePath)
            try:
                while True:
                    time.sleep(5)
#                    outputFile.write((ser.read(ser.inWaiting())))
#                    outputFile.flush()
                    QtWidgets.QApplication.processEvents()
                    datar = ser.read(ser.inWaiting())
                    outputFile.write(datar)
                    outputFile.flush()
#                    self.plainTextEdit.insertPlainText(" Début d'enregistrement")
#                    print(str(datar))
            except KeyboardInterrupt:
                print("Logging demarre")
            finally:
                print("Fin d'enregistrement")

        
    def btnfinrec(self):
        self.plainTextEdit.appendPlainText(" Fin d'enregistrement")
#        print("fin d'enregistrement")
        time.sleep(5)
        sys.exit("fin programme")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

