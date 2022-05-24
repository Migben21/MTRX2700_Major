from difflib import diff_bytes
import numpy as np
import math

# Read data:
# item position
# item length, width, height
item_position = [4,0,0]
item_length = 20
item_width = 20
item_height = 15

# Define parameters
division = 5        # side length of each cube is 5cm
matrix = np.full((8,8),0)
Initial_distance = 5    # Initial distance between item position and (0,0) in each axis

# Use a for loop to place item one by one
# for i in range(len(data)): 

motor_z = 50   # Initial height for clamp is 50cm 
motor_x = 0         # Initial position of step motor in x axis is 0
motor_y = 0         # Initial position of step motor in y axis is 0
clamp_movedown = motor_z - item_height # The distance that clamp will move downwards

# 1.Clamp moves down and catch item
# void motormove(char z,int clamp_movedown)
hold_flag = 1       # hold_flag = 1 when clamp catches item
                    # hold_flag = 1 when clamp loosses item
# 2.Clamp moves up
# void motorback(char z,int clamp_movedown)

# 3. Move item to (0,0)
motor_x = motor_x + Initial_distance
motor_y = motor_y + Initial_distance
# void motormove(char x,int Initial_distance)
# void motormove(char y,int Initial_distance)

# 4.Move item to right place and loose it
cube_length = math.ceil(item_length / division)
cube_width = math.ceil(item_width / division)
cube_height = math.ceil(item_height / division)
print('length = ',cube_length,'   width = ',cube_width,'    height = ',cube_height)
motor_x = (item_position[0] - 0.5*cube_length)*division
motor_y = (item_position[1] + 0.5*cube_width)*division
motor_z = motor_z - item_height - matrix[item_position[0]+1][item_position[1]] * division
hold_flag = 0
print('x = ',motor_x,'   y = ',motor_y,'    z = ',motor_z)
# void motormove(char x,int motor_x)
# void motormove(char y,int motor_y)
# void motormove(char z,int motor_z)

# 5.Clamp return
# void motorback(char z,int motor_z)
# void motorback(char x,int motor_x)
# void motorback(char y,int motor_y)
# void motorback(char x,int Initial_distance)
# void motorback(char y,int Initial_distance)



