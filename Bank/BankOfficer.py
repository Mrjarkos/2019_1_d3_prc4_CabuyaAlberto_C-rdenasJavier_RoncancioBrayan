# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import (QApplication, QDialog, QMainWindow, QFileDialog, QWidget, QMessageBox, QTableWidget, QTableWidgetItem)
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer,QRegExp
from PyQt5.QtGui import QPixmap,QImage,QRegExpValidator
import threading

class BankOfficerinterface(QMainWindow):
	"""docstring for ClassName"""
	def __init__(self):
		super(BankOfficerinterface, self).__init__(None)
		loadUi('bankofficial.ui',self)
		self.bankfunk=BankOfficer()
		

class BankOfficer():
    def __init__(self):
    	
    	
    	self.clientes= []
    	self.accnum=0
    	self.cuentasgen=[]
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
    			self.cuentasgen.append(self.cuentas)
    			return "Cliente creado"
    	self.cliente= [name1,name2,id,age] ## Se hace este debido a que si no hay cuentas no se entra al ciclo for in
    	self.cuentas= [contra,self.accnum, initialvalue,"Unblock"]
    	self.accnum+=1
    	self.cliente.append(self.cuentas)
    	self.clientes.append(self.cliente)
    	self.cuentasgen.append(self.cuentas)
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
    def consul_account(self, id):
    	for z in self.cuentasgen:
    		if z[1]==id:
    			return z
    	return "Cuenta no existe"
    def create_accoun(self, id, key, initialvalue):
    	for z in self.clientes:
    		if z[2]== id:
    			newaccount= [key,self.accnum,initialvalue,"Unblock"]
    			z.append(newaccount)
    			self.cuentasgen.append(newaccount)
    			self.accnum+=1
    			return "Cuenta creada"
    			pass
    	return "Cliente no encontrado, no se pudo crear la cuenta"
    def update_account(self, id):
    	for accounn in self.cuentasgen:
    		if accounn[1]==id:
    			updatedaccount=accounn
    	cont=0
    	for z in self.clientes:
    		cont+=1
    	for x in range(0,cont):
    		i= 0

    		for l in self.clientes[x]:
    			i+=1
    		for y in range(4,i):
    			for g in self.clientes[x][y]:
    				if g== id:
    					self.clientes[x][y]=updatedaccount
    					##print(updatedaccount)
    					return "Cuenta actualizada"

    def Block_Unblockacc(self,idacc,key,state):
    	cont=0
    	for z in self.cuentasgen:
    		if z[0]==key and z[1]== idacc:
    			self.cuentasgen[cont][3]= state
    			self.update_account(idacc)
    			return "Estado de cuenta cambiado"
    		cont+=1




    	return "Cuenta no encontrada, o clave incorrecta"
    def Deposit(self, idacc,ammount):
    	cont=0
    	for z in self.cuentasgen:
    		if z[1]==idacc:
    			if z[3]=="Block":
    				return "cuenta bloqueada"
    			else:
    				self.cuentasgen[cont][2]+=ammount
    				self.update_account(idacc)
    				return "Deposito realizado"
    		cont+=1
    	return "Error al realizar el deposito cuenta inexistente"
    def withdrawal(self, idacc, ammount, key):
    	cont=0
    	for z in self.cuentasgen:
    		if z[0]==key and z[1]==idacc:
    			if z[3]== "Block":
    				return "Cuenta bloqueada"
    			elif z[2]-ammount<0:
    				return "No se tienen los fondos suficientes en la cuenta"
    			else:
    				self.cuentasgen[cont][2]-=ammount
    				self.update_account(idacc)
    				return "Retiro realizado"
    		cont+=1
    	return "Error al realizar el retiro"
    def transfer_money(self, idacc1, key, idacc2, ammount):
    	k=self.withdrawal(idacc1,ammount, key)
    	if k== "Retiro realizado":
    		res=self.Deposit(idacc2,ammount)
    		if res== "Deposito realizado":
    			return "Transferencia realizada"
    			pass
    		else:
    			return res
    	else:
    		return k

app= QApplication(sys.argv)
ui=BankOfficerinterface()
ui.bankfunk.create_client("kk","el",10,19,"kss",1000)
ui.bankfunk.create_client("kk2","el2",12,19,"kss",1000)
ui.bankfunk.create_client("kk2","el2",13,19,"kss",1000)
print(ui.bankfunk.create_accoun(12,"kks2",10))
print(ui.bankfunk.Block_Unblockacc(2,"kss","Block"))
print(ui.bankfunk.withdrawal(3, 10,"kks2"))
print(ui.bankfunk.transfer_money(0,"kss",1, 1000))
print(ui.bankfunk.clientes)
print(ui.bankfunk.cuentasgen)
ui.show()
ret= app.exec_()
sys.exit(ret)
