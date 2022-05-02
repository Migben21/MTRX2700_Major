import numpy as np
import matplotlib as mp
from Includes import boxes as box

def tetris_init(items_multi):
    #determine amount of boxes and set to array
    for b in range(items_multi): #set to change

        items = items_multi[b]

        #array of boxes in line with items 
        x,y,z = 0
        boxes = [box.SmallBox, box.MediumBox, box.LargeBox]
        #compare name of box with the first element in the items array to generate first box to be created

        for i in range(1,4):
            if items[0] == i:
                y = boxes[i].length
                x = boxes[i].width
                z = boxes[i].height
                break

        #Make 3D matrix for each box
        box_matrix = []

        for i in range(x/5):
           box_matrix.append([])

           for j in range(y/5):
                box_matrix[i].append([])

                for k in range(z/5):
                   box_matrix[i][j].append([])





##to be used later
def tetris_place_item():

def tetris_item_coordinates():

def move_y():

def move_x():

def move_z():

