#ifndef BUTT_HEAD
#define BUTT_HEAD

#include <stdio.h>
#include "serial.h"


// Writes 00000000 to the PORT H direction register for it to take input
void init_button(){
  DDRH = 0x00;
}


// Waits for DIP switch 2 or pushbutton SW4
// Meant to be used to step through the code
void step_button_wait(){
  while(PTH_PTH1){
  }
}


// When error is raised, prints to serial asking if 
// user wishes to try again or exit program
// Uses SW3 (PTH_PTH2) as exit and SW2 (PTH_PTH3) as try again
// Returns 1 is SW2 pushed or 0 is SW3 pushed
int error_button(){

  char *message = "Error raised, press SW3 if you wish to try again or SW2 if you wish to exit\n";
  
  serial_print_string(&sci_port, message);
  
  // Waits for SW3 or SW2 to be pushed
  while(!(PTH_PTH2 && PTH_PTH3)){
  }
  
  if (PTH_PTH3){
    serial_print_string(&sci_port, "Attempting last function again");
    return 0;
  }
  else if (PTH_PTH2){
    serial_print_string(&sci_port, "Exiting program");
    return 1;
  }
}


// Test function meant to check if something is working properly
// Enables LEDS, sets PORTB to be output and turns all PORTB LEDs on
void led_test(){
  
  DDRJ = 0xFF;
  DDRB = 0xFF;
  
  PORTB = 0xFF;
  
}


#endif