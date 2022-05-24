#include <stdio.h>

int main() {
    // Hardcoded Input for now:
    int comp_points[] = {2, 4, 5, 6}; // Points to compare
    int dataset_1[] = {14, 32, 23, 55, 66, 34, 50};
    int dataset_2[] = {14, 32, 23, 43, 40, 34, 50};

    int i, k, j = 0;
    int invalid_points[69]; // Array to store index numbers of invalid points
    int no_invalid = 0; // Integer to store number of invalid points

    // Checking sizes of arrays, division to account for memory differences
    // Checking number of points to compare
    int no_comp_points = (sizeof comp_points) / (sizeof comp_points[0]); 
    
    int no_points_1 = (sizeof dataset_1) / (sizeof dataset_1[0]);
    int no_points_2 = (sizeof dataset_2) / (sizeof dataset_2[0]);
    if (no_points_1 != no_points_2) {
        printf("Datasets do not have same number of points.\n");
    }

    printf("Points to Compare: ");
    for (i=0; i < no_comp_points; i++) {
        printf("%d ", comp_points[i]);
    }

    for (i=0; i < no_points_1; i++) {
        // Checks if it's one of the points to be compared, if so then compares
        // Have to put -1 since i starts counting from 0
        if (i == comp_points[k] - 1) { 
            if (dataset_1[i] != dataset_2[i]) {
                invalid_points[j] = i + 1; // Since i counts at 0
                j++;
                no_invalid++;
            }
            k++;
        }
    }

/* // This variation checks through all the points
    for (i=0; i < no_points_1; i++) {
        if (dataset_1[i] != dataset_2[i]) {
            invalid_points[j] = i;
            j++;
            no_invalid++;
        }
    }
*/

    printf("\nInvalid points: ");
    for (i=0; i < no_invalid; i++) {
        printf("%d ", invalid_points[i]);
    }
    printf("\n");

    return 0;
}