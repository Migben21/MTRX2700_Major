import math


def convert_in_function(data_array):
    # Take data from array
    type = data_array[0]
    coordinate_x = data_array[1]
    coordinate_y = data_array[2]
    length = data_array[4]
    width = data_array[5]
    height = data_array[6]

    # Initialise the dimensions for different-size box
    # side length of each cube
    division = 5
    # Type for box is: 1 for small; 2 for medium; 3 for large
    # Box sizes and dimensions(cm):
    # Large: 100*100*40
    # Medium: 75*75*40
    # Small: 40*40*40
    if type == 1:
        side_length = 40 / division
        initial_matrix = [[0] * int(side_length) for i in range(int(side_length))]
    elif type == 2:
        side_length = 75 / division
        initial_matrix = [[0] * int(side_length) for i in range(int(side_length))]
    elif type == 3:
        side_length = 100 / division
        initial_matrix = [[0] * int(side_length) for i in range(int(side_length))]

    # convert the item to cube
    matrix_length = math.ceil(length / division)
    matrix_width = math.ceil(width / division)
    matrix_height = math.ceil(height / division)

    # Add them on matrix
    for i in range((coordinate_x - matrix_length), (coordinate_x )):
        for j in range(coordinate_y, (coordinate_y + matrix_width )):
            initial_matrix[i][j] = initial_matrix[i][j] + matrix_height
    
    return initial_matrix

data_array1 = [1,4,0,3,18,15.6,13]
x = convert_in_function(data_array1)
for i in range(len(x)):
    print(x[i])