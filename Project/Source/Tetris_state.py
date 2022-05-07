from msilib.schema import Error
import numpy as np
import matplotlib as mp
from sympy import Point, Point3D, true
from Includes import boxes as box

class item_organised:
    def __init__(self):
        self.name = ""
        self.point = [0,0,0]
        self.length = 0
        self.width = 0
        self.depth = 0

def tetris_init(box_objs):
    #determine amount of boxes and set to array
    for b in range(box_objs): #set to change

        #box data
        box = box_objs[b]
        dimentions = [box.width/5, box.length/5, box.height/5 ]

        #Make 3D matrix for each box
        box_matrix = []

        for i in range(dimentions[0]):
           box_matrix.append([])

           for j in range(dimentions[1]):
                box_matrix[i].append([])

                for k in range(dimentions[2]):
                   box_matrix[i][j].append([])

        #begin organising objects in the box
        box_pos_data = tetris_main(box_matrix, box.conents, dimentions)
    


def tetris_main(box_matrix, contents, dimentions):
    item_pos_data = []

    for i in range(contents):
        obj_dataframe = ["",[0,0,0],[0,0,0],[0,0,0],0] #[name, (point_x, point_y, point_z), (length, width, hight), (rotation x_axis, rotation y_axis rotation z_axis)]

    #set name and length, width and hight  

    #snaking algorithm for each item in the box
        for z in range(0, dimentions[0]+1):
           for y in range(0, dimentions[1]+1):
                for x in range(0, dimentions[2]+1):
                    space_check(box_matrix, obj_dataframe) #double check that obj_dataframe and box_matrix can be sent back and forth 
                    
                    if obj_dataframe[4] == 1:
                        item_pos_data.append(obj_dataframe)
                        break
                    if obj_dataframe[4] == -1:
                        return Error





                    

                   



##to be used later

def tetris_place_item():

def tetris_item_coordinates():

def orientation_test():

