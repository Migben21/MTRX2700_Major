import sys
from tabnanny import check
import numpy as np
import matplotlib as mp


class item_organised:
    def __init__(self):
        self.name = ""
        self.point = [0,0,0]
        self.dimensions = [0,0,0]
        self.rotations = [0,0,0]
        self.type = "N" # 'N' for normal, 'O' requires strict orientation, default normal

def tetris_init(box_objs):
    #boxes packed with required information, each element references a box, in each box contain the items in order of placement 
    boxes_packed = []
    item_pos_data = []

    #determine amount of boxes and set to array
    for b in range(len(box_objs)): #set to change

        print("BOX", b, " Type:", box_objs[b].size)

        dimensions = [box_objs[b].width, box_objs[b].length, box_objs[b].height]

        #Make 3D matrix for each box
        box_matrix = []
        
        #using 'o' to represent avalible space and 'x' to represent used space 
        for i in range(dimensions[0]):
           box_matrix.append([])

           for j in range(dimensions[1]):
                box_matrix[i].append([])

                for k in range(dimensions[2]):
                   box_matrix[i][j].append(0)

        #begin organising objects in the box
        item_pos_data = tetris_main(box_matrix, box_objs[b].contents, dimensions)
        
        #engaging user if their is a problem
        for i in range(len(item_pos_data)-1):
            if item_pos_data[i] == "ERROR":
                print("ERROR FOUND")
                plan = input("Do you wish to Continue? (Y or N) ")
                if plan == "Y":
                    del item_pos_data[i]
                elif plan == "N":
                    return
                else:
                    continue

        #item_pos_data = organise_items(item_pos_data)
        boxes_packed.append(item_pos_data)    
        print("-------------")
    return boxes_packed


def tetris_main(box_matrix, contents, dimensions):
    item_pos_data = []

    for i in range(len(contents)):
        obj_dataframe = item_organised() #[name, (point_x, point_y, point_z), (length, width, hight), (rotation x_axis, rotation y_axis rotation z_axis)]

        #set name and length, width and hight (due to change depending on the method of item data strcture)
        obj_dataframe.name = contents[i].name  
        obj_dataframe.dimensions = [contents[i].width, contents[i].height, contents[i].length]
        obj_dataframe.type = contents[i].type

        item_pos_data.append(snaking_sub_alg(dimensions, box_matrix, obj_dataframe))
        obj_dataframe = 0
    
    return item_pos_data

def snaking_sub_alg(dimensions, box_matrix, obj_dataframe):
    #snaking algorithm for each item in the box
    for z in range(0, dimensions[0]+1):
        for y in range(0, dimensions[1]+1):
            for x in range(0, dimensions[2]+1):
                current_pos = [x,y,z]
                n = 0
                
                check = space_check_init(box_matrix, obj_dataframe,dimensions,current_pos, n) #double check that obj_dataframe and box_matrix can be sent back and forth 

                if check == 1:
                    #set data into memory of pace and point 
                    box_matrix = item_filler(box_matrix, obj_dataframe, current_pos) 
                    obj_dataframe.point = current_pos

                    #output for testing
                    print("---------------------")
                    print(obj_dataframe.name)
                    print(obj_dataframe.point, " Point")
                    print(obj_dataframe.dimensions ," OG DIM")
                    print("Cont...")
                    return obj_dataframe
    print("Failed ", obj_dataframe.name)
    return ("ERROR")


def space_check_init(box_matrix, obj_dataframe, dimensions, current_pos, n):
    #check the verticies of the box are not interfearing with another box 
    original_dimensions = obj_dataframe.dimensions
    #original_pos = obj_dataframe.rotations

    #recuring function to check different orientations if the object allows it
    if obj_dataframe.type == 'N' and n < 5:
        obj_dataframe = rotate_object(obj_dataframe, n)

        check = space_check(box_matrix, obj_dataframe, dimensions, current_pos)

        if check == 0:
            obj_dataframe.dimensions = original_dimensions 
            #obj_dataframe.rotations = original_pos 

            n = n + 1
    else:
        check = space_check(box_matrix, obj_dataframe, dimensions,current_pos)
    
    #returning set
    return check
    

def space_check(box_matrix, obj_dataframe, dimensions, current_pos):
    #print("checking", current_pos)
    #ensure that the values to do not exceed the matrix index boundries 
    if obj_dataframe.dimensions[0] + current_pos[0] <= dimensions[0] and obj_dataframe.dimensions[1] + current_pos[1] <= dimensions[1] and obj_dataframe.dimensions[2] + current_pos[2] <= dimensions[2]:
    #check all verticies of the box are not colliding with others
        #print("within RANGE")
        if box_matrix[current_pos[0]][current_pos[1]][current_pos[2]] == 0 : #checking current point (O)
                if box_matrix[current_pos[0]][obj_dataframe.dimensions[1] + current_pos[1]][current_pos[2]] == 0 : # checking length from current point vertex (L)
                    if box_matrix[current_pos[0]][current_pos[1]][obj_dataframe.dimensions[2] + current_pos[2]] == 0: #checking height from current point vertex (
                        if box_matrix[current_pos[0]][obj_dataframe.dimensions[1] + current_pos[1]][obj_dataframe.dimensions[2] + current_pos[2]] == 0 : #checking (H+L
                            if box_matrix[obj_dataframe.dimensions[0] + current_pos[0]][obj_dataframe.dimensions[1] + current_pos[1]][current_pos[2]] == 0 : # checking (W+L)
                                if box_matrix[obj_dataframe.dimensions[0] + current_pos[0]][obj_dataframe.dimensions[1] + current_pos[1]][obj_dataframe.dimensions[2] + current_pos[2]] == 0: #checking (H+L+W)
                                    #print("WITHIN SPACE")
                                    return 1
    return 0

#check different roations of the object 
def rotate_object(obj_dataframe, n):
    if n == 0:
        return obj_dataframe
    if n == 1:
        obj_dataframe.dimensions[0], obj_dataframe.dimensions[1] = obj_dataframe.dimensions[1], obj_dataframe.dimensions[0]
    if n == 2: 
        obj_dataframe.dimensions[0], obj_dataframe.dimensions[2] = obj_dataframe.dimensions[2], obj_dataframe.dimensions[0]
    if n == 3:
        obj_dataframe.dimensions[2], obj_dataframe.dimensions[1] = obj_dataframe.dimensions[1], obj_dataframe.dimensions[2]
    if n == 4:
        obj_dataframe.dimensions[2], obj_dataframe.dimensions[1] = obj_dataframe.dimensions[1], obj_dataframe.dimensions[2]
        obj_dataframe.dimensions[0], obj_dataframe.dimensions[1] = obj_dataframe.dimensions[1], obj_dataframe.dimensions[0]
    


def item_filler(box_matrix, obj_dataframe, current_pos):
    for i in range(0, obj_dataframe.dimensions[2] + 1):
           for j in range(0, obj_dataframe.dimensions[1] + 1):
                for k in range(0, obj_dataframe.dimensions[0] + 1):
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
