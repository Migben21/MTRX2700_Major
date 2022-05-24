from Includes.Py_and_c_coms import Init_send_data
from Includes.Tetris_state import tetris_init
from Includes.boxalgorithm import box_algorithm
from Includes.Lidar_angle import  point_check_init
from Includes.plot_3D import plot_3d
from Includes.step_motor_movment import calculate_step
from Includes.Py_and_c_coms import Init_send_data
from Includes.Py_and_c_coms import waiting
from Includes.plot_3D import Initialised_matrix

#DATA PLAN
#   CSV --> BOXALGORITHM --> box data with items inside 
#   box data with items inside --> TETRISALGORITHM --> each box with item positions and dimentions inside 
#   each box with item positions and dimentions inside --> ORGANISE ITEMS/BOX ALGORITHM --> ITEM DATA + NUM OF ITEM 
#   ITEM DATA --> STEPPERPLACEMNT --> STEPPER MOTOR DATA XYZ
#   ITEM DATA --> LIDARANGLE --> ANGLE TO CHECK A1 and A2
#   NUM OF DATA + STEPPER MOTOR DATA XYZ + ANGLE TO CHECK A1 and A2 --> SEND DATA --> [FILE.TXT]
#   WAITING --> ORGANISE ITEMS/BOX ALGORITHM (REPEAT UNTIL ALL IS DONE THEN EXIT)

#initalise Data values
angles = []
stepper = []
box_sizes = []

#Item list Catagorys
path = "Project/Includes/items/"
filename_list = ["bigTest.csv", "invalidItemList.csv", "itemList.csv", "LockMartTM.csv", "oneLine.csv", "sideTooBig.csv"]
Pick_items_list = 2 #put in number 0 - 5 for each list based on 'filename_list' order

#---------------Order of Operation------------------

#Organising items into boxes
box_data = box_algorithm(path + filename_list[Pick_items_list])

#Gathering an Array of the boxes sizes in order
for c in range(len(box_data)):
    box_sizes.append(box_data[c].size)

#Performing tetris algorithm to find placment of items in their boxes 
box_pos_data = tetris_init(box_data)

#Preparing data for Input into C
for i in range(len(box_pos_data)):
    num_items = len(box_pos_data[i])
    box_matrix = Initialised_matrix(box_sizes[i])
    for a in range(num_items):
        data_send = []
        item = box_pos_data[i][a]

        print(item)

        check_point =  point_check_init(item,box_sizes[i])
        stepper = calculate_step(box_sizes[i],item) 

        #plot_3d(box_sizes[i],box_pos_data[i][a],box_matrix)

        data_send.append(num_items)

        for c in range(0,3):
            data_send.append(int(stepper[c]))
        for c in range(0,3):
            data_send.append(check_point[c])

        print(data_send)
        print("-----------")

        Init_send_data(data_send)

        num_items = num_items - 1

        waiting()





