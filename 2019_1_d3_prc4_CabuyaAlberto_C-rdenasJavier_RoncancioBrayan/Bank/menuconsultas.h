#ifndef MENUCONSULTAS_H
#define MENUCONSULTAS_H

#include <QWidget>
#include <QtWidgets/QtWidgets>
#include "client.h"
namespace Ui {
  class menuconsultas;
}

class menuconsultas : public QWidget
{
  Q_OBJECT

public:
  explicit menuconsultas(QWidget *parent = nullptr);
  void changetextlb1(char* msg);
  void changetextlb2(char* msg);
  Client* clienteobj;

  ~menuconsultas();

//private:
  Ui::menuconsultas *ui;
private slots:
  void on_pushButton_clicked();
  void on_pushButton_2_clicked();
  void on_pushButton_3_clicked();
};

#endif // MENUCONSULTAS_H
