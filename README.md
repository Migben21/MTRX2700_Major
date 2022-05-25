# The Package Packer
## Controlled Universally Nextgen Tactical Systems
MTRX2700 Major project; Futuristic technology for supermarkets

Project Aim: To create a state machine that organises supermarket products from a conveyor belt.

# MTRX2700_G1_A2
## Introduction
This is Group A's work for the MTRX2700 Major Project.
Code as well as documentation are stored within this GitHub Repository.

# Instructions:
One simply writes a file with all the items they want, with each line in this file defining a new set of items. This file then has to be declared in main, and when the code is run, a set of data will be outputted & written into a file, 'data.txt'.

This data is sent to the C Component of our code, where it's manually fed in, and the system will check if the object, once placed, is in the right area, returning an error if it is not, and an update message if placed correctly.

# High Level Information about the Code:
This section is to describe the functions and how they're broken down into modules

# Python Modules:

## Box Algorithm / Initialisation
The function reads a CSV file, and determines how many boxes are needed. It then returns an array with each item ordered from largest to smallest with each array referencing a certain box, and also stating its range.

It must also consider other conditions (e.g. fragile items such as eggs).

Also initialises serial communication.

## 'Tetris' Algorithm
Determines the most efficient way of placing objects. This function takes in an order in which the objects placed are known, taking in a file with a list of items. It determines how many boxes are needed and which boxes they should go into. Checks are also conducted to make sure these objects will fit inside the boxes. It then outputs an array ordered in the method of which the objects should be placed. 

## Placement Algorithm
This module uses a 2D view of the space to determine where to place items. The z-axis is irrelevant for this as choosing the area is the main focus. It inputs box information, item dimensions and item position. It then turns this data into a 2D matrix. Distance is calculated in the x, y & z directions and data is sent to the step motors. To visualise this, a 3D Simulation is also conducted. A final matrix is sent to check the module.

# C Modules:

## LIDAR Sensor
The LIDAR Sensor is meant to check that items placed in the box are in the correct position. This module concerns more hardware and operating the LIDAR to scan objects inside boxes and determine from their distances to the sensor how the box is already filled up or possibly empty. It also has to communicate data between the C and Python Modules. It collects LIDAR data from each cubic point in the box and stores this into arrays. Code is run to check between 2 datasets, the current LIDAR array and the intended array, to see if any changes have been made. It outputs the distance between the sensor and the closest surface

## Stepper Motor
This module relates to the device's stepper motors, which were to be used in the placement of items (for this proof-of-concept presentation, there is no tangible stepper motor). It initialises the machine's stepper motors and would change between different states, taking in input from the device.

U, L & B are the ports connected to the stepper motors.

# Testing Procedures:
* CodeWarrior's IDE Debugger was the main method used to debug programs, easily indicating whether the program even compiled or ran as intended. Files couldd also be run step by step, and variables could be checked as they updated through each line.
* Any variables and their addresses could be easily viewed from the debugger, even at any step of debugging
* Different components & configurations could be used to suit debugging & visualisation needs

# Details about the Project:
Group Members: Aditya Bhambri, Michael Mei, Miguel Benatiro, Stephen Capar, Yingjie Mi

* Aditya Bhambri: Worked on LIDAR Sensor Module 

* Michael Mei: Worked on Box Algorithm & Initialisation Module, helped with GitHub merging and debugging code for other modules

* Miguel Benatiro: Assisted with LIDAR Sensor Module, Documentation; README & Minutes

* Stephen Capar: Worked on the 'Tetris' Algorithm, Stepper Motor Module, GitHub organisation

* Yingjie Mi: Worked on Placement Algorithm and an Angle of Object Position Algorithm (Which we ended up failing to integrate)