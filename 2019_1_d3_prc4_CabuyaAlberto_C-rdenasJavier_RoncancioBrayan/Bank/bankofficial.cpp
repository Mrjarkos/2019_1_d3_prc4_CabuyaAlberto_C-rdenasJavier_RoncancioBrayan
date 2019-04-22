#include "bankofficial.h"
#include "ui_bankofficial.h"

BankOfficial::BankOfficial(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::BankOfficial)
{
    ui->setupUi(this);
}

BankOfficial::~BankOfficial()
{
    delete ui;
}
