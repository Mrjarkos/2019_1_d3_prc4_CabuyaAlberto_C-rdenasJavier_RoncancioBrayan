#include "client.h"
#include <QDebug>
Client::Client(char* cc,char* contra )
{
   Cc= cc;
   Contra= contra;
   for (int i=0;i<msjzise;i++) {
       msg[i]='0';

     }
  }

void Client::verifyClient(){


 fd= open(pipename, O_WRONLY);
  if (fd<0){
      close(fd);
      strcpy(msg,"No se pudo abrir la comunicación, intente de nuevo");
    }
  else{

      string send[2];
      send[0]=Cc;
      send[1]=Contra;

      string datout= ";"+send[0]+";"+send[1]+";";

      printf("string: %s string2 %s", send[0].c_str(),send[1].c_str() );
      write(fd,&datout,sizeof(datout));

      sleep(1);

      close(fd);
      fd= open(pipename, O_RDONLY);
      if (fd<0){
          close(fd);
           strcpy(msg,"No se pudo abrir la comunicación, intente de nuevo");
        }
      else{
          void* resul=new char[msjzise];
          read(fd,resul, msjzise);
          //qDebug()<<"cc:"<<(char *)resul;

          printf("%s", (char *)resul);
          strcpy(msg,(char* )resul);
          string msg2= msg;
          if(msg2=="Error al inicar sesion"){
              confirm=1;
            }
          //qDebug()<<"cc:"<<(char *)resul;
          close(fd);
        }

  }

}
void Client::consulclient(int op){
  fd= open(pipenamedata, O_WRONLY);
   if (fd<0){
       close(fd);
       strcpy(msg,"No se pudo abrir la comunicación, intente de nuevo");
     }
   else{
         string datout;
       switch (op) {
         case 1:{
           string send[2];
           send[0]=std::to_string(op);
           send[1]=Cc;

           datout= ";"+send[0]+";"+send[1]+";";
            write(fd,&datout,sizeof(datout));
           //printf("string: %s string2 %s", send[0].c_str(),send[1].c_str() );

            sleep(1);

            close(fd);
          }break ;
          case 2:{
            string send[4];
            send[0]=std::to_string(op);
            send[1]=idaccount;
            send[2]= moneyammount;
            send[3]= Contra;
            datout= ";"+send[0]+";"+send[1]+";"+send[2]+";"+send[3]+";";
            // qDebug()<<"Sending"<<datout.c_str();
            //printf("string: %s string2 %s", send[0].c_str(),send[1].c_str() );
              write(fd,&datout,sizeof(datout));

              sleep(1);

              close(fd);
           }
           break;
         case 3:{
             string send[4];
             send[0]=std::to_string(op);
             send[1]=idaccount;
             send[2]= moneyammount;
             send[3]= Contra;
             datout= ";"+send[0]+";"+send[1]+";"+send[2]+";"+send[3]+";";
               //qDebug()<<"Sending"<<datout.c_str();
             //printf("string: %s string2 %s", send[0].c_str(),send[1].c_str() );
               write(fd,&datout,sizeof(datout));

               sleep(1);

               close(fd);

           }
         }



       fd= open(pipenamedata, O_RDONLY);
       if (fd<0){
           close(fd);
            strcpy(msg,"No se pudo abrir la comunicación, intente de nuevo");
         }
       else{
           void* resul=new char[msjzise];
           read(fd,resul, msjzise);
           //qDebug()<<"cc:"<<(char *)resul;
           printf("%s", (char *)resul);
           strcpy(msg,(char* )resul);
           close(fd);
         }

   }

}
