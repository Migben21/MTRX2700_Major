# The Problem
Inventory management is one of the most important processes for any businesses, perhaps even especially more for Grocery Stores. To help them manage this, it'd be great to have an automated system for this process, preventing stockouts, excess inventory, and less unsold products. 

# Our solution
In order to deal with this issue, our group wanted to create a state machine that sorts items on a conveyor belt and then places these items into boxes.

Python would be used mainly for code, and classes could be used for the different item types, their dimensions and even for box characteristics.

A LIDAR could be used to check if the items placed in the box are in the correct position, and the different classes would factor in if certain items were conditional (e.g. fragile items like eggs can only be placed in the top layer)

The States go from Idle -> Ready -> 'Tetris' <-> Placing -> Checking - > Idle -> Error.

A stepper motor can be used for just this scenario to act as the system's 'hand'. And a fixed height bewteen the grappler and conveyor belt, as well as another fixed distance between the LIDAR and box.

The system also works under the assumption that all items have been successfully identified for the sake of simplication. An identification module may be made if time allows for it.

# The breakdown and its modules

First Module is the Initialisation Module, which will check how many boxes are needed. The program has to read CSV Files, determine how many boxes are needed, as well as return an array with items ordered from largest to smallest with each array referencing a certain box, also stating its range. It must also consider other conditions (e.g. fragile items). This is currently being worked on by Michael.

Second Module is the Placement Analysis Module, which determines the most efficient way of placing objects. It takes in an order in which the objects placed are known. It then outputs an array ordered in the method of which the objects will be placed. A 3d Graph then displays where it should be in the box, the object is then placed in the box, a function stops this process from continuing until a command is inputted, which checks the space and then proceeds. This is currently being worked on by Stephen.

Third Module is the Placement Algorithm Module. It uses a 2D space to determine where to place the items. Z-axis order is irrelevant for this case, as choosing the area is the main focus. It should also do the boxes in the 3D space, possibly giving a 3D representation of where the boxes will go (likely using MatplotLib). This is being worked on by Yingjie.

The Last but also arguably one that would operate before the first, is the LIDAR sensor itself. This module concerns more of the hardware and operating the LIDAR to scan objects inside boxes and determine from their distances to the sensor how the box is already filled up or possibly empty. It also has to transfer the microcontroller's C data into readable data for the Python programs. This module is being worked on by Aditya and Miguel.

There are also a number of optional things we'd like to add if we have the time but are dependent:
- Machine beeping when complete and sends message to LCD, also notifying the Python console
    - Double beep for errors
    - Print a code for the error (ID for every error)
- Identification Module