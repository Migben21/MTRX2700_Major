#include <hidef.h>      /* common defines and macros */
#include "derivative.h"      /* derivative-specific definitions */
#include <string.h>
#include "serial.h"
#include "error.h"
#include "button.h"
#include "stepper_motor.h"
#include "C_and_py_coms.h"
#include "array_compare.h"
#include "accelerometer.h"
#include "servo.h"
#include "pll.h"
#include "l3g4200d_definitions.h"
#include "l3g4200d.h"
#include "iic.h"
#include "gyro.h"
#include "laser.h"
#include "servo_laser.h"

char *x = "hello world!!!!!\n";
char *y = "This is a test\n";

int py_err; // Placeholder for error return from python functions
// Placeholder for python function pointer
// Will need to be declared within code with appropriate amount of function parameters

int (*py_function)(); 
 
void main(void) {
  
  init_button();
  init_serial(&sci_port);
	EnableInterrupts;
	current_character = &x[0];
	
	serial_print_string(&sci_port, x);
  
  // Waits for the string to finish sending
  // Last 2 characters in last printed string get thanos snapped if this isnt there
  while (*current_character != 0x00){
  }

}

