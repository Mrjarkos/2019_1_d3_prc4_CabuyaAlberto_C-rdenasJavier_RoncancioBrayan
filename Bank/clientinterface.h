#ifndef CLIENTINTERFACE_H
#define CLIENTINTERFACE_H

#include <QtWidgets/QMainWindow>
#include<QtWidgets/QMainWindow>
#include <QList>
#include <QStringList>
#include <QString>
#include <QtWidgets/QWidget>
#include <QSharedPointer>
#include <QHash>
#include <QtWidgets/QDialog>
#include<QtDebug>
#include "client.h"
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
