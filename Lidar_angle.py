import numpy as np
import math

# input:
# Item dimensions: [length,width,height] 
item_dimension = [5,5,5]
# item_dimesion = object.dimension
# Item coordinater:
item_position = [0,0,0]
# item_position = object.point
# Lidar position: eg.[len/2,wid/2,hight]
box_dimension = [40,40,40]
# box_dimension = 

def angle_at_corners(item_dimension,item_position,box_dimension): #main function

    # Initialise the angle and corners, lidar position is at center of box
    angle=np.full((4,2),0)
    corners = [[0,1,0],[1,1,0],[1,0,0],[0,0,0]]

    ## Find four corners
    corners[0][0] = item_position[0]                    # left-top point
    corners[0][1] = item_position[1] + item_dimension[1]
    corners[0][2] = item_position[2] + item_dimension[2]
    corners[1][0] = item_position[0] + item_dimension[0]# right-botton point
    corners[1][1] = item_position[1] + item_dimension[1]
    corners[1][2] = item_position[2] + item_dimension[2] 
    corners[2][0] = item_position[0] + item_dimension[0]# right-botton point
    corners[2][1] = item_position[1]
    corners[2][2] = item_position[2] + item_dimension[2]
    corners[3][0] = item_position[0]                    # left-botton point
    corners[3][1] = item_position[1]
    corners[3][2] = item_position[2] + item_dimension[2]
    # print(corners)

    for i in range(len(corners)):
        angle = calculate_angle(corners[i],i,angle)
    return angle

def calculate_angle(point,n,angle_matrix):
        
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



angle = angle_at_corners(item_dimension,item_position,box_dimension)
print(angle)