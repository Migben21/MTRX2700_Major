#ifndef SCI_Header
#define SCI_Header

#include <mc9s12dg256.h>


typedef struct SerialPort{
  byte *baudHigh;
  byte *baudLow;
  byte *controlReg1;
  byte *controlReg2;
  byte *dataReg;
  byte *statusReg;
}SerialPort;

void init_serial(SerialPort *serial);

void serial_print(char *text, SerialPort *serial);

#endif