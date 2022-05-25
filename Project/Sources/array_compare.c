#include <stdio.h>
#include "array_compare.h"

void point_compare(int data_1, int data_2, int *storage_array, int counter) {
    if (data_1 != data_2) {
        *storage_array = counter;
    }
    else{
        *storage_array = -1;
    }
}

int main() {
    // Hardcoded Input for now
    //int points[] = {1, 3, 4, 9, 19, 20}; // Points to compare
    int set_1[27] = {11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37};
    int set_2[27] = {11, 00, 13, 00, 00, 16, 17, 18, 00, 20, 21, 22, 23, 00, 25, 26, 27, 28, 00, 30, 31, 32, 00, 34, 35, 00, 00};
    int invalid_array[27];

    int i = 0;
    for (i=0; i < 27; i++) {
        point_compare(set_1[i], set_2[i], &invalid_array[i], i);
    }

    printf("Invalid point indexi: ");
    for (i=0; i < 27; i++) {
        if (invalid_array[i] != -1) {
            printf("%i ", invalid_array[i]);
        }
        //printf("%i ", array[i]);
    }

    return 0;
}

/* Old attempt that was meant to take in and output arrays
int array_compare(int comp_points[], int dataset_1[], int dataset_2[], int *invalid_points[]) {
    int i = 0, k = 0, j = 0;
    
    int no_invalid = 0; // Integer to store number of invalid points

    int no_points = 27;

    for (i=0; i < no_points; i++) {
        // Checks if it's one of the points to be compared, if so then compares
        // Have to put -1 since i starts counting from 0
        if (i == comp_points[k] - 1) { 
            if (dataset_1[i] != dataset_2[i]) {
                (*invalid_points)[j] = i + 1; // Since i counts at 0
                j++;
                no_invalid++;
            }
            k++;
        }
    }
    return 0;
}
*/