
import numpy as np
import matplotlib.pyplot as plt

# Preset Values for each level (cm)
lvl_0 = 0
lvl_1 = 3
lvl_2 = 6
lvl_3 = 9

layer_1 = []
layer_2 = []
layer_3 = []

i = 0
while i < 9:
    layer_1.append(0)
    layer_2.append(0)
    layer_3.append(0)
    i+=1

print("Layer 1:", end = ' ') 
print(layer_1)
print("Layer 2:", end = ' ')
print(layer_2)
print("Layer 3:", end = ' ')
print(layer_3)

'''
def compareValue(value):
    #value = np.abs(value)  # This is only if you want it to take in integers
    
    if (value > lvl_3):
        closest_value = lvl_3

    elif (value > lvl_2):
        if value > ((lvl_2-lvl_1)/2):
        closest_value = lvl_2
        else:
        closest_value = lvl_3

    elif (value > lvl_1):
        gap = lvl_1 - lvl_0
        if value > ((lvl_1-lvl_0)/2):
        closest_value = lvl_1
        else:
        closest_value = lvl_2
        
    elif (value > lvl_0):
        if value > ((lvl_1-lvl_0)/2):
        closest_value = lvl_0
        else:
        closest_value = lvl_1

    else:
        print("Invalid value.")
    
    return closest_value
'''



'''
# Creating Layer Arrays
no_of_layers = 3
area = 9
i = 1
layer_ = [] # Multiple dimension array; an array that will contain the layer arrays
while i <= no_of_layers:
    layer_[i] = [] # Creates an array for each layer

    j = 0
    while j < area:
        layer_[i].append(0)
        j+=1

    i+=1

i = 0
while i <= no_of_layers:
    print("Layer:", end = ' ')
    print(layer_[i])
    i+=1
'''

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