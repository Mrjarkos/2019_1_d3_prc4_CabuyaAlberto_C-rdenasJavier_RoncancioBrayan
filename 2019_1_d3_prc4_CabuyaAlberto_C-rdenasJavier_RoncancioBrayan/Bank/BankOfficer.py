# -*- coding: utf-8 -*-
# !/usr/bin/python
import sys
import os
from PyQt5.QtWidgets import (QApplication, QDialog, QMainWindow, QFileDialog, QWidget, QMessageBox, QTableWidget, QTableWidgetItem)
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
##from construct import Struct, Magic, UBInt32, Const, String
import threading
import time, errno
import ctypes
#from libc.stdlib cimport malloc, free
#from posix.mman cimport mmap, PROT_READ, PROT_WRITE, MAP_SHARED



class Blockunint(QWidget):
	"""docstring for Blockunint"""
	def __init__(self, arg):
		super(Blockunint, self).__init__(None)
		loadUi('blockunbloc.ui',self)
		self.arg = arg
		self.unblock.clicked.connect(self.unblockacc)
		self.block.clicked.connect(self.blockacc)
	def unblockacc(self):
		idacc=self.id.text()
		key= self.Contra.text()
		msg= self.arg.Block_Unblockacc(idacc,key,"Unblock")
		QMessageBox.warning(self,"Resultado",msg)
	def blockacc(self):
		idacc=self.id.text()
		key= self.Contra.text()
		msg= self.arg.Block_Unblockacc(idacc,key,"Block")
		QMessageBox.warning(self,"Resultado",msg)
class consultas(QWidget):
	"""docstring for consultas"""
	def __init__(self, arg,op):
		super(consultas, self).__init__(None)
		loadUi('consultas.ui',self)
		self.arg = arg
		if op==0:
			self.consultar.clicked.connect(self.consultar_clicked1)
		if op== 1:
			self.consultar.clicked.connect(self.consultar_clicked2)
	def consultar_clicked1(self):
		self.listWidget.clear()
		ident=self.id.text() 
		objconsult= self.arg.consul_client(ident)
		length=len(objconsult)
		if objconsult!= "Cliente no encontrado":
			for z in range(0,3):
				self.listWidget.addItem(objconsult[z])
			self.listWidget.addItem("Cuenas:")
			for x in range(4,length):
				#print(x)
				#print(objconsult[x])
				strtosend=  "Id: "+str(objconsult[x][1])+" Saldo: "+objconsult[x][2]+" Estado: "+objconsult[x][3]
				self.listWidget.addItem(strtosend)
		else:
			QMessageBox.warning(self,"Resultado",objconsult)
	
	def consultar_clicked2(self):
		self.listWidget.clear()
		ident=self.id.text() 
		objconsult= self.arg.consul_account(ident)
		if objconsult=="Cuenta no existe":
			QMessageBox.warning(self,"Resultado",objconsult)

		else:
			objconsult= self.arg.consul_account(ident).copy()	
			objconsult[1]= str(objconsult[1])
			objconsult.pop(0)
			for z in objconsult:
				self.listWidget.addItem(z)
class Getaccountdata(QWidget):
	"""docstring for Getaccountdata"""
	def __init__(self, arg, tipo):
		super(Getaccountdata, self).__init__(None)
		loadUi('accountdata2.ui',self)
		self.arg = arg
		if tipo==0:
			self.Ok.clicked.connect(self.Ok_clicked1)
		elif tipo==1:
			self.Ok.clicked.connect(self.Ok_clicked2)
		elif tipo==2:
			self.Ok.clicked.connect(self.Ok_clicked3)
	def Ok_clicked1(self):
		cc=self.cc.toPlainText()
		contra= self.contrasea.toPlainText()
		initmoney=self.money.toPlainText()
		msg= self.arg.create_accoun(cc,contra,initmoney)
		#print(self.arg.cuentasgen)
		QMessageBox.warning(self,"Resultado",msg)
	def Ok_clicked2(self):
		cc=self.cc.toPlainText()
		contra= self.contrasea.toPlainText()
		initmoney=self.money.toPlainText()
		msg= self.arg.Deposit(cc,initmoney)
		#print(self.arg.cuentasgen)
		QMessageBox.warning(self,"Resultado",msg)
	def Ok_clicked3(self):
		cc=self.cc.toPlainText()
		contra= self.contrasea.toPlainText()
		ammount=self.money.toPlainText()
		msg= self.arg.withdrawal(cc, ammount, contra)
		#print(self.arg.cuentasgen)
		QMessageBox.warning(self,"Resultado",msg)
