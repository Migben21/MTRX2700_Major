#include <stdio.h>

int main() {
    // Hardcoded Input for now:
    int comp_points[] = {1, 3, 4, 9, 19, 20}; // Points to compare
    int dataset_1[27] = {11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37};
    int dataset_2[27] = {11, 00, 13, 00, 00, 16, 17, 18, 00, 20, 21, 22, 23, 00, 25, 26, 27, 28, 00, 30, 31, 32, 00, 34, 35, 00, 00};

    int i, k, j = 0;
    int invalid_points[27]; // Array to store index numbers of invalid points
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

    printf("\nNumber of Invalid Points: %d", no_invalid);
    printf("\nInvalid points: ");
    for (i=0; i < no_invalid; i++) {
        printf("%d ", invalid_points[i]);
    }
    printf("\nNo. of Points: %d\n", no_points_1);

    return 0;
}
