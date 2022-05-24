from Sources.Py_and_c_coms import Init_send_data
from Sources.Tetris_state import tetris_init
from Sources.boxalgorithm import box_algorithm
from Sources.Lidar_angle import  
from Sources.3dplot import  
from Sources.Py_and_c_coms import Init_send_data
from Sources.Py_and_c_coms import waiting
from Includes import CSV 

#DATA PLAN
#   CSV --> BOXALGORITHM --> box data with items inside 
#   box data with items inside --> TETRISALGORITHM --> each box with item positions and dimentions inside 
#   each box with item positions and dimentions inside --> ORGANISE ITEMS/BOX ALGORITHM --> ITEM DATA + NUM OF ITEM 
#   ITEM DATA --> STEPPERPLACEMNT --> STEPPER MOTOR DATA XYZ
#   ITEM DATA --> LIDARANGLE --> ANGLE TO CHECK A1 and A2
#   NUM OF DATA + STEPPER MOTOR DATA XYZ + ANGLE TO CHECK A1 and A2 --> SEND DATA --> [FILE.TXT]
#   WAITING --> ORGANISE ITEMS/BOX ALGORITHM (REPEAT UNTIL ALL IS DONE THEN EXIT)

#initalise Data values
data_send = []
angles = []
stepper = []

#Order of Operation
box_data = box_algorithm(CSV)

box_pos_data = tetris_init(box_data)

for i in range(len(box_pos_data)):
    num_items = len(box_pos_data[i])
    for a in range(len(box_pos_data[i])):

        angles =  3dplot(box_pos_data[i][a])
        stepper = placment(box_pos_data[i][a]) 

        data_send.append(num_items)
        data_send.append(stepper)
        data_send.append(angles)

        Init_send_data(data_send)

        num_items = num_items - 1

        waiting()





