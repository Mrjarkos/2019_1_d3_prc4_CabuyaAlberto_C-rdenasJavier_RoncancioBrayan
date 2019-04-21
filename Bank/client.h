#ifndef CLIENT_H
#define CLIENT_H
#include "account.h"
#define pipename "/tmp/myfifo"
#define pipenamedata "/tmp/myfifo2"
#define msjzise 1000
class Client
{
public:
    Client(char* , char*);
   void verifyClient();
   void consulclient(int);
   char* Cc;
   char* Contra;
   char * idaccount;
   char* moneyammount;
    char msg[msjzise];
    int fd;
};

#endif
