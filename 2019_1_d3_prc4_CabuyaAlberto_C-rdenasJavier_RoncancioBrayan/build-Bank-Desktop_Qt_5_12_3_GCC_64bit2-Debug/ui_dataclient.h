/********************************************************************************
** Form generated from reading UI file 'dataclient.ui'
**
** Created by: Qt User Interface Compiler version 5.12.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_DATACLIENT_H
#define UI_DATACLIENT_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QLabel>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Form
{
public:
    QLabel *label;
    QTextEdit *Name;
    QLabel *label_2;
    QTextEdit *Lastname;
    QLabel *label_3;
    QTextEdit *cc;
    QLabel *label_4;
    QTextEdit *money;
    QPushButton *Ok;
    QTextEdit *contrasea;
    QLabel *label_5;

    void setupUi(QWidget *Form)
    {
        if (Form->objectName().isEmpty())
            Form->setObjectName(QString::fromUtf8("Form"));
        Form->resize(400, 387);
        label = new QLabel(Form);
        label->setObjectName(QString::fromUtf8("label"));
        label->setGeometry(QRect(30, 10, 211, 17));
        Name = new QTextEdit(Form);
        Name->setObjectName(QString::fromUtf8("Name"));
        Name->setGeometry(QRect(30, 40, 351, 31));
        label_2 = new QLabel(Form);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setGeometry(QRect(30, 80, 191, 17));
        Lastname = new QTextEdit(Form);
        Lastname->setObjectName(QString::fromUtf8("Lastname"));
        Lastname->setGeometry(QRect(30, 100, 351, 31));
        label_3 = new QLabel(Form);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setGeometry(QRect(30, 140, 261, 17));
        cc = new QTextEdit(Form);
        cc->setObjectName(QString::fromUtf8("cc"));
        cc->setGeometry(QRect(30, 160, 351, 31));
        label_4 = new QLabel(Form);
        label_4->setObjectName(QString::fromUtf8("label_4"));
        label_4->setGeometry(QRect(30, 200, 341, 17));
        money = new QTextEdit(Form);
        money->setObjectName(QString::fromUtf8("money"));
        money->setGeometry(QRect(30, 220, 351, 31));
        Ok = new QPushButton(Form);
        Ok->setObjectName(QString::fromUtf8("Ok"));
        Ok->setGeometry(QRect(150, 330, 89, 25));
        contrasea = new QTextEdit(Form);
        contrasea->setObjectName(QString::fromUtf8("contrasea"));
        contrasea->setGeometry(QRect(30, 280, 351, 31));
        label_5 = new QLabel(Form);
        label_5->setObjectName(QString::fromUtf8("label_5"));
        label_5->setGeometry(QRect(30, 260, 301, 17));

        retranslateUi(Form);

        QMetaObject::connectSlotsByName(Form);
    } // setupUi

    void retranslateUi(QWidget *Form)
    {
        Form->setWindowTitle(QApplication::translate("Form", "Form", nullptr));
        label->setText(QApplication::translate("Form", "Inserte nombre del cliente", nullptr));
        label_2->setText(QApplication::translate("Form", "Inserte apellido", nullptr));
        label_3->setText(QApplication::translate("Form", "Inserte numero de identificaci\303\263n", nullptr));
        label_4->setText(QApplication::translate("Form", "Inserte cantidad de dinero inicial", nullptr));
        Ok->setText(QApplication::translate("Form", "ok", nullptr));
        label_5->setText(QApplication::translate("Form", "Inserte la contrase\303\261a", nullptr));
    } // retranslateUi

};

namespace Ui {
    class Form: public Ui_Form {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_DATACLIENT_H
