#include <hidef.h>      /* common defines and macros */
#include "derivative.h"      /* derivative-specific definitions */
#include <string.h>
#include "serial.h"
#include "error.h"
#include "button.h"

char *x = "hello world!!!!!\n";
char *y = "This is a test\n";

int py_err; // Placeholder for error return from python functions
// Placeholder for python function pointer
// Will need to be declared within code with appropriate amount of function parameters

int (*py_function)(); 
 
void main(void) {
  
  py_err = 2;
  
  init_button();
  
  init_serial(&sci_port);
  
	EnableInterrupts;
	
	current_character = &x[0];
	
	serial_print_string(&sci_port, x);
	
	error_button();
	
	serial_print_string(&sci_port, y);
	
	step_button_wait();
	led_test();
	
  error_state(py_err);
  
  // Waits for the string to finish sending
  // Last 2 characters in last printed string get thanos snapped if this isnt there
  while (*current_character != 0x00){
  }
  
  step_button_wait();
  // first function
}

