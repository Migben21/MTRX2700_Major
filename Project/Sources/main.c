#include <hidef.h>      /* common defines and macros */
#include "derivative.h"      /* derivative-specific definitions */
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include "serial.h"
#include "error.h"
#include "button.h"
#include "stepper_motor.h"
//#include "C_and_py_coms.h"
#include "termio.h"
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
char *z = "this is the end\n";

int data[10];

int py_err; // Placeholder for error return from python functions
// Placeholder for python function pointer
// Will need to be declared within code with appropriate amount of function parameters

int (*py_function)(); 

  
 
void main(void) {
  //for reading from file however converted to take on input
  int i = 0;
	int *arr;
	const char *s = ","; 
  const char *str_data = "1,1,1,1,1,1,1,1"; //input data here
  char *token;
  
  init_button();
  init_serial(&sci_port);
	EnableInterrupts;
	current_character = &x[0];
	data[0] = 420;  // arbitrary number to poll for changes to data.txt
	
	while(1){
	  
	  
  	serial_print_string(&sci_port, y);
    
    error_button();  
                                
    //read fropm file(was :()
    /*
    while (i != 1){
        ptr = fopen("../MTRX2700_Major/Project/Includes/data.txt", "r");

        fseek (ptr, 0, SEEK_END);
        size = ftell(ptr);

        if (0 != size) {
            i = 1;
        }else{
            fclose(ptr);
        }
    }
    */
    

    //scan string and begin deconstruction into elements of int 


    token = strtok(str_data, s);

    while(token != NULL ) {
      arr[i] = atoi(token);
      i++;
    
      token = strtok(NULL, s);    
   }
  
    
    serial_print_string(&sci_port, x);
    
    lidar();
    
    //motor_init(5, 0);
    
    //check
    
    //clean something idk
    
    //go to next box
    
    serial_print_string(&sci_port,z);
      
	}

}

