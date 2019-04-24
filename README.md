# Desarrollo de un programa en C++ y Phyton para gestión de operaciones de un banco mediante implementación de interfaces gráficas con Qt

Presentado por:

Alberto Cabuya\
Javier Cárdenas\
Brayan Roncancio\

# Resumen

En el siguiente informe se enseñara de forma detallada la elaboración de una interfaz gráfica realizada para el usuario de un banco y para el funcionario del banco; para la elaboración de dichas interfazes se utilizara el programa Qt empleando dos lenguajes de programación; Phyton y c++. Para la elaboración de la interfaz de usuario se utilizo c++ y para la interfaz del operario Phyton; con el fin de profundizar conocimientos en las dos areas; estas interfaces iran conectadas por medio de tuberias al codigo fuente escrito en c++, el cual fue realizado días anteriores, cuando se creo un banco en el cúal se podia realizar depositos, retiros, crear clientes, cuentas, verificar cuentas, bloquearlas, desbloquearlas, etc...

# Introducción

En la actualidad, los codigos de programación cuentan con interfaces gráficas que facilitan la comprensión de un programa a un usuario que tiene o no idea del tema. Hace algunos años, cuando la programación no estaba en auge, las interfaces de programación no se encontraban en ventanas de forma organizada y bonita para el ojo humano; sino que se encontraba, en forma de texto plano, complicando el uso de programas. Para este caso en especifico, se dese mejorar la presentación de un banco realizado anteriormente, haciendo uso de una aplicación llamada Qt. Esto para facilitar la comprensión y estructuración del programa que lleva a cabo dicha labor. 

# Objetivos

## Objetivo General

* Implementar una interfaz gráfica que facilite la comprensión y uso de un programa que simula el funcionamiento de un banco

## Objetivos Específicos

* Implementar una interfaz para usuario en Qt haciendo uso del lenguaje c++ 
* Implementar una interfaz para funcionario de un banco en Qt haciendo uso del lenguaje Phyton
* Comunicar dos tipos de lenguajes diferenetes por medio de la implementación de tuberias

# Planteamiento del problema
Se requiere diseñar un sistema que maneje todos los procesos que se pueden llevar en un banco, es decir; transacciones, habilitar o deshabilitar cuentas, crear o borrar cuentas, crear usuarios. Para ello se debe emplear una interfaz gráfica que facilite la manipulación del sistema que llevara a cabo dicha labor; se necesita emplear dos lenguajes de programación c++ y Phyton. Los dos lenguajes deben interactuar entre sí, el transporte de información sera llevada a cabo por medio de hilos y se deben atender los problemas que se puedan presentar al ingrsar datos o valores numericos; es decir, en la elaboración de cuentas y en las transacciones.

# Desarrollo

## Estructuración del Programa

Para el desarrollo del programa se dividió el programa en 2 procesos diferentes el cual se decidieron comunicar mediante tuberías, más adelante se especificará cada uno de ellos.

### Programa Interfaz Cliente C++
Para el desarrollo del programa del banco que atiende al cliente, se identificaron 2 clases fundamentales en funcionamiento: cliente y la clase de la interfaz gráfica, dichar clases de relacionan a continuación:

* `Client`:

En la clase cliente es donde se define el cliente: donde se almacena la información a mostrar del cliente y se realizan las operaciones del cliente en la interfaz del cliente. No se vio la necesidad de implementar mas clases debido a que toda la informacion necesaria para realizar las operaciones en la interfaz del cliente se almacena y procesa en el servidor, el cliente simplemente solicita la informacion y la muestra.

``` c++
#ifndef CLIENT_H
#define CLIENT_H
#include "account.h"
#include <algorithm>
#include <iterator>
#include <vector>
#define pipename "/tmp/myfifo"
#define pipenamedata "/tmp/myfifo2"
#define msjzise 1000

  class Client
  {
  public:
     char* Cc;
     char* Contra;
     char* idaccountconsulta;
     char* moneyammount;
     int confirm=0;
     char msg[msjzise];
     int fd;
     Client(char* , char*);
     void verifyClient();
     void consulclient(int);
  };
```

