#ifndef SCI_Header
#define SCI_Header

#include <hidef.h>
#include "derivative.h"
#include <string.h>
#include <mc9s12dg256.h>
#include <stdio.h>


extern char  *current_character = 0x00;

typedef struct SerialPort{
  byte *baudHigh;
  byte *baudLow;
  byte *controlReg1;
  byte *controlReg2;
  byte *dataReg;
  byte *statusReg;
} SerialPort;


extern SerialPort sci_port = {&SCI1BDH, &SCI1BDL, &SCI1CR1, &SCI1CR2, &SCI1DRL, &SCI1SR1};


void init_serial(struct SerialPort *serial){
  *(serial->baudHigh) = 0;
  *(serial->baudLow) = 156;   
  *(serial->controlReg2) = SCI1CR2_RE_MASK|SCI1CR2_TE_MASK|SCI1CR2_TCIE_MASK;
  *(serial->controlReg1) = 0x00;  
}


void serial_char_print(SerialPort *serial, char text){ 
  
  int wait_counter = 0;
  while ((*(serial->statusReg) & SCI1SR1_TDRE_MASK) == 0){
    if (wait_counter < 0xFE){
      wait_counter++;
    }
  }
  
  *(serial->dataReg) = text;
}


void serial_print_string(SerialPort *serial, char *text) {
  while (*text){
    serial_char_print(serial, *text);
    text++;
  } 
}
                       

#pragma CODE_SEG __NEAR_SEG NON_BANKED
__interrupt VectorNumber_Vsci1 void SerialInterruptHandler(void){
  
  if (*(sci_port.statusReg) & SCI1SR1_TDRE_MASK && *current_character != 0x00){
    serial_char_print(&sci_port, *(current_character++));
  } 
  else if (*current_character == 0x00){
    *(sci_port.controlReg2) &= ~SCI1CR2_TCIE_MASK;
  }
}

#endif
