#ifndef SCI_Header
#define SCI_Header

#include <hidef.h>
#include "derivative.h"
#include <string.h>
#include "serial.h"
#include <mc9s12dg256.h>

int current_char_index = 0;
char *print_string = "this is a test\n";

typedef struct SerialPort{
  byte *baudHigh;
  byte *baudLow;
  byte *controlReg1;
  byte *controlReg2;
  byte *dataReg;
  byte *statusReg;
} SerialPort;

SerialPort sci_port = {&SCI1BDH, &SCI1BDL, &SCI1CR1, &SCI1CR2, &SCI1DRL, &SCI1SR1};

void init_serial(struct SerialPort *serial){
  *(serial->baudHigh) = 0;
  *(serial->baudLow) = 156;   
  *(serial->controlReg2) = SCI1CR2_RE_MASK|SCI1CR2_TE_MASK|SCI1CR2_TCIE_MASK;
  *(serial->controlReg1) = 0x00;  
}


void serial_print_string(SerialPort *serial, char *text) {
  
  // Waits for any previous strings to finish printing
  while (128 == (*(serial->controlReg2) & SCI0CR2_SCTIE_MASK)){
  }
  
  strcpy(print_string, text);
  
  *(serial->controlReg2) |= SCI1CR2_SCTIE_MASK;
}

void serial_char_print(SerialPort *serial, char text[]){
  
  static index = 0;
  
  // Resets index to 0 to prepare for printing a new line
  if ('\0' == text[index]){
    index = 0;
  }
  
  // Sends char to serial 
  *(serial->dataReg) = text[index];
  
  index++;
}

// Waits for DIP switch 2 or pushbutton SW4
// Literally just waits for a button to be pressed
// ~~/(>o<)\~~
void button_wait(){
  while(PTH_PTH1){
  }
}
                       

interrupt VectorNumber_Vsci1 void SerialInterruptHandler(){
    if ((*(sci_port.statusReg) & SCI1SR1_TDRE_MASK && print_string[current_char_index]) != 0x00){
      serial_char_print(&sci_port, print_string);
    }
    else if (print_string[current_char_index] == 0x00){
      *(sci_port.controlReg2) &= ~SCI1CR2_TCIE_MASK;
    }
}

#endif