class Getaccountdataac(QWidget):
	"""docstring for Getaccountdataac"""
	def __init__(self, arg):
		super(Getaccountdataac, self).__init__(None)
		loadUi('dataclient.ui',self)
		self.arg = arg
		self.Ok.clicked.connect(self.Ok_clicked)
	def Ok_clicked(self):
		Name1= self.Name.text()
		Lastname= self.Lastname.text()
		cc=self.cc.text()
		contra= self.contrasea.text()
		oldid=self.money.text()
		contra= self.contrasea.text()
		msg= self.arg.update_client(Name1,Lastname,cc,oldid,contra)
		#print(self.arg.cuentasgen)
		QMessageBox.warning(self,"Resultado",msg)
class Mostrarlist(QMainWindow):
	"""docstring for Mostrarlist"""
	def __init__(self, arg,op):
		super(Mostrarlist, self).__init__(None)
		loadUi('mostrar.ui',self)
		self.argv= arg
		if op==1:
			self.mostrar_clientes()
		if op==2:
			self.mostrar_acc()
			
	def mostrar_clientes(self):
		self.listWidget.clear()
		cont=0
		for z in self.argv.clientes:
			cont+=1
		for x in range(0,cont):
			item= self.argv.clientes[x].copy()
					##item[2]= str(item[2])
					#item[3]= str(item[3])
			str1= "Cliente: "+" Nombre: "+item[0]+" apellido: "+item[1]+" cc: "+item[2]
			self.listWidget.addItem(str1)
					##time.sleep(2)
	def mostrar_acc(self):
		cont=0
		cont3=0
		#print(self.bankfunk.cuentasgen)
		for z in self.argv.clientes:
			cont+=1
		for x in range(0,cont):
			item= self.argv.clientes[x].copy()
			str1= "Cliente: "+" Nombre: "+item[0]+" apellido: "+item[1]+" cc: "+item[2]
			cont2=0
			#for z in self.argv.clientes[x]:
			#	cont2+=1
			cont2=len(self.argv.clientes[x])
			for y in range(4,cont2):				
				item2= self.argv.clientes[x][y].copy()
				#item[2]= str(item[2])
				#item[3]= str(item[3])
				
				item2[1]=str(item2[1])
				#item2[2]=str(item2[2])
				str2= " id: "+item2[1]+" Saldo: "+ item2[2]+ " Estado: "+item2[3]+ "\n"
				
				item3= [str1, str2]
				str3= ' cuenta: '.join(item3)
				self.listWidget.addItem(str3)
			cont3+=1
