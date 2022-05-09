import numpy as np
import matplotlib as mp
from Includes import boxes as box

class item_organised:
    def __init__(self):
        self.name = ""
        self.point = [0,0,0]
        self.dimentions = [0,0,0]
        self.rotations = [0,0,0]

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
           box_matrix.append([o])

           for j in range(dimentions[1]):
                box_matrix[i].append([o])

                for k in range(dimentions[2]):
                   box_matrix[i][j].append([o])

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

    #snaking algorithm for each item in the box
        for z in range(0, dimentions[0]+1):
           for y in range(0, dimentions[1]+1):
                for x in range(0, dimentions[2]+1):
                    current_pos = [x,y,z]
                    box_matrix, obj_dataframe = space_check(box_matrix, obj_dataframe, current_pos) #double check that obj_dataframe and box_matrix can be sent back and forth 
                    
                    if obj_dataframe[4] == 1:
                        item_pos_data.append(obj_dataframe)
                        break
                    if obj_dataframe[4] == -1:
                        return "Error"
    return


def space_check(box_matrix, obj_dataframe, current_pos):
    check = 0

    #check the verticies 

    if check == 0:
        orientation_test(box_matrix, obj_dataframe, current_pos)
    
    return box_matrix, obj_dataframe

def organise_items(item_pos_data):
    #bubble sort the data
    n = len(item_pos_data)
    for a in range(n-1):
        for b in range(0, n-a-1):
            #sorts based on the value of the points z element of its position 
            if item_pos_data[b].point[2] > item_pos_data[b + 1].point[2] :
                item_pos_data[b], item_pos_data[b + 1] = item_pos_data[b + 1], item_pos_data[b]
    
    return item_pos_data
 

def orientation_test(box_matrix, obj_dataframe, current_pos):

