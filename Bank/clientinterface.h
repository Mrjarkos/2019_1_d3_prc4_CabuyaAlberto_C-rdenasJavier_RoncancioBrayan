#ifndef CLIENTINTERFACE_H
#define CLIENTINTERFACE_H
#include "account.h"
#include <QtWidgets/QMainWindow>

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

#endif // CLIENTINTERFACE_H
