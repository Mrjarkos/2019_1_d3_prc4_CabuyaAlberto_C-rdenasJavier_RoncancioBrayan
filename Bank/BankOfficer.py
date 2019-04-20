# -*- coding: utf-8 -*-
import sys
import os
from PyQt5.QtWidgets import (QApplication, QDialog, QMainWindow, QFileDialog, QWidget, QMessageBox, QTableWidget, QTableWidgetItem)
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import threading


class Getaccountdata(QWidget):
	"""docstring for Getaccountdata"""
	def __init__(self, arg):
		super(Getaccountdata, self).__init__(None)
		loadUi('accountdata.ui')
		self.arg = arg
		
class Mostrarlist(QMainWindow):
	"""docstring for Mostrarlist"""
	def __init__(self):
		super(Mostrarlist, self).__init__(None)
		loadUi('mostar.ui',self)
class Getdataclient(QWidget):
			"""docstring for Getdataclient"""
			def __init__(self, arg):
				super(Getdataclient, self).__init__(None)
				loadUi('dataclient.ui',self)
				self.arg= arg	
				self.Ok.clicked.connect(self.Ok_clicked)
			def Ok_clicked(self):
				Name1= self.Name.toPlainText()
				Lastname= self.Lastname.toPlainText()
				cc=self.cc.toPlainText()
				contra= self.contrasea.toPlainText()
				initmoney=self.money.toPlainText()
				msg= self.arg.create_client(Name1,Lastname,cc,contra,initmoney)
				QMessageBox.warning(self,"Resultado",msg)


class BankOfficerinterface(QMainWindow):
	"""docstring for ClassName"""
	def __init__(self):
		super(BankOfficerinterface, self).__init__(None)
		loadUi('bankofficial.ui',self)
		self.bankfunk=BankOfficer()
		self.Mostrarclientes.clicked.connect(self.Mostrarclientes_clicked)
		self.Mostrarcuentas.clicked.connect(self.Mostrarcuentas_clicked)
		self.Crearcliente.clicked.connect(self.Crearcliente_clicked)
		self.Crearcuenta.clicked.connect(self.Crearcuenta_clicked)
		self.thradq= QThread()
		self.thradq2= QThread()
		self.thradq3= QThread()
		self.thradq4= QThread()
	def Mostrarclientes_clicked(self):
		self.thradq.started.connect(self.mostraracclist)
		self.thradq.start()
	def Mostrarcuentas_clicked(self):
		self.thradq2.started.connect(self.mostrarcountlis)
		self.thradq2.start()
	def Crearcliente_clicked(self):
		self.thradq3.started.connect(self.getclientdata)
		self.thradq3.start()
	def Crearcuenta_clicked(self):
		self.thradq4.started.connect(self.getaccountdata)
		self.thradq4.start()


	def mostraracclist(self):
		self.mostrarlist=Mostrarlist()
		self.mostrarlist.setWindowTitle('Lista de clientes')
		cont=0
		for z in self.bankfunk.clientes:
			cont+=1
		for x in range(0,cont):
			item= self.bankfunk.clientes[x].copy()
			##item[2]= str(item[2])
			#item[3]= str(item[3])
			item.pop()
			item.pop()
			str1= ' '.join(item)
			str1= "Cliente: "+str1
			self.mostrarlist.listWidget.addItem(str1)
		##self.mostrarlist.listView.setViewMode(QtGui.QListView.I)
		self.mostrarlist.label.setText("Lista de clientes guardados")
		self.mostrarlist.show()
		self.thradq.quit()
	def mostrarcountlis(self):
		self.mostrarlist2=Mostrarlist()	
		self.mostrarlist2.setWindowTitle('Lista de cuentas')	
		cont=0
		for z in self.bankfunk.clientes:
			cont+=1
		for x in range(0,cont):
			item= self.bankfunk.clientes[x].copy()
			item2= self.bankfunk.cuentasgen[x].copy()
			#item[2]= str(item[2])
			#item[3]= str(item[3])
			item.pop()
			item.pop()
			item2[1]=str(item2[1])
			#item2[2]=str(item2[2])
			item2.pop(0)
			str2= ' '.join(item2)
			str1= ' '.join(item)
			str1= "Cliente: "+str1
			item3= [str1, str2]
			str3= ' cuenta: '.join(item3)
			self.mostrarlist2.listWidget.addItem(str3)
		##self.mostrarlist.listView.setViewMode(QtGui.QListView.I)
		self.mostrarlist2.label.setText("Lista de cuentas guardadas")
		self.mostrarlist2.show()
		self.thradq2.quit()
	def getclientdata(self):
		self.getclientdata= Getdataclient(self.bankfunk)
		self.getclientdata.setWindowTitle("Client data")
		self.getclientdata.show()
		self.thradq3.quit()
	def getaccountdata(self):
		self.getaccountdata= Getaccountdata(self.bankfunk)
		self.getaccountdata.setWindowTitle("Account data")
		self.getaccountdata.show()
		self.thradq4.quit()







class BankOfficer():
    def __init__(self):
    	
    	##self.clientesolo= []
    	self.clientes= []
    	self.accnum=0
    	self.cuentasgen=[]

    	pass
    def create_client(self,name1,name2,id,contra,initialvalue):
    	
    	for z in self.clientes:
    		if z[2]== id:
    			return "Cliente ya existe"	
    	self.cliente= [name1,name2,id,contra] ## Se hace este debido a que si no hay cuentas no se entra al ciclo for in
    	self.cuentas= [contra,self.accnum, initialvalue,"Unblock"]
    	self.accnum+=1
    	##self.clientesolo.append(self.cliente)
    	self.cliente.append(self.cuentas)
    	self.clientes.append(self.cliente)
    	self.cuentasgen.append(self.cuentas)
    	return "Cliente creado"
    			
    def update_client(self,name1,name2,newid,oldid):
    	self.cliente= [name1,name2,newid]
    	i=0
    	for z in self.clientes:
    		if z[2]==oldid:
    			self.cliente.append(Z[3])
    			self.cliente.append(z[4])
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
    		if z[2]== id and z[3]== key:
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
ui.show() 
ret= app.exec_()
sys.exit(ret)
