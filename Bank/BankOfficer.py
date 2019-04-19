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
    	self.accnum=0
    	pass
    def create_client(self,name1,name2,id,age,contra,initialvalue):
    	
    	for z in self.clientes:
    		if z[2]== id:
    			return "Cliente ya existe"
    		else:
    			self.cliente= [name1,name2,id,age] 
    			self.cuentas= [contra,self.accnum, initialvalue, "Unblock"] ##0 significa cuenta desbloqueada
    			self.accnum+=1
    			self.cliente.append(self.cuentas)
    			self.clientes.append(self.cliente)
    			return "Cliente creado"
    	self.cliente= [name1,name2,id,age] ## Se hace este debido a que si no hay cuentas no se entra al ciclo for in
    	self.cuentas= [contra,self.accnum, initialvalue,"Unblock"]
    	self.accnum+=1
    	self.cliente.append(self.cuentas)
    	self.clientes.append(self.cliente)
    	return "Cliente creado"
    			
    def update_client(self,name1,name2,newid,age,oldid):
    	self.cliente= [name1,name2,newid,age]
    	i=0
    	for z in self.clientes:
    		if z[2]==oldid:
    			self.cliente.append(z[5])
    			self.clientes[i]=self.cliente
    			return "Exito"
    		else:    			
    			i+=1
    	return "Cliente no encontrado"
    def consul_client(self, id):
    	for z in self.clientes:
    		if z[2]== id:
    			return z
    	return "Cliente no encontrado"
    def create_accoun(self, id, key, initialvalue):
    	for z in self.clientes:
    		if z[2]== id:
    			newaccount= [key,self.accnum,initialvalue,"Unblock"]
    			z.append(newaccount)
    			self.accnum+=1
    			return "Cuenta creada"
    			pass
    	return "Cliente no encontrado, no se pudo crear la cuenta"
    def Block_Unblockacc(self,idacc,key,state):
    	cont=0
    	for z in self.clientes:
    		cont+=1
    	for x in range(0,cont):
    		i= 0

    		for l in self.clientes[x]:
    			i+=1
    		for y in range(4,i):
    			for g in self.clientes[x][y]:
    				##print(g)
    				##print(i)
    				##print(x)
    				##print(y)
    				if g== key :
    					for m in self.clientes[x][y]:
    						if m== idacc:
    							self.clientes[x][y][3]=state
    							return"Estado cambiado"

    					pass

    		##print(i)

    	return "Cuenta no encontrada, o clave incorrecta"


app= QApplication(sys.argv)
ui=BankOfficer()
ui.setWindowTitle('Test')
ui.create_client("kk","el",10,19,"kss",1000)
ui.create_client("kk2","el2",12,19,"kss",1000)
ui.create_client("kk2","el2",13,19,"kss",1000)
print(ui.create_accoun(12,"kks2",10))
print(ui.Block_Unblockacc(2,"kss","Block"))
print(ui.clientes)
ui.show()
ret= app.exec_()
sys.exit(ret)
