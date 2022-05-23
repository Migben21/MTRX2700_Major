from Source.Py_and_c_coms import Init_send_data
from Source.Tetris_state import tetris_init
#from Source import boxalgorithm 
#from Source import Lidar_angle 
#from Source import 3d_plot 
from Includes import boxes as box
from Includes import objecttypes as shopping

items = [shopping.Apples(), shopping.Bottles(), shopping.MilkCarton()]

small_box = box.SmallBox(items)

boxes = [small_box]

boxes_packed = tetris_init(boxes)

print(boxes_packed)

