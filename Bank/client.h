#ifndef CLIENT_H
#define CLIENT_H
#include "account.h"
#define pipename "/tmp/myfifo"
#define msjzise 1000
class Client
{
public:
    Client(char* , char*);
    char msg[msjzise];
    int fd;
};

#endif
