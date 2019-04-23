/********************************************************************************
** Form generated from reading UI file 'menuconsultas.ui'
**
** Created by: Qt User Interface Compiler version 5.12.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MENUCONSULTAS_H
#define UI_MENUCONSULTAS_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_menuconsultas
{
public:
    QPushButton *pushButton;
    QPushButton *pushButton_2;
    QPushButton *pushButton_3;
    QLabel *label;
    QLabel *label_2;
    QLineEdit *lineEdit;
    QLineEdit *lineEdit_2;
    QLineEdit *lineEdit_3;
    QLineEdit *lineEdit_4;
    QLabel *label_3;
    QLabel *label_4;
    QLabel *label_5;
    QLabel *label_6;

    void setupUi(QWidget *menuconsultas)
    {
        if (menuconsultas->objectName().isEmpty())
            menuconsultas->setObjectName(QString::fromUtf8("menuconsultas"));
        menuconsultas->resize(646, 428);
        pushButton = new QPushButton(menuconsultas);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));
        pushButton->setGeometry(QRect(20, 130, 171, 25));
        pushButton_2 = new QPushButton(menuconsultas);
        pushButton_2->setObjectName(QString::fromUtf8("pushButton_2"));
        pushButton_2->setGeometry(QRect(20, 200, 171, 25));
        pushButton_3 = new QPushButton(menuconsultas);
        pushButton_3->setObjectName(QString::fromUtf8("pushButton_3"));
        pushButton_3->setGeometry(QRect(20, 280, 171, 25));
        label = new QLabel(menuconsultas);
        label->setObjectName(QString::fromUtf8("label"));
        label->setGeometry(QRect(50, 40, 271, 17));
        label_2 = new QLabel(menuconsultas);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setGeometry(QRect(50, 80, 341, 17));
        lineEdit = new QLineEdit(menuconsultas);
        lineEdit->setObjectName(QString::fromUtf8("lineEdit"));
        lineEdit->setGeometry(QRect(210, 200, 131, 25));
        lineEdit_2 = new QLineEdit(menuconsultas);
        lineEdit_2->setObjectName(QString::fromUtf8("lineEdit_2"));
        lineEdit_2->setGeometry(QRect(360, 200, 241, 25));
        lineEdit_3 = new QLineEdit(menuconsultas);
        lineEdit_3->setObjectName(QString::fromUtf8("lineEdit_3"));
        lineEdit_3->setGeometry(QRect(210, 280, 131, 25));
        lineEdit_4 = new QLineEdit(menuconsultas);
        lineEdit_4->setObjectName(QString::fromUtf8("lineEdit_4"));
        lineEdit_4->setGeometry(QRect(360, 280, 241, 25));
        label_3 = new QLabel(menuconsultas);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setGeometry(QRect(210, 180, 141, 17));
        label_4 = new QLabel(menuconsultas);
        label_4->setObjectName(QString::fromUtf8("label_4"));
        label_4->setGeometry(QRect(360, 180, 151, 17));
        label_5 = new QLabel(menuconsultas);
        label_5->setObjectName(QString::fromUtf8("label_5"));
        label_5->setGeometry(QRect(210, 260, 141, 17));
        label_6 = new QLabel(menuconsultas);
        label_6->setObjectName(QString::fromUtf8("label_6"));
        label_6->setGeometry(QRect(360, 260, 151, 17));

        retranslateUi(menuconsultas);

        QMetaObject::connectSlotsByName(menuconsultas);
    } // setupUi

    void retranslateUi(QWidget *menuconsultas)
    {
        menuconsultas->setWindowTitle(QApplication::translate("menuconsultas", "Form", nullptr));
        pushButton->setText(QApplication::translate("menuconsultas", "Consulta de saldo", nullptr));
        pushButton_2->setText(QApplication::translate("menuconsultas", "Depositar en  cuenta", nullptr));
        pushButton_3->setText(QApplication::translate("menuconsultas", "Retirar dienro", nullptr));
        label->setText(QApplication::translate("menuconsultas", "TextLabel", nullptr));
        label_2->setText(QApplication::translate("menuconsultas", "TextLabel", nullptr));
        label_3->setText(QApplication::translate("menuconsultas", "N\303\272mero de cuenta", nullptr));
        label_4->setText(QApplication::translate("menuconsultas", "Valor a depositar", nullptr));
        label_5->setText(QApplication::translate("menuconsultas", "N\303\272mero de cuenta", nullptr));
        label_6->setText(QApplication::translate("menuconsultas", "Valor a retirar", nullptr));
    } // retranslateUi

};

namespace Ui {
    class menuconsultas: public Ui_menuconsultas {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MENUCONSULTAS_H