class Getdataclient(QWidget):
			"""docstring for Getdataclient"""
			def __init__(self, arg):
				super(Getdataclient, self).__init__(None)
				loadUi('dataclient.ui',self)
				self.arg= arg	
				self.Ok.clicked.connect(self.Ok_clicked)
			def Ok_clicked(self):
				Name1= self.Name.text()
				Lastname= self.Lastname.text()
				cc=self.cc.text()
				contra= self.contrasea.text()
				initmoney=self.money.text()
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
		self.Modificardata.clicked.connect(self.Modificardata_clicked)
		self.deposit.clicked.connect(self.Deposit_clicked)
		self.withdrawal.clicked.connect(self.Withdrawal_clicked)
		self.Consulaccount.clicked.connect(self.consulaccount_clicked)
		self.Consultarclient.clicked.connect(self.Consultarclient_clicked)
		self.Block_Unblock.clicked.connect(self.Block_Unblock_clicked)

		self.thradq= QThread()
		self.thradq2= QThread()
		self.thradq3= QThread()
		self.thradq4= QThread()
		self.thradq5= QThread()
		self.thradq6= QThread()
		self.thradq7= QThread()
		self.thradq8= QThread()
		self.thradq9= QThread()
		self.thradq10= QThread()



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
	def Modificardata_clicked(self):
		self.thradq5.started.connect(self.modificardat)
		self.thradq5.start()
	def Deposit_clicked(self):
		self.thradq6.started.connect(self.depositmoney)
		self.thradq6.start()
	def Withdrawal_clicked(self):
		self.thradq7.started.connect(self.withdraw_money)
		self.thradq7.start()
	def consulaccount_clicked(self):
		self.thradq8.started.connect(self.consultacc)
		self.thradq8.start()
	def Consultarclient_clicked(self):
		self.thradq9.started.connect(self.consuclient)
		self.thradq9.start()
	def Block_Unblock_clicked(self):
		self.thradq10.started.connect(self.blocunblock)
		self.thradq10.start()


	def mostraracclist(self):
		self.mostrarlist=Mostrarlist(self.bankfunk,1)
		self.mostrarlist.setWindowTitle('Lista de clientes')
		
		##self.mostrarlist.listView.setViewMode(QtGui.QListView.I)
		self.mostrarlist.label.setText("Lista de clientes guardados")
		self.mostrarlist.show()
		self.thradq.quit()
	def mostrarcountlis(self):
		self.mostrarlist2=Mostrarlist(self.bankfunk,2)	
		self.mostrarlist2.setWindowTitle('Lista de cuentas')	
		
		##self.mostrarlist.listView.setViewMode(QtGui.QListView.I)
		self.mostrarlist2.label.setText("Lista de cuentas guardadas")
		self.mostrarlist2.show()
		self.thradq2.quit()
	def getclientdata(self):
		self.getclientdata1= Getdataclient(self.bankfunk)
		self.getclientdata1.setWindowTitle("Client data")
		self.getclientdata1.show()
		self.thradq3.quit()
	def getaccountdata(self):
		self.getaccountdata1= Getaccountdata(self.bankfunk,0)
		self.getaccountdata1.setWindowTitle("Account data")
		self.getaccountdata1.show()
		self.thradq4.quit()
	def modificardat(self):
		self.getaccountdata3= Getaccountdataac(self.bankfunk)
		self.getaccountdata3.setWindowTitle("Account data")
		self.getaccountdata3.label.setText("Insete nuevo nombre del cliente")
		self.getaccountdata3.label_2.setText("Insete nuevo apellido del cliente")
		self.getaccountdata3.label_3.setText("Insete nuevo número de identificación")
		self.getaccountdata3.label_4.setText("Insete número de identificación vieja")
		self.getaccountdata3.show()
		self.thradq5.quit()
	def depositmoney(self):
		self.Depositt= Getaccountdata(self.bankfunk,1)
		self.Depositt.setWindowTitle("Depositando")
		self.Depositt.label.setText("Inserte id de la cuenta")
		self.Depositt.label_2.setText(" ")
		self.Depositt.contrasea.setReadOnly(True)
		self.Depositt.show()
		self.thradq6.quit()
	def withdraw_money(self):
		self.withawint= Getaccountdata(self.bankfunk,2)
		self.withawint.setWindowTitle("Retirando")
		self.withawint.label.setText("Inserte id de la cuenta")
		self.withawint.label_3.setText("Inserte la cantidad de dinero a retirar")
		self.withawint.show()
		self.thradq7.quit()
	def consultacc(self):
		self.consulacc1= consultas(self.bankfunk,1)
		self.consulacc1.setWindowTitle("Consultando cuenta")
		self.consulacc1.label.setText("Inserte id de la cuenta")
		self.consulacc1.show()
		self.thradq8.quit()
	def consuclient(self):
		self.cosulclienint = consultas(self.bankfunk, 0)
		self.cosulclienint.setWindowTitle("Consultando cliente")
		self.cosulclienint.label.setText("Inserte ide del cliente")
		self.cosulclienint.show()
		self.thradq9.quit()
	def blocunblock(self):
		self.Blockunblock= Blockunint(self.bankfunk)
		self.Blockunblock.setWindowTitle("Cambiando estado de cuenta")
		self.Blockunblock.show()
		self.thradq10.quit()









