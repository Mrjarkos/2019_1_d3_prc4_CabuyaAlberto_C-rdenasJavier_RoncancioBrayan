# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import (QApplication, QDialog, QMainWindow, QFileDialog, QWidget, QMessageBox, QTableWidget, QTableWidgetItem)
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer,QRegExp
from PyQt5.QtGui import QPixmap,QImage,QRegExpValidator
import threading


class BankOfficer(QMainWindow):
    def __init__(self):
    	super(BankOfficer,self).__init__(None)
    	loadUi('bankofficial.ui',self)
    	self.clientes= []
    	pass
    def create_client(self,name1,name2,id,age,contra):
    	self.cliente= [name1,name2,id,age,contra]
    	self.cuentas= []
    	self.cliente.append(cuentas)
    	self.clientes.append(cliente)
    	return "Cliente creado"
    def update_client(self,name1,name2,id,age,contra):
    	self.cliente= [name1,name2,id,age,contra]
    	self.status = cliente in self.clientes
    	if self.status == True:
            	self.posid=self.clientes.index(cliente)
            	self.clientes[posid]=[name1,name2,id,age,contra]
            	return "Exito"
            	pass
    	else: 
            	return "Cliente no encontrado"
app= QApplication(sys.argv)
ui=BankOfficer()
ui.setWindowTitle('Test')
ui.show()
ret= app.exec_()
sys.exit(ret)
