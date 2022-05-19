#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void pool_data_transfer(FILE* ptr){
    i = 0;
 
    // Opening file in reading mode and determining if file has content
    while (i != 1){
        ptr = fopen("test.txt", "r");

        fseek (ptr, 0, SEEK_END);
        size = ftell(ptr);

        if (0 != size) {
            i = 1
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

      return data
   }*
}