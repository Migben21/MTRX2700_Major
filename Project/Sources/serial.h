#ifndef SCI_Header
#define SCI_Header

#include <hidef.h>
#include "derivative.h"
#include <string.h>
#include <mc9s12dg256.h>
#include <stdio.h>


char write_buffer[256];
char *current_character = 0x00;

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
  *(serial->controlReg2) = SCI1CR2_RE_MASK|SCI1CR2_TE_MASK;
  *(serial->controlReg1) = 0x00;  
}


void serial_print_string(SerialPort *serial, char *text) {
    
  *(serial->controlReg2) |= SCI1CR2_SCTIE_MASK;
  
  // Waits for any previous strings to finish printing
  while (128 == (*(serial->controlReg2) & SCI1CR2_SCTIE_MASK)){
  }
  
  current_character = &text[0];

}


void serial_char_print(SerialPort *serial, char text){ 
 
  // Sends char to serial 
  *(serial->dataReg) = text;

}


// Waits for DIP switch 2 or pushbutton SW4
// Literally just waits for a button to be pressed
// ~~/(>o<)\~~
void button_wait(){
  while(PTH_PTH1){
  }
}
                       

#pragma CODE_SEG __NEAR_SEG NON_BANKED
__interrupt void SerialInterruptHandler(void){
  serial_char_print(&sci_port, (*(current_character++)));
  
  while (*current_character != 0x00){
  }
}

#endif
