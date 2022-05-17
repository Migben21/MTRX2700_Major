#include <hidef.h>      /* common defines and macros */
#include "derivative.h"      /* derivative-specific definitions */
#include <string.h>
#include "serial.h"

char x[16] = "hello world\r";
 
void main(void) {

  init_serial(&sci_port);
  
	EnableInterrupts;
	
	serial_print_string(&sci_port, x);

}

