""" 
To build a plot and compare to given data after using LIDAR

For now:
- Create an empty 3D Grid, which can be fed with data of basically 1 or 0 at each point of the xyz axis
- 0 is empty space, whilst 1 is taken
- For now, create a 3D Space of 50x50x50 cm (which can be changed later on, also going with cubic rather than rectangular box for now)
"""

import numpy as np
import matplotlib.pyplot as plt

#empty_array = np.empty((2,3,3))
#print(empty_array)

# Making an array for each axis
i = 0
x = []
y = []
z = []

while i < 50:
    x.append(1)
    y.append(1)
    z.append(1)
    i+=1

box_space = [x, y, z]

# Showing axis and their status
print("x-axis:", end = ' ')
print(box_space[0])
print("y-axis:", end = ' ')
print(box_space[1])
print("z-axis:", end = ' ')
print(box_space[2])

fig = plt.figure()
ax = plt.axes(projection = '3d')

# Still figuring out how to display a 3D map of the empty and non-empty spaces
#ax.scatter3D(x, y, z, color = "red")
ax.scatter3D(box_space[0], box_space[1], box_space[2], color = "red")

plt.title("Taken up spaces.")
plt.show()