#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//#include "../Includes"

void pool_data_transfer(FILE* ptr){
    i = 0;
 
    // Opening file in reading mode and determining if file has content
    while (i != 1){
        ptr = fopen("../MTRX2700_Major/Project/Includes/data.txt", "r");

        fseek (ptr, 0, SEEK_END);
        size = ftell(ptr);

        if (0 != size) {
            i = 1
        }else{
            fclose(ptr)
        }
    }

    return ptr
}

int * data_collector(){
    char buffer[50];
    char *token
    const char s = ","
    int data[10]
    int i = 0

    FILE* ptr = pool_data_transfer(FILE* ptr)

    fscanf(ptr, "%s", buffer);

    strok(buffer, s);

    while( token != NULL ) {
      data[i] = atoi(token);
      i++;
    
      token = strtok(NULL, s);
    
      
   }
   fclose(ptr)
   return data
}

void clean_file(){
    FILE* ptr
    
    ptr = fopen("../MTRX2700_Major/Project/Includes/data.txt", "w");

    fclose(ptr)

    return
}