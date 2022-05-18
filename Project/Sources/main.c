#include <hidef.h>      /* common defines and macros */
#include "derivative.h"      /* derivative-specific definitions */
#include <string.h>
#include "serial.h"
#include "error.h"
#include "button.h"

char *x = "hello world!!!!!\n";
char *y = "This is a test\n";

 
void main(void) {

  init_serial(&sci_port);
  
	EnableInterrupts;
	
	current_character = &x[0];
	
	serial_print_string(&sci_port, x);
	
	error_button();
	
  error_state(1);
  
  // Waits for the string to finish sending
  // Last 2 characters in last printed string get thanos snapped if this isnt there
  while (*current_character != 0x00){
  }
  
}

