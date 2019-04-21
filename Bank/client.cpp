#include "client.h"
#include <QDebug>
Client::Client(char* cc,char* contra )
{
  fd= open(pipename, O_WRONLY);
  if (fd<0){
      close(fd);
      strcpy(msg,"No se pudo abrir el pipe, intente de nuevo");
    }
  else{

      string send[2];
      send[0]=cc;
      send[1]=contra;
      string datout= send[0]+";"+send[1];
     // char* rec[2];
      write(fd,&datout,sizeof(datout));
      sleep(1);
     //qDebug()<<"cc:"<<send[0]<<"cont:"<<send[1];

      //read(fd, rec,msjzise);
      //printf("%s", rec[0]);
     //qDebug()<<"cc:"<<rec[0]<<"cont:"<<rec[1];
      close(fd);
      fd= open(pipename, O_RDONLY);
      if (fd<0){
          close(fd);
           strcpy(msg,"No se pudo abrir el pipe, intente de nuevo");
        }
      else{
          void* resul;
          read(fd,resul, msjzise);
          qDebug()<<"cc:"<<resul;
          printf("%s", (char *)resul);
        }

  }
}
