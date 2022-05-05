import numpy as np
import matplotlib as mp
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

        box = box_objs[b]

        #array of boxes in line with items 
        x = box.width
        y = box.length
        z = box.height

        #Make 3D matrix for each box
        box_matrix = []

        for i in range(x/5):
           box_matrix.append([])

           for j in range(y/5):
                box_matrix[i].append([])

                for k in range(z/5):
                   box_matrix[i][j].append([])

        #begin organising objects in the box
        tetris_main(box_matrix, box.conents)
    



##to be used later
def tetris_main(box_matrix, contents):

def tetris_place_item():

def tetris_item_coordinates():

def move_y_test():

def move_x_test():

def move_z_test():

def orientation_test():

