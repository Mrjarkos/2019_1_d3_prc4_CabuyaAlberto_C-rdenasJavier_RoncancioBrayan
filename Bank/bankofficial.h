#ifndef BANKOFFICIAL_H
#define BANKOFFICIAL_H

#include <QMainWindow>

namespace Ui {
class BankOfficial;
}

class BankOfficial : public QMainWindow
{
    Q_OBJECT

public:
    explicit BankOfficial(QWidget *parent = 0);
    ~BankOfficial();

private:
    Ui::BankOfficial *ui;
};

#endif // BANKOFFICIAL_H
