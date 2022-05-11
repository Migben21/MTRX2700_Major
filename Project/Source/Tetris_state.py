import numpy as np
import matplotlib as mp
from Includes import boxes as box

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

    #determine amount of boxes and set to array
    for b in range(box_objs): #set to change

        #box data
        box = box_objs[b]
        dimentions = [box.width/5, box.length/5, box.height/5 ]

        #Make 3D matrix for each box
        box_matrix = []
        
        #using 'o' to represent avalible space and 'x' to represent used space 
        for i in range(dimentions[0]):
           box_matrix.append(0)

           for j in range(dimentions[1]):
                box_matrix[i].append(0)

                for k in range(dimentions[2]):
                   box_matrix[i][j].append(0)

        #begin organising objects in the box
        item_pos_data = tetris_main(box_matrix, box.conents, dimentions)
        
        if(item_pos_data == "Error"):
            #call function of error
            return 
        item_pos_data = organise_items(item_pos_data)
        boxes_packed.append(item_pos_data)
    
    

    return


def tetris_main(box_matrix, contents, dimentions):
    item_pos_data = []

    for i in range(contents):
        obj_dataframe = item_organised #[name, (point_x, point_y, point_z), (length, width, hight), (rotation x_axis, rotation y_axis rotation z_axis)]

    #set name and length, width and hight (due to change depending on the method of item data strcture)
        obj_dataframe.name = contents[i].name  
        obj_dataframe.dimentions = contents[i].dimentions 
        obj_dataframe.type = contents[i].type

    #snaking algorithm for each item in the box
        for z in range(0, dimentions[0]+1):
           for y in range(0, dimentions[1]+1):
                for x in range(0, dimentions[2]+1):
                    current_pos = [x,y,z]
                    box_matrix, obj_dataframe = space_check_init(box_matrix, obj_dataframe, current_pos) #double check that obj_dataframe and box_matrix can be sent back and forth 
                    
                    if obj_dataframe != 0:
                        item_pos_data.append(obj_dataframe)
                        break
                    else:
                        return "ERROR"
    return item_pos_data


def space_check_init(box_matrix, obj_dataframe, current_pos,n):
    #check the verticies of the box are not interfearing with another box 
    check = space_check(box_matrix, obj_dataframe, current_pos)

    #recuring function to check different orientations if the object allows it
    if check == 0 and obj_dataframe.type == 'N':
        n = n + 1
        #rotate x-axis -90 and 90 degrees
        #rotate y-axis -90 and 90 degrees
        #rotate z-axis -90 and 90 degrees
        space_check_init(box_matrix, obj_dataframe, current_pos,n)
    
    #returning set
    if check == 0:
        return box_matrix, 0
    else:
        box_matrix = item_filler(box_matrix, obj_dataframe, current_pos)
        return box_matrix, obj_dataframe
    

def space_check(box_matrix, obj_dataframe, current_pos):
    if box_matrix[current_pos[0]][current_pos[1]][current_pos[2]] == 0 : #checking current point (O)
        if box_matrix[obj_dataframe.dimentions[0] + current_pos[0]][current_pos[1]][current_pos[2]] == 0 : #checking width from current point vertex (W)
            if box_matrix[current_pos[0]][obj_dataframe.dimentions[1] + current_pos[1]][current_pos[2]] == 0 : # checking length from current point vertex (L)
                if box_matrix[current_pos[0]][current_pos[1]][obj_dataframe.dimentions[2] + current_pos[2]] == 0: #checking height from current point vertex (H)
                    if box_matrix[current_pos[0]][obj_dataframe.dimentions[1] + current_pos[1]][obj_dataframe.dimentions[2] + current_pos[2]] == 0 : #checking (H+L)
                        if box_matrix[obj_dataframe.dimentions[0] + current_pos[0]][obj_dataframe.dimentions[1] + current_pos[1]][current_pos[2]] == 0 : # checking (W+L)
                            if box_matrix[obj_dataframe.dimentions[0] + current_pos[0]][obj_dataframe.dimentions[1] + current_pos[1]][obj_dataframe.dimentions[2] + current_pos[2]] == 0: #checking (H+L+W)
                                return 1
    return 0

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
 



