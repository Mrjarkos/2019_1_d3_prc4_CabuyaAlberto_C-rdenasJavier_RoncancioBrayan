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

<img src="URL_DE_LA_IMAGEN" />

Una vez validado los datos del usuario, se muestra una nueva ventana, en donde el cliente puede interactuar con el servidor mediante la siguiente interfaz:

<img src="URL_DE_LA_IMAGEN" />

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

### Programa Interfaz Oficinista Phyton - Servidor


### Comunicación

# Conclusiones
