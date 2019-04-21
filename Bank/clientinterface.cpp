#include "clientinterface.h"
#include "ui_clientinterface.h"
#include <qmessagebox.h>
ClientInterface::ClientInterface(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::ClientInterface)
{
    ui->setupUi(this);
}

ClientInterface::~ClientInterface()
{
    delete ui;
}

void ClientInterface::on_pushButton_clicked()
{
    char* cc= new char[100];
    QString str= ui->textEdit->toPlainText();
    string kks= str.toStdString();
    strcpy(cc,kks.c_str());
    char* contra= new char[100];
    QString str2= ui->textEdit_2->toPlainText();
    kks= str2.toStdString();
    strcpy(contra,kks.c_str());
    //qDebug()<<"kks";
    Client* cliente= new Client(cc, contra);
    cliente->verifyClient();

    if(cliente->fd<0){
        QMessageBox::critical(this,tr("Error"),tr(cliente->msg));
      }
    else {
        QMessageBox::information(this,tr("Info"),tr(cliente->msg));
        if(cliente->msg !="Error al inicar sesion"){
          menuconsultas* menu = new menuconsultas();
          menu->clienteobj= cliente;
          menu->changetextlb1(cliente->msg);
          menu->changetextlb2(cc);
          menu->show();
        }

      }
}
