import matplotlib.pyplot as plt
import numpy as np


matrix = np.arange(16)#.reshape(4,4)

fig = plt.figure()
ax = fig.gca(projection='3d')
x = [1,2,3,4]
y = [1,2,3,4]
z = matrix
# z = np.random.randint(0, 1000, 16)
print(matrix)
print(z)

xx,yy = np.meshgrid(x,y)
x, y = xx.ravel(), yy.ravel()

height = np.zeros_like(z)
width = depth = 1

ax.bar3d(x, y, height, width, depth, z,  color='b', zsort='average')  # width, depth, height
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()