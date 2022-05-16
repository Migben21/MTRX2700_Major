#include <hidef.h>
#include "derivative.h"
#include <string.h>
#include <stdio.h>
#include "serial.h"

SerialPort sci_port = {&SCI1BDH, &SCI1BDL, &SCI1CR1, &SCI1CR2, &SCI1DRL, &SCI1SR1};

void init_serial(struct SerialPort *serial){
  *(serial->baudHigh) = 0;
  *(serial->baudLow) = 156;   
  *(serial->controlReg2) = SCI1CR2_RE_MASK|SCI1CR2_TE_MASK|SCI1CR2_TCIE_MASK;
  *(serial->controlReg1) = 0x00;
  
}


void serial_print(char *text, SerialPort *serial){
  ;;  
}


interrupt VectorNumber_Vsci1 void SerialInterrupt(){
  ;; 
}