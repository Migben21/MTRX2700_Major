#ifndef MOTOR_HEAD
#define MOTOR_HEAD

#include <hidef.h>      /* common defines and macros */
#include "derivative.h"      /* derivative-specific definitions */

#define NUM_OF_STATES 8 //There are 8 different states in this particular example.
#define DELAY_MAX 2000 //The maximum # of counts used to create a time delay.


void port_selector(int i, char *state_array, int next_state){
   int PTU;
   int PTL;
   int PTV;
   
   switch(i){
   case(0):
    //setting up port U for x coord stepper motor
    PTU = state_array[next_state]; 
   break;

   case(1):
    //setting up port L for y coord stepper motor 
    PTL = state_array[next_state]; 
   break;

   case(2):
    //setting up port V for z coord stepper motor
    PTV = state_array[next_state]; 
   break; 
 }
}


void motor_stepping(int steps, char next_state, char *state_array, int i){
  int steps_to_move = steps; //Set the # of steps to move. An arbitrary positive # can be used.
  int a;
  
  for(a = 0; a < DELAY_MAX; a++){
     //Wait here for a while.
  }
  
  while (steps_to_move > 0){
    //If next_state is greater than the highest
    //available state, 7, then cycle back to 0
    if (next_state > (NUM_OF_STATES - 1)){
        next_state = 0;
    }
    port_selector(i, state_array, next_state); //Place new value in Port U. Rotation may be observed
    for(a = 0; a < DELAY_MAX; a++)
      {
    //Wait here for a while.
    }
    next_state++; //Increment next_state. Cycling though the states causes rotation
    //in one direction. Decrementing states causes opposite rotation.
    steps_to_move--; //Subtract 1 from the total # of steps remaining to be moved.
    
  }
}


void motor_init(int steps,int i){
/*******************CREATE VARIABLES*******************/
   char letters[3] = {'X','Y','Z'};
   //This array actually contains the state values that will be placed on Port U.
   //State #0 corresponds to a value of 0x06, state #1 corresponds to a value of 0x02, etc.
   int state_array[NUM_OF_STATES] = {0x06, 0x02, 0x0A, 0x08, 0x09, 0x01, 0x05, 0x04};
   
   //Used to select the next state to put in register U.
   int next_state = 0; //Init next_state to state 0. next_state can start from any state
   //within the range of possible states in this example, 0-7.
   //initialising intergers to store port addresses
   int DDRU;
   int PTU;
   int PTL;
   int DDRL;
   int DDRV;
   int PTV;
   //selecting the ports
   switch(i){
     case(0):
        //setting up port U for x coord stepper motor
        DDRU = 0xFF; //Writing 0xFF to DDRU sets all bits of Port U to act as output.
        PTU = 0; //Init Port U by writing a value of zero to Port U.
        PTU = state_array[next_state]; 
     break;

     case(1):
      //setting up port L for y coord stepper motor 
      DDRL = 0xFF; //Writing 0xFF to DDRU sets all bits of Port U to act as output.
      PTL = 0; //Init Port U by writing a value of zero to Port U.
      PTL = state_array[next_state]; 
     break;

     case(2):
      //setting up port V for z coord stepper motor
      DDRV = 0xFF; //Writing 0xFF to DDRU sets all bits of Port U to act as output.
      PTV = 0; //Init Port U by writing a value of zero to Port U.
      PTV = state_array[next_state]; 
     break; 
   }

 printf("---%c Steppermotor Activated---\n", letters[i]);
 printf("Moving %d rotations in %c direction\n", steps, letters[i]);

//Init Port to the starting state. In this example,
 //since only 4 pins are needed to control the motor, only
 //the lower nibble of Port is being used. This line
 //selects state 0 and places the corresponding value
 //(0x06) in the lower nibble of Port.

  motor_stepping(steps, next_state, state_array, i);

  return;
}


void data_init_stepper(int x, int y, int z){
  /*relations of each point referencing 5 cm*/
  //8 bits in the u-port, upper part for x and lower part for y
  //With a 6 cm diameter gear geared down to a 5cm circumference gear to move both bars, this allows each value of x and y to be consistant
  int i;
  int rotations[3];
  
  rotations[0] = x;
  rotations[1] = y;
  rotations[2] = z;

  //move steppermotors to their correct postions 
  for (i = 0; i < 3; i++){
    motor_init(rotations[i], i);
  }

  //move steppermotors to their rest positions 
  for (i = 2; i >= 0; i--){
    motor_init(-rotations[i], i);
  }
}


#endif

