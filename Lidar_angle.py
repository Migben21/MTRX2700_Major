import numpy as np
import math

# input:
class item_organised:
    def __init__(self):
        self.name = ""
        self.point = [0,0,0]
        self.dimentions = [0,0,0]
        self.rotations = [0,0,0]
        self.type = "N"

box_type = 's'
item = item_organised
item.point = [2,2,0]
item.dimentions = [20,10,5]

# # Item dimensions: [length,width,height] 
# item.dimentions = [5,5,5]
# # item_dimesion = item.dimension
# # Item coordinater:
# item.point = [0,0,0]
# # item.point = item.point
# Lidar position: eg.[len/2,wid/2,hight]
# box_dimension = [40,40,40]
# box_dimension = 

def angle_at_corners(item,box_type): #main function
    # Initialise the angle and corners, lidar position is at center of box
    angle=np.full((4,2),0)
    corners = [[0,1,0],[1,1,0],[1,0,0],[0,0,0]]
    division = 5
    box_dimension = box_cal(box_type)

    ## Find four corners
    corners[0][0] = item.point[0]*division                    # left-top point
    corners[0][1] = item.point[1]*division + item.dimentions[1]
    corners[0][2] = item.point[2]*division + item.dimentions[2]
    corners[1][0] = item.point[0]*division + item.dimentions[0]# right-botton point
    corners[1][1] = item.point[1]*division + item.dimentions[1]
    corners[1][2] = item.point[2]*division + item.dimentions[2] 
    corners[2][0] = item.point[0]*division + item.dimentions[0]# right-botton point
    corners[2][1] = item.point[1]*division
    corners[2][2] = item.point[2]*division + item.dimentions[2]
    corners[3][0] = item.point[0]*division                    # left-botton point
    corners[3][1] = item.point[1]*division
    corners[3][2] = item.point[2]*division + item.dimentions[2]
    # print(corners)

    for i in range(len(corners)):
        angle = calculate_angle(corners[i],i,angle,box_dimension)
    return angle

def box_cal(box_type):
    if box_type == 's':
        box_dimension = [40,40,40]
    elif box_type == 'm':
        box_dimension = [75,75,40]
    elif box_type == 'l':
        box_dimension = [100,100,40]
    return box_dimension

def calculate_angle(point,n,angle_matrix,box_dimension):
        
        lidar_position = [box_dimension[0]/2,box_dimension[1]/2,300]
        # distance in x
        x_distance = lidar_position[0] - point[0]
        # distance in y
        y_distance = lidar_position[1] - point[1]
        # distance in z
        z_distance = lidar_position[2] - point[2]
        # print(' x=',x_distance,' y=',y_distance,' z=',z_distance)
        
        # calculate the angle value
        # xy plane and zy
        angle_matrix[n][0] = round(90 -math.atan2(y_distance,x_distance)/math.pi*180)
        if y_distance == 0:
            angle_matrix[n][1] = round(math.atan2(x_distance,z_distance)/math.pi*180)
        else:
            angle_matrix[n][1] = round(math.atan2(y_distance,z_distance)/math.pi*180)
        # print(angle)
        return angle_matrix


# test
angle = angle_at_corners(item,box_type)
print(angle)