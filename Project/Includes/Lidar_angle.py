import numpy as np
import math


def point_check_init(item,box_type): #main function
    # Initialise the angle and corners, lidar position is at center of box
    num_points = 3
    box_dimension = box_cal(box_type)
    check_point = []

    for i in range(0,3):
        x = (box_dimension[i]/num_points)
        y = (item.point[i]) + (box_dimension[i]/2)
        check_point.append(round(y/x))

    return check_point

def box_cal(box_type):
    if box_type == 's':
        box_dimension = [40,40,40]
    elif box_type == 'm':
        box_dimension = [75,75,40]
    elif box_type == 'l':
        box_dimension = [100,100,40]
    return box_dimension


# test
# angle = angle_at_corners(item,box_type)
# print(angle)