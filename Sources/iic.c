/*
* IIC Host Driver for Dragon12-plus
* Author: Tom Almy
* Date: January 29, 2008

* Updated: Eduardo Nebot July 2015
* refactored (major): Stewart Worrall 2021
* updated: Stewart Worrall 2022
  
    **********************
   
   Resources Used: Timer 7
*/


#include <hidef.h>      /* common defines and macros */
#include "derivative.h"      /* derivative-specific definitions */

#include "iic.h"

#define IIC_TIMEOUT_ITERATIONS 10


// *** timeout control ***
volatile uint8_t alarmSignaled = 0; /* Flag set when alarm 1 signaled */

volatile uint16_t currentTime = 0; /* variables private to timeout routines */
uint16_t alarmTime = 0;
volatile uint8_t alarmSet = 0;

void setAlarm(uint16_t msDelay);

IIC_ERRORS iicstart(uint8_t control);      
IIC_ERRORS iicrestart(uint8_t *buffer);    
IIC_ERRORS iictransmit(uint8_t *buffer); 

void iicstop(void);
void iicswrcv(void);

// receive a single byte
IIC_ERRORS iicreceiveone(uint8_t *buffer);      

// receive one of a sequence of bytes
IIC_ERRORS iicreceive(uint8_t *buffer);

// receive the second last byte
// disable ACK for last read
IIC_ERRORS iicreceivem1(uint8_t *buffer);

// receive the last byte
// reenable ACK, request stop
IIC_ERRORS iicreceivelast(uint8_t *buffer);


// *** I2C Functions ***

// prototype for initialising the IIC timeout timers
void Init_TC7(void);


void iicinit(IIC_SPEED iic_speed) {

  // start the interrupt timer for iic timeouts
  Init_TC7();

  if (iic_speed == IIC_20KHZ) {
    IBFD = 0x35; // 20KHz operation
  } else if (iic_speed == IIC_100KHZ) {
    IBFD = 0x23; // 100KHz operation
  } else {                               
    // 20KHz is the default
    IBFD = 0x35; // 20KHz operation
  }
    
  IBAD = 0x2; // Slave address is 1 (never address ourselves, please!)
  IBCR |= 0x80; // Set IBEN
}


/* Returns error code on failure */
IIC_ERRORS iic_request_data(uint8_t device, uint8_t address) {
    int result = NO_ERROR;

    // request iic data
    result = iicstart(device);

    if (result != NO_ERROR) {
      iicstop();
      return result;
    }
    
    result = iictransmit(&address);
    return result;
}


/* Returns error code on failure */
IIC_ERRORS iic_read_data(uint8_t device, uint8_t *buffer, uint8_t buffer_size) {

  IIC_ERRORS result = 0;
  int buffer_counter = 0;
  
  if (buffer_size < 2) {
    return IIC_DATA_SIZE_TOO_SMALL; 
  }
   
  // receive iic data
  result = iicrestart(&device);

  // set the iic to receive data
  iicswrcv();

  for (buffer_counter = 0; 
       buffer_counter < buffer_size - 2; 
       buffer_counter++)
  {
    // NOTE: the bytes are assumed to be LSB first
    //       so each pair should be swapped around
    //       read LSB, then MSB
    if (buffer_counter & 0x01)
      result = iicreceive(&(buffer[buffer_counter - 1]));
    else
      result = iicreceive(&(buffer[buffer_counter + 1]));
  }

  // Last two bits require a different read process
  // NOTE: the bytes are assumed to be LSB first
  //       so each pair should be swapped around
  //       read LSB, then MSB
  result = iicreceivem1(&(buffer[buffer_counter + 1]));
  result = iicreceivelast(&(buffer[buffer_counter]));
  
  return result;
}



/* Returns error code on failure */
IIC_ERRORS iic_send_data(uint8_t device, uint8_t *buffer, uint8_t buffer_size) {
 
    int results = NO_ERROR;
    int counter = 0;

    results = iicstart(device);

    for (counter = 0; counter < buffer_size; counter++) {
      results = iictransmit(&(buffer[counter]));
    }
    
    iicstop(); 
      
    return results;
}




