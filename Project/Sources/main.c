#include <hidef.h>      /* common defines and macros */
#include "derivative.h"      /* derivative-specific definitions */
#include <string.h>
#include "serial.h"

char *x = "hello world!!!!!\n";
char *y = "This is a test\n";
 
void main(void) {

  init_serial(&sci_port);
  
	EnableInterrupts;
	
	current_character = &x[0];
	
	while(1){
	  serial_print_string(&sci_port, y);
	  
	  *(sci_port.controlReg2) |= SCI1CR2_TCIE_MASK;

	}
}

