#include "client.h"
#include <QDebug>
Client::Client(char* cc,char* contra )
{
  fd= open(pipename, O_RDWR);
  if (fd<0){
      close(fd);
      strcpy(msg,"No se pudo abrir el pipe, intente de nuevo");
      mkfifo(pipename,0666);
    }
  else{

      char* send[2];
      send[0]=cc;
      send[1]=contra;
      char* rec[2];
      write(fd,send,strlen(cc)+strlen(contra)+sizeof (send));
      sleep(1);
     //qDebug()<<"cc:"<<send[0]<<"cont:"<<send[1];

      read(fd, rec,msjzise);

     //qDebug()<<"cc:"<<rec[0]<<"cont:"<<rec[1];
      sleep(1);
      close(fd);
  }
}
