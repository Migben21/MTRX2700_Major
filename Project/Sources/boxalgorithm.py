import csv
import sys
from Includes import objecttypes as obj
from Includes import boxes as box


# Functions to be used for .sort() key parameter later
# Returns the volume of an input object for use with later sorting
def vol(entry):
    return entry.volume


# Returns the type of the input object
def get_type(entry):
    return entry.type


# Goes through csv file containing items and calculates how many boxes are needed
# Returns array of boxes with what items are to be placed inside those boxes
def box_algorithm(filename):
    with open('../Includes/items/' + filename, newline='') as csvfile:
        contents = csv.reader(csvfile, delimiter=',', quotechar='|')
        for line in contents:
            # array to store input items
            itemList = []
            fragileItemList = []

            for i in line:
                # Compares content of csv file to dictionary containing all item names to create objects
                # print(obj.allItems[i.lower()]().name)
                try:
                    itemList.append(obj.allItems[i.lower()]())
                except KeyError:
                    sys.stderr.write("Invalid item name")
                    exit(1)

            # Sorts array in order from largest to smallest
            itemList.sort(key=vol, reverse=True)

            for i in range(len(itemList)):
                # print(itemList[i].name + ' ' + str(itemList[i].volume))
                if itemList[i].type == "f":
                    print('y')
                    fragileItemList.append(itemList[i])
            print("")


box_algorithm('itemList.csv')
