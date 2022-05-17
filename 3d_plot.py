import numpy as np
import math
import matplotlib.pyplot as plt


def Initialised_matrix(type):
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
        empty_matrix = [[0] * int(side_length) for i in range(int(side_length))]
    elif type == 2:
        side_length = 75 / division
        empty_matrix = [[0] * int(side_length) for i in range(int(side_length))]
    elif type == 3:
        side_length = 100 / division
        empty_matrix = [[0] * int(side_length) for i in range(int(side_length))]       
    return empty_matrix


def convert_function(data_array):
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
    initial_matrix = Initialised_matrix(type)

    # convert the item to cube
    matrix_length = math.ceil(length / division)
    matrix_width = math.ceil(width / division)
    matrix_height = math.ceil(height / division)
    # print('length = ',matrix_length,'   width = ',matrix_width,'    height = ',matrix_height)

    # Add them on matrix    
    for i in range((coordinate_x - matrix_length), coordinate_x):
        for j in range(coordinate_y, (coordinate_y + matrix_width)):
            initial_matrix[i][j] = initial_matrix[i][j] + matrix_height

    return initial_matrix


# Convert 2D matrix into an 1D array
def flatten(a):
    if not isinstance(a, (list, )):
        return [a]
    else:
        b = []
        for item in a:
            b += flatten(item)
    return b


# Read the item data
############################
# Example:
# type = 1
# coodinate_x = 4   [4,0,0]
# coodinate_y = 0
# length = 18
# width = 15.6
# height = 13
############################

data_array1 = [1, 4, 0, 0, 18, 15, 13]
data_array2 = [1, 2, 0, 3, 10, 5, 5]
data = [data_array1, data_array2]
number_of_items = len(data)

# Error handling
# 1. Not the defined size of the box
# 2. Given hight is lower than height of existing items
for n in range (number_of_items):
    if data[n][0] != 1 and data[n][0] != 2 and data[n][0] != 3:
        print('Error! Please use Correct box!\n')
        break

    
Placed_matrix = Initialised_matrix(data[0][0])
buffer_matrix = Initialised_matrix(data[0][0])

# Convert item to matrix and plot them in 3D in turns
for i in range(number_of_items):
    # Use a convert function to convert item to cube
    # and place in right location
    # Error handling first if sth wrong on height
    if data[i][3] < buffer_matrix[data[i][1]-1][data[i][2]]:
        print('Error! The position in height of item',i+1,' is not allowed!\n')
        # print(data[i][3],buffer_matrix[data[i][1]-1][data[i][2]])
        # print(data[i][1],data[i][2])
        break

    convert_matrix = convert_function(data[i])
    buffer_matrix = convert_matrix
    
    for i in range(len(convert_matrix)):
        for j in range(len(convert_matrix[0])):
            Placed_matrix[i][j] = Placed_matrix[i][j] + convert_matrix[i][j]
    
    # Print test for matrix
    # for i in range(len(Placed_matrix)):
    #     print(Placed_matrix[i])
    # print('\n')


    ## 3D plot
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    x = np.arange(len(Placed_matrix))
    y = np.arange(len(Placed_matrix))
    z = flatten(Placed_matrix)

    xx,yy = np.meshgrid(x,y)
    x, y = xx.ravel(), yy.ravel()

    height = np.zeros_like(z)
    width = depth = 1

    # ax.title('Placement')
    ax.bar3d(x,y , height, width, depth, z,  color='b', zsort='average')  # width, depth, height
    ax.set_xlabel('Width')
    ax.set_ylabel('Length')
    ax.set_zlabel('Height')
    ax.set_zlim([0,8])

    plt.show()