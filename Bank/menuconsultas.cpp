#include "menuconsultas.h"
#include "ui_menuconsultas.h"
#include "client.h"

menuconsultas::menuconsultas(QWidget *parent) :
  QWidget(parent),
  ui(new Ui::menuconsultas)
{
  ui->setupUi(this);
}
void menuconsultas::changetextlb1(char* msg){
  ui->label->setText(msg);
}
void menuconsultas::changetextlb2(char* msg){
  ui->label_2->setText(msg);
}
menuconsultas::~menuconsultas()
{
  delete ui;
}

void menuconsultas::on_pushButton_clicked()
{
    clienteobj->consulclient(1);

    QMessageBox::information(this,tr("Info"),tr(clienteobj->msg));

}

void menuconsultas::on_pushButton_2_clicked()
{
     char * idacctmp= new char[20];
     QString text= ui->lineEdit->text();
      string idaccount1= text.toStdString();
      strcpy(idacctmp,idaccount1.c_str());
      clienteobj->idaccount=idacctmp;
      //qDebug()<<"id"<<clienteobj->idaccount;
      char * moneytmp= new char[20];
      QString text2= ui->lineEdit_2->text();
     string ammount= text2.toStdString();
     strcpy(moneytmp,ammount.c_str());
     clienteobj->moneyammount= moneytmp;
      //qDebug()<<"id"<<clienteobj->idaccount;

    clienteobj->consulclient(2);
    QMessageBox::information(this,tr("Info"),tr(clienteobj->msg));
}

void menuconsultas::on_pushButton_3_clicked()
{
  char * idacctmp= new char[20];
  QString text= ui->lineEdit_3->text();
   string idaccount1= text.toStdString();
   strcpy(idacctmp,idaccount1.c_str());
   clienteobj->idaccount=idacctmp;
   //qDebug()<<"id"<<clienteobj->idaccount;
   char * moneytmp= new char[20];
   QString text2= ui->lineEdit_4->text();
  string ammount= text2.toStdString();
  strcpy(moneytmp,ammount.c_str());
  clienteobj->moneyammount= moneytmp;
   //qDebug()<<"id"<<clienteobj->idaccount;
  clienteobj->consulclient(3);
  QMessageBox::information(this,tr("Info"),tr(clienteobj->msg));
}
