import csv
import sys
from Includes import objecttypes as obj
from Includes import boxes as box


# Functions to be used for .sort() key parameter later
# Function to get the volume of an input object for use with later sorting
def vol(entry):
    return entry.volume


# Function to return the type of the input object
def get_type(entry):
    return entry.type


with open('../Includes/items/itemList.csv', newline='') as csvfile:
    contents = csv.reader(csvfile, delimiter=',', quotechar='|')
    for line in contents:
        # array to store input items
        everything = []

        for i in line:
            # Compares content of csv file to dictionary containing all item names to create objects
            # print(obj.allItems[i.lower()]().name)
            try:
                everything.append(obj.allItems[i.lower()]())
            except KeyError:
                sys.stderr.write("Invalid item name")
                exit(1)

        # Sorts array in order from largest to smallest
        everything.sort(key=vol, reverse=True)
        for i in range(len(everything)):
            print(everything[i].name + ' ' + str(everything[i].volume))
        print("")
