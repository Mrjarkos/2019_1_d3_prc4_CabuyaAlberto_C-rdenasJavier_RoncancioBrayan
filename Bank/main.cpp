#include <QApplication>
#include "clientinterface.h"
int main(int argc, char *argv[])
{
  QApplication a(argc, argv);
  ClientInterface* interfaz= new ClientInterface();
  interfaz->show();
  return a.exec();
}
