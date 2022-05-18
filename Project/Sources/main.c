#include <hidef.h>      /* common defines and macros */
#include "derivative.h"      /* derivative-specific definitions */
#include <string.h>
#include "serial.h"
#include "error.h"

char *x = "hello world!!!!!\n";
char *y = "This is a test\n";
char *blank = " ";
 
void main(void) {

  init_serial(&sci_port);
  
	EnableInterrupts;
	
	current_character = &x[0];
	
	serial_print_string(&sci_port, x);

	  
  error_state(1);
   
  serial_print_string(&sci_port, blank);
  
}

