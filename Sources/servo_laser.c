#include <hidef.h>      /* common defines and macros */
#include <assert.h>
#include "derivative.h"      /* derivative-specific definitions */

// need this for string functions
#include <stdio.h>

#include "pll.h"
//#include "simple_serial.h"
#include "servo.h"
#include "laser.h"



void delay(int duration){

int l,m;
for(l=0; l<duration; l++) {
  for(m=0; m<4000; m++);
}
  
}

void main(void) {

  int azi = 1700;
  int ele = 2300;
  int i = 0;
  int j = 0;
  int k = 0;
  int l = 0;  
  
  int azi_array[27];
  int ele_array[27];          
  unsigned long singleSample_array[27];  
  
  //char buffer[128];  
  
  unsigned long singleSample;
  
  EnableInterrupts;

  // make sure the board is set to 24MHz
  //  this is needed only when not using the debugger
  PLL_Init();

  // initialise PWM
  PWMinitialise();
  
  laserInit();

  Init_TC6();
  

  
  for(l=1; l<=3; l++){
    int azi = 1800;
    int ele = 2300;  
    for(i=1; i<=3; i++){
      for(j=1; j<=3; j++){
        setServoPose(azi,ele);
        delay(2000);
        GetLatestLaserSample(&singleSample);
       
        azi_array[k] = azi;
        ele_array[k] = ele;
        singleSample_array[k] = singleSample;

        azi += 500;
        k++;
         
      }
    if (i<3){
      azi = 1800;
      ele += 300;
    }
  }
  }
  
    


}
  