/* Returns error code on failure */
IIC_ERRORS iicresponse(void) { 

  // wait to see what our response is
  setAlarm(IIC_TIMEOUT_ITERATIONS);

  while ((IBSR & 0x2) == 0 && !alarmSignaled) {}; // Wait for IBIF to set
  if (alarmSignaled) {
    iicstop();
    return NO_RESPONSE;
  }
  IBSR &= 0x2;        // Clear IBIF
  if (IBSR&1) { // NAK -- stop!
    iicstop();
    return NAK_RESPONSE;
  }
  
  return NO_ERROR;
}    


/* Returns error code on failure */
IIC_ERRORS iicstart(uint8_t control) {
    setAlarm(IIC_TIMEOUT_ITERATIONS);
    while (IBSR_IBB != 0 && !alarmSignaled) {}; // Wait for IBB flag to clear
    if (alarmSignaled) {
        return IIB_CLEAR_TIMEOUT;
    }
    IBCR |= 0x30;
    IBDR = control;
    setAlarm(IIC_TIMEOUT_ITERATIONS);
    while (IBSR_IBB && !alarmSignaled) {}; // Wait for IBB flag to set
    if (alarmSignaled) {
        return IIB_SET_TIMEOUT;
    }
    return iicresponse();
}

    
void iicstop(void) {
    IBCR &= ~0x20;
}


IIC_ERRORS iicrestart(uint8_t *buffer) {
    IBCR |= 0x04;
    IBDR = *buffer;
    return iicresponse();
}


IIC_ERRORS iictransmit(uint8_t *buffer) {
    IBDR = *buffer;
    return iicresponse();
}


void iicswrcv(void) {
  volatile uint8_t read_value;

  IBCR &= ~0x10; // put in receive mode
  read_value = IBDR;    // dummy read (better not be optimized out!)
}


/* Returns error code on failure */
IIC_ERRORS iicreceive(uint8_t *buffer) {
    setAlarm(IIC_TIMEOUT_ITERATIONS);
    
    while ((IBSR & 0x2) == 0 && !alarmSignaled) {};
    if (alarmSignaled) {
        return RECEIVE_TIMEOUT;
    }
    IBSR &= 0x2;
    *buffer = IBDR;
    
    return NO_ERROR;
}


/* Returns error code on failure */
IIC_ERRORS iicreceivem1(uint8_t *buffer) {
    setAlarm(IIC_TIMEOUT_ITERATIONS);
    while ((IBSR & 0x2) == 0 && !alarmSignaled) {};
    if (alarmSignaled) {
        return RECEIVE_TIMEOUT;
    }
    IBSR &= 0x2;
    IBCR |= 0x8; // disable ACK for last read
    *buffer = IBDR;
    
    return NO_ERROR;
}


/* Returns error code on failure */
IIC_ERRORS iicreceivelast(uint8_t *buffer) {
    setAlarm(IIC_TIMEOUT_ITERATIONS);
    while ((IBSR & 0x2) == 0 && !alarmSignaled) {};
    if (alarmSignaled) {
        return RECEIVE_TIMEOUT;
    }
    IBSR &= 0x2;
    IBCR &= ~0x8;    // reenable ACK
    IBCR &= ~0x20;    // generate STOP
    IBCR |= 0x10;    // set transmit
    
    *buffer = IBDR;
    return NO_ERROR;
}


/* Returns error code on failure */
IIC_ERRORS iicreceiveone(uint8_t *buffer) {
    IBCR |= 0x8;    // Disable ACK
    iicswrcv();
    
    return iicreceivelast(buffer);
}


// *** Alarms ***
void setAlarm(uint16_t msDelay)
{
  currentTime = 0;
  alarmTime = currentTime + msDelay;
  alarmSet = 1;
  alarmSignaled = 0;
}


void Init_TC7 (void) {
  TSCR1_TEN = 1;
  
  TSCR2 = 0x00;   // prescaler 1, before 32 = 0x04
  TIOS_IOS7 = 1;   // set channel 7 to output compare
    
  TCTL1_OL7 = 1;    // Output mode for ch7
  TIE_C7I = 1;   // enable interrupt for channel 7
}


// the interrupt for timer 7 which is used for a iic timeout
#pragma CODE_SEG __NEAR_SEG NON_BANKED /* Interrupt section for this module. Placement will be in NON_BANKED area. */
__interrupt void TC7_ISR(void) { 
   
    TC7 = TCNT + 30000;   // add a delay to the timer
    TFLG1 |= TFLG1_C7F_MASK;
    
    currentTime++;
    if (alarmSet && currentTime == alarmTime)
    {
        alarmSignaled = 1;
        alarmSet = 0;
    }
}
