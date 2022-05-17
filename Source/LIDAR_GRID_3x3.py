
import numpy as np
import matplotlib.pyplot as plt

# Preset Values for each level (cm)
lvl_0 = 0
lvl_1 = 3
lvl_2 = 6
lvl_3 = 9

def compareValue(value):
    value = np.abs(value)
    if (value > lvl_0):
        gap = lvl_1 - lvl_0
        value - gap/2
        closest_value = lvl_0

    elif (value > lvl_1):
        gap = lvl_2 - lvl_1
        closest_value = lvl_1

    elif (value > lvl_2):
        gap = lvl_2 - lvl_3
        closest_value = lvl_2

    elif (value > lvl_3):
        gap = lvl_2 - lvl_3
        closest_value = lvl_3

    else:
        print("Invalid value.")
    
    return closest_value

# 1 Array for each layer?
layer_1 = []


'''
def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

array = np.random.random(10)
print(array)

value = 0.5
print(find_nearest(array, value))

'''