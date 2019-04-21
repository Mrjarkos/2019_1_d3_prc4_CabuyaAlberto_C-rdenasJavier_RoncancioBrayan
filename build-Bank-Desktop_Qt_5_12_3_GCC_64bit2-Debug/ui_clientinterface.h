/********************************************************************************
** Form generated from reading UI file 'clientinterface.ui'
**
** Created by: Qt User Interface Compiler version 5.12.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_CLIENTINTERFACE_H
#define UI_CLIENTINTERFACE_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_ClientInterface
{
public:
    QWidget *centralWidget;
    QLabel *label_2;
    QTextEdit *textEdit;
    QTextEdit *textEdit_2;
    QPushButton *pushButton;
    QLabel *label;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;

    void setupUi(QMainWindow *ClientInterface)
    {
        if (ClientInterface->objectName().isEmpty())
            ClientInterface->setObjectName(QString::fromUtf8("ClientInterface"));
        ClientInterface->resize(324, 248);
        centralWidget = new QWidget(ClientInterface);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        centralWidget->setAcceptDrops(true);
        label_2 = new QLabel(centralWidget);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setGeometry(QRect(20, 10, 201, 17));
        textEdit = new QTextEdit(centralWidget);
        textEdit->setObjectName(QString::fromUtf8("textEdit"));
        textEdit->setGeometry(QRect(20, 40, 271, 31));
        textEdit_2 = new QTextEdit(centralWidget);
        textEdit_2->setObjectName(QString::fromUtf8("textEdit_2"));
        textEdit_2->setGeometry(QRect(20, 100, 271, 31));
        pushButton = new QPushButton(centralWidget);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));
        pushButton->setGeometry(QRect(60, 150, 89, 25));
        label = new QLabel(centralWidget);
        label->setObjectName(QString::fromUtf8("label"));
        label->setGeometry(QRect(20, 80, 171, 17));
        ClientInterface->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(ClientInterface);
        menuBar->setObjectName(QString::fromUtf8("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 324, 22));
        ClientInterface->setMenuBar(menuBar);
        mainToolBar = new QToolBar(ClientInterface);
        mainToolBar->setObjectName(QString::fromUtf8("mainToolBar"));
        ClientInterface->addToolBar(Qt::TopToolBarArea, mainToolBar);

        retranslateUi(ClientInterface);

        QMetaObject::connectSlotsByName(ClientInterface);
    } // setupUi

    void retranslateUi(QMainWindow *ClientInterface)
    {
        ClientInterface->setWindowTitle(QApplication::translate("ClientInterface", "ClientInterface", nullptr));
        label_2->setText(QApplication::translate("ClientInterface", "Inserte su c\303\251dula", nullptr));
        pushButton->setText(QApplication::translate("ClientInterface", "Comprobar", nullptr));
        label->setText(QApplication::translate("ClientInterface", "Inserte su contrase\303\261a", nullptr));
    } // retranslateUi

};

namespace Ui {
    class ClientInterface: public Ui_ClientInterface {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_CLIENTINTERFACE_H
