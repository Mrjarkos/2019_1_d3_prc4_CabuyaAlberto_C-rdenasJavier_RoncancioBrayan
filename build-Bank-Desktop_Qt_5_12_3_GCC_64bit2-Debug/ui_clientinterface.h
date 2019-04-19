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
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_ClientInterface
{
public:
    QWidget *centralWidget;
    QTextEdit *textEdit;
    QTextEdit *textEdit_2;
    QPushButton *pushButton;
    QLabel *label;
    QLabel *label_2;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *ClientInterface)
    {
        if (ClientInterface->objectName().isEmpty())
            ClientInterface->setObjectName(QString::fromUtf8("ClientInterface"));
        ClientInterface->resize(400, 300);
        centralWidget = new QWidget(ClientInterface);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        textEdit = new QTextEdit(centralWidget);
        textEdit->setObjectName(QString::fromUtf8("textEdit"));
        textEdit->setGeometry(QRect(60, 50, 271, 31));
        textEdit_2 = new QTextEdit(centralWidget);
        textEdit_2->setObjectName(QString::fromUtf8("textEdit_2"));
        textEdit_2->setGeometry(QRect(60, 120, 271, 31));
        pushButton = new QPushButton(centralWidget);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));
        pushButton->setGeometry(QRect(150, 180, 89, 25));
        label = new QLabel(centralWidget);
        label->setObjectName(QString::fromUtf8("label"));
        label->setGeometry(QRect(70, 100, 171, 17));
        label_2 = new QLabel(centralWidget);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setGeometry(QRect(70, 30, 201, 17));
        ClientInterface->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(ClientInterface);
        menuBar->setObjectName(QString::fromUtf8("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 400, 22));
        ClientInterface->setMenuBar(menuBar);
        mainToolBar = new QToolBar(ClientInterface);
        mainToolBar->setObjectName(QString::fromUtf8("mainToolBar"));
        ClientInterface->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(ClientInterface);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        ClientInterface->setStatusBar(statusBar);

        retranslateUi(ClientInterface);

        QMetaObject::connectSlotsByName(ClientInterface);
    } // setupUi

    void retranslateUi(QMainWindow *ClientInterface)
    {
        ClientInterface->setWindowTitle(QApplication::translate("ClientInterface", "ClientInterface", nullptr));
        pushButton->setText(QApplication::translate("ClientInterface", "Comprovar", nullptr));
        label->setText(QApplication::translate("ClientInterface", "Inserte su contrase\303\261a", nullptr));
        label_2->setText(QApplication::translate("ClientInterface", "Inserte su c\303\251dula", nullptr));
    } // retranslateUi

};

namespace Ui {
    class ClientInterface: public Ui_ClientInterface {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_CLIENTINTERFACE_H
