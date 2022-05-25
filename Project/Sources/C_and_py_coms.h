#ifndef COMMS
#define COMMS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "termio.h"

int data[10];
    
void clean_file(){
    FILE* ptr;
    
    ptr = fopen("../MTRX2700_Major/Project/Includes/data.txt", "w");

    fclose(ptr);
}


void data_collector(){
    char buffer[50];
    char *token;
    const char *s = ",";
    int i = 0;
    FILE* ptr;
    int size = 0;
 
    // Opening file in reading mode and determining if file has content
    while (i != 1){
        ptr = fopen("..Includes/data.txt", "r");
                                                      
        fseek(ptr, 0, SEEK_END);
        size = ftell(ptr);

        if (0 != size) {
            i = 1;
        }else{
            fclose(ptr);
        }
    }

    //scan file for string and begin deconstruction into elements of int 
    fscanf(ptr, "%s", buffer);
    i = 0;

    strtok(buffer, s);

    while(token != NULL ) {
      data[i] = atoi(token);
      i++;
    
      token = strtok(NULL, s);
    
      
   }
   
   fclose(ptr);
   
   clean_file();
}


#endif
