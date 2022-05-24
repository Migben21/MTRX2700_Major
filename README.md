# Controlled Universally Nextgen Tactical Systems
MTRX2700 Major project; Futuristic technology for supermarkets

Project Aim: To create a state machine that organises supermarket products from a conveyor belt.

# MTRX2700_G1_A2
## Introduction
This is Group A's work for the MTRX2700 Major Project.
Code as well as documentation are stored within this GitHub Repository.

# Instructions:

## Operating the State Machine:


# High Level Information about the Code:
This section is to describe the functions and how they're broken down into modules

## State Machine States:
1: Idle
2: Initialise
3: 'Tetris'
4: Placement
5: Checking
6: Outputting 3D Representation

## Module 1: Initialisation / Box Algorithm / Initialising Serial
The function reads a CSV file, and determines how many boxes are needed. It then returns an array with each item ordered from largest to smallest with each array referencing a certain box, and also stating its range.

It must also consider other conditions (e.g. fragile items such as eggs).

## Module 2: Tetris
Determines the most efficient way of placing objects. This function takes in an order in which the objects placed are known. It then outputs an array ordered in the method of which the objects should be placed. 

A 3D Graph is also shown that displays where it's meant to be in the box.

The function stops this process constantly until a command is inputted, which checks the space and then proceeds in an endless loop, constantly updating after each command.

## Module 3: Placement Algorithm
This module uses a 2D view of the space to determine where to place items. The z-axis is irrelevant for this as choosing the area is the main focus.  It should also do the boxes in the 3D space, possibly giving a 3D representation of where the boxes will go (likely using MatplotLib).

## Module 4: LIDAR Sensor
This module concerns more hardware and operating the LIDAR to scan objects inside boxes and determine from their distances to the sensor how the box is already filled up or possibly empty. It also has to transfer the microcontroller's C data into readable data for the Python programs. 

# Testing Procedures:
* 

# Details about the Project:
Group Members: Aditya Bhambri, Michael Mei, Miguel Bentiro, Stephen Capar, Yingjie Mi