* `Clientinterface`:

Para el diseño de la interfaz grafica se desarrolló gracias a la herramienta de Qt 5.12.3, el cual es un entorno de desarrollo de software para ubuntu y otros sistemas operativos bastante versatil e intuitivo.

El `programa` cuando inicia muestra la siguiente gui, la cual pide usuario y contraseña para poder proceder con la transacción que quiera realizar, la cual muestra la siguiente gui:

<img src="https://www.dropbox.com/s/6ggp29b48orajmj/intrfaz%20usr2.png?dl=0" />

Una vez validado los datos del usuario, se muestra una nueva ventana, en donde el cliente puede interactuar con el servidor mediante la siguiente interfaz:

<img src="https://www.dropbox.com/s/0nypkhgrtv83c0t/interfazusuario.png?dl=0" />

En esta ventana el cliente podrá realizar operaciones de consulta de saldo, de cuentas o depositar o retirar dinero. Si desea realizar otras operaciones como bloquear una cuenta, deberá realizarlo exclusivamente en el banco.

La definición de la clase `Clientinterface` se muestra a continuacion:

``` c++
#ifndef CLIENTINTERFACE_H
#define CLIENTINTERFACE_H

#include <QtWidgets/QMainWindow>
#include<QtWidgets/QMainWindow>
#include <QList>
#include <QStringList>
#include <QString>
#include <QtWidgets/QWidget>
#include <QtWidgets/QTabWidget>
#include <QSharedPointer>
#include <QHash>
#include <QtWidgets/QDialog>
#include<QtDebug>
#include "client.h"
#include "menuconsultas.h"
namespace Ui {
class ClientInterface;
}

class ClientInterface : public QMainWindow
{
    Q_OBJECT

public:
    explicit ClientInterface(QWidget *parent = 0);
    ~ClientInterface();

private slots:
    void on_pushButton_clicked();
    
private:
    Ui::ClientInterface *ui;
};

#endif  //CLIENTINTERFACE_H
```

### Programa Interfaz Oficinista Phyton


<img src="https://www.dropbox.com/s/7nn9qombz421moj/interface_banquero.png?dl=0" />


### Servidor (Phyton)

El servidor del banco se encarga de atender las operaciones requeridas por las otras dos interfaces. El servidor cuenta con la clase `BankOfficer`, el programa no es estrictamente orientado a objetos, debido a que para los clientes y para las cuentas se implementaron `listas` en vez de clases, a continuación se muestra una porción de código que crea un cliente, en él se ilustra mejor el tratamiento dado a las cuentas y a los clientes. El servidor como tal no tiene implementado ninguna interfaz gráfica, ya que no es necesario. Este recibe una cadena de caracteres mediante pipes con nombre y atenderá de acuerdo al primer caracter leido.

* `Client`:

Los clientes tienen una estructura similar a la clase `Client.cpp` implementada en el programa de interfaz gráfica del cliente (nombre, apellido, id, cuentas, etc), sin embargo divergen en la interpretación, mientras que en C++ era una clase, en este programa se trataron los clientes como listas, los cuales permitieron una mayor versatilidad en la gestión de estos, sin embargo se pierde el concepto, la estructuración y las ventajas que ofrece programar programación orientada a objetos.

``` phyton
    def create_client(self,name1,name2,id,contra,initialvalue):
    	try:
    		int(initialvalue)
    	except:
    		return "Valor a insertar no valido"
    	for z in self.clientes:
    		if z[2]== id:
    			return "Cliente ya existe"	
    	self.cliente= [name1,name2,id,contra] 
## Se hace este debido a que si no hay cuentas no se entra al ciclo for in
    	self.cuentas= [contra,self.accnum, initialvalue,"Unblock"]
    	self.accnum+=1
    	##self.clientesolo.append(self.cliente)
    	self.cliente.append(self.cuentas)
    	self.clientes.append(self.cliente)
    	self.cuentasgen.append(self.cuentas)
    	return "Cliente creado"
```

* `Cuentas`:

Las cuentas recibieron un tratamiento similar a los clientes (se trataron como listas) pero anidados a estos, es decir que una cuenta no puede existir mientras no exista un cliente, esto se puede evidenciar en las excepciones implementadas en el siguiente código:

``` phyton
  def create_accoun(self, id, key, initialvalue):
    	try:
    		int(initialvalue)
    	except:
    		return "Valor a insertar no valido"
    	for z in self.clientes:
    		if z[2]== id and z[3]== key:
    			newaccount= [key,self.accnum,initialvalue,"Unblock"]
    			z.append(newaccount)
    			self.cuentasgen.append(newaccount)
    			self.accnum+=1
    			return "Cuenta creada"
    			pass
    	return "Cliente no encontrado, no se pudo crear la cuenta"
```
* Métodos:

`Block_unblock`:

``` phyton
    def Block_Unblockacc(self,idacc,key,state):
    	cont=0
    	for z in self.cuentasgen:
    		if z[0]==key and str(z[1])== idacc:
    			self.cuentasgen[cont][3]= state
    			self.update_account(idacc)
    			return "Estado de cuenta cambiado"
    		cont+=1
    	return "Cuenta no encontrada, o clave incorrecta"
```

`Deposit`:

``` phyton
    def Deposit(self, idacc,ammount):
    	try:
    		int(initialvalue)
    	except:
    		return "Valor a insertar no valido"
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
```

`Withdrawal`:

```phyton
    def withdrawal(self, idacc, ammount, key):
    	try:
    		int(ammount)
    	except:
    		return "Valor a insertar no valido"
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
```

`Transfer_money`:

``` phyton
    def transfer_money(self, idacc1, key, idacc2, ammount):
    	try:
    		int(ammount)
    	except:
    		return "Valor a insertar no valido"
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


```

### Comunicación

Para la comunicación entre los dos programas se implementaron tuberías con nombre, a continuación se muestran los dos métodos de atención:

* Login del cliente:

Cuando el servidor iniciaba, creaba un hilo que estuviera pendiente de las suscripciones del cliente (sea el cliente del banco o banquero), el cual se abría una tubería solo para especificación del path en donde se creaba la tubería para la atención del servidor.

``` phyton 
    def thread_pipe(self):

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

```


* Atención del servicio:

Fue necesario implementar hilos para atender a cada cliente, debido a que se debía estar pendiente de la tubería y realizar operaciones que cada cliente requiera. Cada hilo creaba y atendía cada tubería, posteriormente esperaba a que hubiese una cadena de caracteres en la tubería, se leía el primer caracter y se atendía de acuerdo al caracter recibido.

``` phyton

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
```

# Conclusiones

* El lenguaje de programación Phyton tiene una nomenclatura facil para el usuario que programa, debido a ello facilita la comprensión y elaboración de un programa, por ejemplo, el auto asignamiento del tipo de variable, evita que se presenten errores en la utilización de las variables; además se pudo observar, que el lenguaje presenta sobrecargas en su método self. Pero se pudo apreciar que al ser un lenguaje interpretado necesita mayor tiempo para la ejecución de un programa en comparación a lenguajes compilados o ensamblados. 

* Para poder comunicar dos programas escritos en diferentes lenguajes de programación, en phyton es muy facil usando pipes o memoria compartida; para este caso en especifico se usaron pipes o tuberias debido a que la memoria compartida no esta disponible para las versiones que se usaron de phyton. 

* Desde un punto de vista estructurado el programa que se realizo, se puede observar que el programa no presenta una programación orientada a objetos, por lo cual, se ve cierto nivel de complejidad para la comprensión del codigo; al aplicar la programación orientada a objetos se hubiese aumentado la legitimidad de dicho código y se hubiesen podido aprovechar propiedades como polimorfismo, encapsulamiento, herencia. 


