#ifndef ERR_Header
#define ERR_Header

#include <hidef.h>
#include "derivative.h"
#include "serial.h"


char *error_message;


void error_state(int errCode){
  
  switch (errCode) {
    case 1:
      error_message = "Invalid Item name in contents\n";
      break;
    case 2:
      error_message = "Item too big to fit inside any box\n";
      break;
    default:
      error_message = "Undefined Error Code\n";
      break;
  }
  
  serial_print_string(&sci_port, error_message);
}


#endif