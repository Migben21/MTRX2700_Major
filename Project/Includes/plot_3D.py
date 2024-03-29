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
    if type == 's':
        side_length = 40 / division
        empty_matrix = [[0] * int(side_length) for i in range(int(side_length))]
    elif type == 'm':
        side_length = 75 / division
        empty_matrix = [[0] * int(side_length) for i in range(int(side_length))]
    elif type == 'l':
        side_length = 100 / division
        empty_matrix = [[0] * int(side_length) for i in range(int(side_length))]       
    return empty_matrix


def convert_function(item,box_type):
    # Take data from array
    coordinate_x = item.point[0]
    coordinate_y = item.point[1]
    length = item.dimensions[0]
    width = item.dimensions[1]
    height = item.dimensions[2]
    # print(item.point)
    
    # Initialise the dimensions for different-size box
    # side length of each cube
    division = 5
    initial_matrix = Initialised_matrix(box_type)

    # convert the item to cube
    matrix_length = math.ceil(length / division)
    matrix_width = math.ceil(width / division)
    matrix_height = math.ceil(height / division)
    # print('length = ',matrix_length,'   width = ',matrix_width,'    height = ',matrix_height)

    # Add them on matrix    
    for j in range((coordinate_x ), coordinate_x +  matrix_length):
        for i in range(coordinate_y, (coordinate_y + matrix_width)):
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


def plot_3d(item,box_type,Placed_matrix):
    # Convert item to matrix and plot them in 3D in turns
    # Use a convert function to convert item to cube
    # and place in right location
    convert_matrix = convert_function(item,box_type)

    for i in range(len(convert_matrix)):
        for j in range(len(convert_matrix[0])):
            Placed_matrix[i][j] = Placed_matrix[i][j] + convert_matrix[i][j]

    # # Print test for matrix
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

    ax.bar3d(y,x , height, width, depth, z,  color='lightsteelblue', zsort='average')  # width, depth, height
    ax.set_xlabel('Width')
    ax.set_ylabel('Length')
    ax.set_zlabel('Height')
    ax.set_zlim([0,8])
    ax.xaxis.set_ticks_position('top')  #Invert the x axis
    ax.invert_xaxis()

    plt.show()

    # The matrix for plot is inversed, so here inverse back
    Placed_matrix = np.flipud(Placed_matrix)
    return Placed_matrix

# test
# input:
# class item_organised:
#     def __init__(self):
#         self.name = ""
#         self.point = [0,0,0]
#         self.dimensions = [0,0,0]
#         self.rotations = [0,0,0]
#         self.type = "N"

# box_type = 's'
# item = item_organised
# item.point = [0,4,0]
# item.dimensions = [20,10,5]
# matrix = Initialised_matrix(box_type)
# matrix = plot_3d(item,box_type,matrix)
# for i in range(len(matrix)):
#     print(matrix[i])