class BankOfficer():
    def __init__(self):
    	self.path= '/tmp/myfifo'
    	self.pathdatapipe= '/tmp/myfifo2'
    	try:
    		os.unlink(self.path)
    		os.mkfifo(self.path)  		

    		pass
    	except:
    		os.mkfifo(self.path)
    	try:
    		os.unlink(self.pathdatapipe)
    		os.mkfifo(self.pathdatapipe)  
    	except:
    		os.mkfifo(self.pathdatapipe)

    	
    	
    	self.bufferSize=1000
    	##self.clientesolo= []
    	self.clientes= []
    	self.accnum=0
    	self.cuentasgen=[]
    	self.threadd= threading.Thread(target=self.thread_pipe)
    	self.threaddata= threading.Thread(target= self.Thread_datapipe)
    	self.threadd.start()
    	self.threaddata.start()
    	#self.threadd.join()
    	pass
    def Thread_datapipe(self):
    	while(1):
    		fifo=open(self.pathdatapipe,"rb")
    		str1=fifo.readline()
    		str2= str(str1)
    		newstr= "".join(str2)
    		newstr2= newstr.split(';')
    		#print(type(str2))
    		##print(newstr2)
    		#print(newstr2[1]+";"+newstr2[2])
    		fifo.close()
    		if newstr2[1]=="1":
    			dataout = self.consult_client_accounts(newstr2[2])
    		if newstr2[1]=="2":
    			#print(newstr2[3])
    			dataout= self.Deposit(newstr2[2],newstr2[3])
    		if newstr2[1]=="3":
    			dataout= self.withdrawal(newstr2[2],newstr2[3],newstr2[4])


    		fifo= open(self.pathdatapipe,"w")
    		st1out= dataout
    		fifo.write(st1out)
    		fifo.close()




    def thread_pipe(self):
    	self.create_client("Juan","Perez","100","er","1000")
    	self.create_client("Andrés","Lopez","200","er","2000")
    	self.create_accoun("100","er", "5000")
    	self.create_accoun("100","er", "10000")
    	cuentas=self.consult_client_accounts("100")
    	#print(cuentas)

    	while(1):
    		fifo=open(self.path, "rb")
    		#os.ftruncate(self.path,self.bufferSize)
    		#print(fifo)
    		str1=fifo.readline()
    		#print(type(str1))
    		#print(str1)
    		cont=0
    		str2= str(str1)
    		newstr= "".join(str2)
    		newstr2= newstr.split(';')
    		#print(type(str2))
    		#print(newstr2[1]+";"+newstr2[2])
    		fifo.close()
    		entro=0
    		for z in self.clientes:
    			if z[2]==newstr2[1] and z[3]== newstr2[2]:
    				msgg="Hola "+z[0]+ " "+z[1]
    				entro=1
    		if entro==0:
    			msgg= "Error al inicar sesion"
    			pass    		
    		fifo= open(self.path,"w")
    		st1out= msgg
    		fifo.write(st1out)
    		fifo.close()



    				

    		
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
    			
    def update_client(self,name1,name2,newid,oldid,contra):
    	self.cliente2= [name1,name2,newid,contra]
    	i=0
    	for z in self.clientes:
    		if z[2]==oldid and z[3]==contra:
    			
    			for compronewid in self.clientes:
    				
    				if compronewid[2]==newid and compronewid[2]!=oldid:
    					return "Id ya usado"
    			listalen= len(self.clientes[i])
    			for x in range(4,listalen):
    				self.cliente2.append(z[x])
    				#print(x)
    				#print(z[x])
    				#print(self.cliente2)
    			self.clientes[i]=self.cliente2
    			#print(self.clientes[i])
    			return "Exito"
    		else:    			
    			i+=1
    	return "Cliente no encontrado, o clave incorrecta"
    def consul_client(self, id):
    	for z in self.clientes:
    		if str(z[2])== id:
    			return z
    	return "Cliente no encontrado"
    def consult_client_accounts(self, id):
    	for z in self.clientes:
    		if str(z[2])== id:
    			leng= len(z)
    			datout= "Cuentas:\n"
    			for x in range(4,leng ):
    				#print(z)
    				datout= datout+" id: "+str(z[x][1])+" Saldo: "+z[x][2]+"\n"
    			return datout	

    def consul_account(self, id):
    	for z in self.cuentasgen:
    		if str(z[1])==id:
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
    	updatedaccount="0"
    	for accounn in self.cuentasgen:
    		if accounn[1]==id:
    			updatedaccount=accounn
    	cont=len(self.clientes)
    	
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
    		if z[0]==key and str(z[1])== idacc:
    			self.cuentasgen[cont][3]= state
    			self.update_account(idacc)
    			return "Estado de cuenta cambiado"
    		cont+=1




    	return "Cuenta no encontrada, o clave incorrecta"
    def Deposit(self, idacc,ammount):
    	cont=0
    	for z in self.cuentasgen:
    		##print(z[1])
    		##print(idacc)
    		if str(z[1])==idacc:

    			if z[3]=="Block":
    				return "cuenta bloqueada"
    			else:

    				amount2 = int(self.cuentasgen[cont][2])+int(ammount)
    				self.cuentasgen[cont][2]=str(amount2)
    				self.update_account(idacc)
    				return "Deposito realizado"
    		cont+=1

    	return "Error al realizar el deposito cuenta inexistente"
    def withdrawal(self, idacc, ammount, key):
    	cont=0
    	for z in self.cuentasgen:
    		if z[0]==key and str(z[1])==idacc:
    			if z[3]== "Block":
    				return "Cuenta bloqueada"
    			elif int(z[2])-int(ammount)<0:
    				return "No se tienen los fondos suficientes en la cuenta"
    			else:
    				ammount2=int(self.cuentasgen[cont][2])-int(ammount)
    				self.cuentasgen[cont][2]= str(ammount2)
    				self.update_account(z[1])
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
