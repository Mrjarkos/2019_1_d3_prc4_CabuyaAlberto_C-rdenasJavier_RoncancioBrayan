/********************************************************************************
** Form generated from reading UI file 'bankofficial.ui'
**
** Created by: Qt User Interface Compiler version 5.12.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_BANKOFFICIAL_H
#define UI_BANKOFFICIAL_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_BankOfficial
{
public:
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QWidget *centralWidget;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *BankOfficial)
    {
        if (BankOfficial->objectName().isEmpty())
            BankOfficial->setObjectName(QString::fromUtf8("BankOfficial"));
        BankOfficial->resize(400, 300);
        menuBar = new QMenuBar(BankOfficial);
        menuBar->setObjectName(QString::fromUtf8("menuBar"));
        BankOfficial->setMenuBar(menuBar);
        mainToolBar = new QToolBar(BankOfficial);
        mainToolBar->setObjectName(QString::fromUtf8("mainToolBar"));
        BankOfficial->addToolBar(mainToolBar);
        centralWidget = new QWidget(BankOfficial);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        BankOfficial->setCentralWidget(centralWidget);
        statusBar = new QStatusBar(BankOfficial);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        BankOfficial->setStatusBar(statusBar);

        retranslateUi(BankOfficial);

        QMetaObject::connectSlotsByName(BankOfficial);
    } // setupUi

    void retranslateUi(QMainWindow *BankOfficial)
    {
        BankOfficial->setWindowTitle(QApplication::translate("BankOfficial", "BankOfficial", nullptr));
    } // retranslateUi

};

namespace Ui {
    class BankOfficial: public Ui_BankOfficial {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_BANKOFFICIAL_H
