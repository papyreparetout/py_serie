# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'envoi_serie.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# envoi des donnees d'un fichier sur une liaison série
#
import os, sys, time
import serial.tools.list_ports
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QInputDialog, QLineEdit,
QPushButton, QProgressBar,
QSlider, QWidget,
QApplication, 
QMessageBox,QFileDialog)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(729, 588)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 50, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(500, 40, 81, 20))
        self.label_2.setObjectName("label_2")
        self.vitesse = QtWidgets.QLineEdit(Dialog)
        self.vitesse.setGeometry(QtCore.QRect(500, 80, 91, 20))
        self.vitesse.setObjectName("vitesse")
        self.vitesse.setAlignment(Qt.AlignRight)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(196, 0, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.debutenv = QtWidgets.QPushButton(Dialog)
        self.debutenv.setGeometry(QtCore.QRect(200, 510, 91, 23))
        self.debutenv.setObjectName("debutenv")
        self.debutenv.clicked.connect(self.btndebenv)
        self.finenv = QtWidgets.QPushButton(Dialog)
        self.finenv.setGeometry(QtCore.QRect(490, 510, 75, 23))
        self.finenv.setObjectName("finenv")
        self.finenv.clicked.connect(self.btnfinenv)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(30, 80, 441, 22))
        self.comboBox.setObjectName("comboBox")
        # on remplit la combobox avec la liste des ports
        ports = serial.tools.list_ports.comports(include_links=False)
        nbport = 0
        listport = []
        for port, desc, hwid in sorted(ports):
            listport.append(port + " : "+ desc)
            self.comboBox.addItem(listport[nbport])
            nbport = nbport + 1
        self.comboBox.activated.connect(self.onActivated)
        
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(90, 300, 541, 161))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.choixfich = QtWidgets.QPushButton(Dialog)
        self.choixfich.setGeometry(QtCore.QRect(50, 190, 75, 23))
        self.choixfich.setObjectName("choixfich")
        self.choixfich.clicked.connect(self.btchoix)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(50, 160, 91, 16))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Port COM"))
        self.label_2.setText(_translate("Dialog", "vitesse (baud)"))
        self.label_3.setText(_translate("Dialog", "Envoi données sur  liaison série via USB"))
        self.debutenv.setText(_translate("Dialog", "Envoi"))
        self.finenv.setText(_translate("Dialog", "Arrêt"))
        self.choixfich.setText(_translate("Dialog", "choix fich"))
        self.label_4.setText(_translate("Dialog", "Fichier donnees"))

    def onActivated(self):
        print(str(self.comboBox.currentText()))
        self.plainTextEdit.insertPlainText("port choisi: " + str(self.comboBox.currentText()))

    def btndebenv(self):
        global fichdonn
        baud = 0
        port = self.comboBox.currentText()
        ipoint = port.find(":")
        portc = port[0:ipoint-1]
        baud = self.vitesse.text()
        ibaud = int(baud)
        print("port "+portc + " Vitesse "+ baud)
        print("debut envoi")
        self.plainTextEdit.appendPlainText(" Début d'envoi")
        # lecture fichier des donnees et envoi sur la liaison serie
#        self.plainTextEdit.appendPlainText(str(outputFilePath))
        time.sleep(1)
        with serial.Serial(portc, ibaud) as ser, open(fichdonn,"r") as donnee:
            print("Envoi demarre. Ctrl-C to stop.")
            try:
                while True:
                    byteread = donnee.read(1)
                    if (not byteread):
                        break
        #            time.sleep(1)
                    ser.write(byteread)
        #            outputFile.flush()
            except KeyboardInterrupt:
                print("Envoi demarre")
            finally:
                print("Fin d'envoi")
        
    def btnfinenv(self):
        self.plainTextEdit.appendPlainText(" Fin d'envoi")
#        print("fin d'enregistrement")
        time.sleep(5)
        sys.exit("fin programme")
        
    def btchoix(self):
        global fichdonn
        # choix du fichier de donnees
        dossier = QFileDialog.getOpenFileName()
        self.plainTextEdit.appendPlainText(
               "Fichier sélectionné : "+str(dossier) +'\n')
        print(str(dossier))
        print(dossier[0])
        fichdonn = dossier[0]
        pass
        
if __name__ == "__main__":
#    import sys
    global fichdonn
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

