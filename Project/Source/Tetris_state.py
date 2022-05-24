import sys
from tabnanny import check
import numpy as np
import matplotlib as mp


class item_organised:
    def __init__(self):
        self.name = ""
        self.point = [0,0,0]
        self.dimentions = [0,0,0]
        self.rotations = [0,0,0]
        self.type = "N" # 'N' for normal, 'O' requires strict orientation, default normal

def tetris_init(box_objs):
    #boxes packed with required information, each element references a box, in each box contain the items in order of placement 
    boxes_packed = []
    item_pos_data = []

    #determine amount of boxes and set to array
    for b in range(len(box_objs)): #set to change

        dimentions = [box_objs[b].width, box_objs[b].length, box_objs[b].depth]

        #Make 3D matrix for each box
        box_matrix = []
        
        #using 'o' to represent avalible space and 'x' to represent used space 
        for i in range(dimentions[0]):
           box_matrix.append([])

           for j in range(dimentions[1]):
                box_matrix[i].append([])

                for k in range(dimentions[2]):
                   box_matrix[i][j].append(0)

        #begin organising objects in the box
        item_pos_data.append(tetris_main(box_matrix, box_objs[b].contents, dimentions))
        
        if(item_pos_data == "Error"):
            #call function of error
            return 
        
        item_pos_data = organise_items(item_pos_data)
        boxes_packed.append(item_pos_data)    
    return boxes_packed


def tetris_main(box_matrix, contents, dimentions):
    item_pos_data = []

    for i in range(len(contents)):
        obj_dataframe = item_organised() #[name, (point_x, point_y, point_z), (length, width, hight), (rotation x_axis, rotation y_axis rotation z_axis)]

        #set name and length, width and hight (due to change depending on the method of item data strcture)
        obj_dataframe.name = contents[i].name  
        obj_dataframe.dimentions = [contents[i].width, contents[i].height, contents[i].length]
        obj_dataframe.type = contents[i].type

        item_pos_data.append(snaking_sub_alg(dimentions, box_matrix, obj_dataframe))
        obj_dataframe = 0
    
    return item_pos_data

def snaking_sub_alg(dimentions, box_matrix, obj_dataframe):
    #snaking algorithm for each item in the box
    for z in range(0, dimentions[0]+1):
        for y in range(0, dimentions[1]+1):
            for x in range(0, dimentions[2]+1):
                current_pos = [x,y,z]
                n = 0
                
                check = space_check_init(box_matrix, obj_dataframe,dimentions,current_pos, n) #double check that obj_dataframe and box_matrix can be sent back and forth 

                if check == 1:
                    #set data into memory of pace and point 
                    box_matrix = item_filler(box_matrix, obj_dataframe, current_pos) 
                    obj_dataframe.point = current_pos

                    #output for testing
                    print("---------------------")
                    print(obj_dataframe.name)
                    print(obj_dataframe.point, " Point")
                    print(obj_dataframe.dimentions ," OG DIM")
                    print("Cont...")
                    return obj_dataframe
    print("Failed")
    return ("ERROR")


def space_check_init(box_matrix, obj_dataframe, dimentions, current_pos, n):
    #check the verticies of the box are not interfearing with another box 
    original_dimentions = obj_dataframe.dimentions
    #original_pos = obj_dataframe.rotations

    #recuring function to check different orientations if the object allows it
    if obj_dataframe.type == 'N' and n < 5:
        obj_dataframe = rotate_object(obj_dataframe, n)

        check = space_check(box_matrix, obj_dataframe, dimentions, current_pos)

        if check == 0:
            obj_dataframe.dimentions = original_dimentions 
            #obj_dataframe.rotations = original_pos 

            n = n + 1
    else:
        check = space_check(box_matrix, obj_dataframe, dimentions,current_pos)
    
    #returning set
    return check
    

def space_check(box_matrix, obj_dataframe, dimentions, current_pos):
    #print("checking", current_pos)
    #ensure that the values to do not exceed the matrix index boundries 
    if obj_dataframe.dimentions[0] + current_pos[0] <= dimentions[0] and obj_dataframe.dimentions[1] + current_pos[1] <= dimentions[1] and obj_dataframe.dimentions[2] + current_pos[2] <= dimentions[2]:
    #check all verticies of the box are not colliding with others
        #print("within RANGE")
        if box_matrix[current_pos[0]][current_pos[1]][current_pos[2]] == 0 : #checking current point (O)
                if box_matrix[current_pos[0]][obj_dataframe.dimentions[1] + current_pos[1]][current_pos[2]] == 0 : # checking length from current point vertex (L)
                    if box_matrix[current_pos[0]][current_pos[1]][obj_dataframe.dimentions[2] + current_pos[2]] == 0: #checking height from current point vertex (
                        if box_matrix[current_pos[0]][obj_dataframe.dimentions[1] + current_pos[1]][obj_dataframe.dimentions[2] + current_pos[2]] == 0 : #checking (H+L
                            if box_matrix[obj_dataframe.dimentions[0] + current_pos[0]][obj_dataframe.dimentions[1] + current_pos[1]][current_pos[2]] == 0 : # checking (W+L)
                                if box_matrix[obj_dataframe.dimentions[0] + current_pos[0]][obj_dataframe.dimentions[1] + current_pos[1]][obj_dataframe.dimentions[2] + current_pos[2]] == 0: #checking (H+L+W)
                                    #print("WITHIN SPACE")
                                    return 1
    return 0

#check different roations of the object 
def rotate_object(obj_dataframe, n):
    if n == 0:
        return obj_dataframe
    if n == 1:
        obj_dataframe.dimentions[0], obj_dataframe.dimentions[1] = obj_dataframe.dimentions[1], obj_dataframe.dimentions[0]
    if n == 2: 
        obj_dataframe.dimentions[0], obj_dataframe.dimentions[2] = obj_dataframe.dimentions[2], obj_dataframe.dimentions[0]
    if n == 3:
        obj_dataframe.dimentions[2], obj_dataframe.dimentions[1] = obj_dataframe.dimentions[1], obj_dataframe.dimentions[2]
    if n == 4:
        obj_dataframe.dimentions[2], obj_dataframe.dimentions[1] = obj_dataframe.dimentions[1], obj_dataframe.dimentions[2]
        obj_dataframe.dimentions[0], obj_dataframe.dimentions[1] = obj_dataframe.dimentions[1], obj_dataframe.dimentions[0]
    


def item_filler(box_matrix, obj_dataframe, current_pos):
    for i in range(0, obj_dataframe.dimentions[2] + 1):
           for j in range(0, obj_dataframe.dimentions[1] + 1):
                for k in range(0, obj_dataframe.dimentions[0] + 1):
                    box_matrix[k + current_pos[0]][j+ current_pos[1]][i + current_pos[2]] = 1
                   
    return box_matrix


def organise_items(item_pos_data):
    #bubble sort the data
    n = len(item_pos_data)
    for a in range(n-1):
        for b in range(0, n-a-1):
            #sorts based on the value of the points z element of its position 
            if item_pos_data[b].point[2] > item_pos_data[b + 1].point[2] :
                item_pos_data[b], item_pos_data[b + 1] = item_pos_data[b + 1], item_pos_data[b]
    
    return item_pos_data
 





