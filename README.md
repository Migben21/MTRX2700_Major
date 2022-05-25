# Controlled Universally Nextgen Tactical Systems
MTRX2700 Major project; Futuristic technology for supermarkets

Project Aim: To create a state machine that organises supermarket products from a conveyor belt.

# MTRX2700_G1_A2
## Introduction
This is Group A's work for the MTRX2700 Major Project.
Code as well as documentation are stored within this GitHub Repository.

# Instructions:
One simply writes a file with all the itemss thhey want
Each new line defines a new set of items

Declare the file in main

Run the code


it will output a set of data and write it to data.txt

This data is to be sent to the C Component of our code

It's then manually fed in

The system will then be checking if that object once placed is in the right area, and will return an error if it is not.


## Operating the State Machine:


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

# C Modules

## LIDAR Sensor
The LIDAR Sensor is meant to check that items placed in the box are in the correct position. This module concerns more hardware and operating the LIDAR to scan objects inside boxes and determine from their distances to the sensor how the box is already filled up or possibly empty. It also has to communicate data between the C and Python Modules. It collects LIDAR data from each cubic point in the box and stores this into arrays. Code is run to check between 2 datasets, the current LIDAR array and the intended array, to see if any changes have been made. It outputs the distance between the sensor and the closest surface

# Testing Procedures:
* CodeWarrior's IDE Debugger was the main method used to debug programs, easily indicating whether the program even compiled or ran as intended. Files couldd also be run step by step, and variables could be checked as they updated through each line.
* Any variables and their addresses could be easily viewed from the debugger, even at any step of debugging
* Different components & configurations could be used to suit debugging & visualisation needs

# Details about the Project:
Group Members: Aditya Bhambri, Michael Mei, Miguel Benatiro, Stephen Capar, Yingjie Mi

* Aditya Bhambri: Worked on

* Michael Mei:

* Miguel Benatiro:

* Stephen Capar:

* Yingjie Mi: