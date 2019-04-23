#ifndef CLIENT_H
#define CLIENT_H
#include "account.h"
#include <algorithm>
#include <iterator>
#include <vector>
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
   int confirm=0;
    char msg[msjzise];
    int fd;
};

#endif
