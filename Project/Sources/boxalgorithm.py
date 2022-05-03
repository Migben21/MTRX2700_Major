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


# Function to determine the amount of and size of boxes needed for a list of items
def determine_boxes(items):
    boxes = []
    scannedItems = []
    totalVolume = 0

    for i in range(len(items)):
        totalVolume += items[i].volume
        scannedItems.append(items[i])

        if totalVolume >= 100 * 100 * 40:  # Volume of large box
            if len(scannedItems):
                sys.stderr.write("Item too large to fit in a box")
                exit(2)  # Item too large for any box
            else:
                scannedItems.pop(len(scannedItems)-1)
                boxes.append(box.LargeBox(scannedItems))
                scannedItems = []
                totalVolume = 0
                i -= 1

    if (40 ^ 3) - totalVolume < 0:
        if (75 * 75 * 40) - totalVolume < 0:
            boxes.append(box.LargeBox(scannedItems))
        else:
            boxes.append(box.MediumBox(scannedItems))
    else:
        boxes.append(box.SmallBox(scannedItems))

    return boxes


# Goes through csv file to read what items need to be sorted and parses them into determine_boxes()
# Returns array of boxes with objects to be placed inside
def box_algorithm(filename):
    boxes = []
    with open('../Includes/items/' + filename, newline='') as csvfile:
        contents = csv.reader(csvfile, delimiter=',', quotechar='|')
        for line in contents:
            # array to store items
            itemList = []
            fragileItemList = []

            for i in line:
                # Compares content of csv file to dictionary containing all item names to create objects
                try:
                    itemList.append(obj.allItems[i.lower()]())
                except KeyError:
                    sys.stderr.write("Invalid item name")
                    exit(1)  # Invalid item name found in contents

            # Sorts array in order from largest to smallest
            itemList.sort(key=vol, reverse=True)

            # Separates fragile items into their own list and removes them from the normal item list
            for i in range(len(itemList)):
                if itemList[i].type == "f":
                    fragileItemList.append(itemList[i])

            for i in range(len(fragileItemList)):
                itemList.remove(fragileItemList[i])

            normalItems = determine_boxes(itemList)
            fragileItems = determine_boxes(fragileItemList)

            for i in range(len(normalItems)):
                boxes.append(normalItems[i])
            for i in range(len(fragileItems)):
                boxes.append(fragileItems[i])

    return boxes
