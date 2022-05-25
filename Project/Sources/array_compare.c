#include <stdio.h>
#include "array_compare.h"

void point_compare(int data_1, int data_2, int *storage_array, int counter) {
      if (((data_1 - data_2) > 1 ) || ((data_2 - data_2) > 1)) {
          *storage_array = counter;
      }
      else{
          *storage_array = -1;
      }
}

void array_check() {
    // Hardcoded Input for now
    //int points[] = {1, 3, 4, 9, 19, 20}; // Points to compare
    int set_1[27] = {11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37};
    int set_2[27] = {11, 00, 13, 00, 00, 16, 17, 18, 00, 20, 21, 22, 23, 00, 25, 26, 27, 28, 00, 30, 31, 32, 00, 34, 35, 00, 00};
    int invalid_array[27];

    int i = 0;
    for (i=0; i < 27; i++) {
        point_compare(set_1[i], set_2[i], &invalid_array[i], i);
    }
}



