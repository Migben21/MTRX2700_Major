import csv
import sys
from Includes import objecttypes as obj
from Includes import boxes as box


# Opens csv file and reads what items need to be sorted and parses them into determine_boxes()
# Returns array of boxes with objects to be placed inside
def box_algorithm(filename):
    boxes = []
    with open(filename, newline='') as csvfile:
        contents = csv.reader(csvfile, delimiter=',', quotechar='|')
        for line in contents:
            # array to store items
            itemList = []
            fragileItemList = []
            for i in line:
                # Remove spaces from input
                i = i.translate({ord(' '): None for j in ' '})
                # Compares content of csv file to dictionary containing all item names to create objects
                try:
                    itemList.append(obj.allItems[i.lower()]())
                except KeyError:
                    return 1  # Invalid item name found in contents
            # Sorts array in order from largest to smallest
            itemList.sort(key=vol, reverse=True)
            # Separates fragile items into their own list and removes them from the normal item list
            for i in range(len(itemList)):
                if itemList[i].type == "F":
                    fragileItemList.append(itemList[i])
            for i in range(len(fragileItemList)):
                itemList.remove(fragileItemList[i])
            normalItems = determine_boxes(itemList)
            fragileItems = determine_boxes(fragileItemList)
            for i in range(len(normalItems)):
                if normalItems[i].contentsVolume:
                    boxes.append(normalItems[i])
            for i in range(len(fragileItems)):
                if fragileItems[i].contentsVolume:
                    boxes.append(fragileItems[i])
    return boxes


# Functions to be used for .sort() key parameter
# Returns the volume of an input object for use with later sorting
def vol(entry):
    return entry.volume


# Returns the type of the input object
def get_type(entry):
    return entry.type


# Returns the size of the smallest side of a rotatable object
def smallest_side(entry):
    if entry.type != 'F':
        dimensions = [int(entry.height), int(entry.width), int(entry.length)]
        smallest = sorted(dimensions)[0]
        return smallest
    else:
        return entry.height


# Returns the largest side of an object
def largest_side(entry):
    dimensions = [int(entry.height), int(entry.width), int(entry.length)]
    largest = sorted(dimensions)[2]
    return largest


# Checks the dimensions of an input item and checks if the largest side of an item is larger than the size of a box
# Returns 0 if item won't fit in box, or 1 if it can
def side_check(items, side):
    if largest_side(items) > side:
        return 0
    else:
        return 1


# Function to determine the amount of and size of boxes needed for a list of items
def determine_boxes(items):
    boxes = []
    scannedItems = []
    totalVolume = 0
    check = 0
    for i in range(len(items)):
        totalVolume += items[i].volume
        scannedItems.append(items[i])
        if totalVolume >= 100 * 100 * 40:  # Volume of large box
            if len(scannedItems) == 1:
                return 2  # Item too large for any box
            elif totalVolume != 0:
                scannedItems.pop(len(scannedItems)-1)
                boxes.append(box.LargeBox(scannedItems))
                scannedItems = [items[i]]
                totalVolume = 0
    if totalVolume > (40 * 40 * 40):
        if totalVolume > (75 * 75 * 40):
            boxes.append(box.LargeBox(scannedItems))
        else:
            for i in range(len(scannedItems)):
                check = side_check(scannedItems[i], 75)
            if check:
                boxes.append(box.MediumBox(scannedItems))
            else:
                boxes.append(box.LargeBox(scannedItems))
    else:
        for i in range(len(scannedItems)):
            check = side_check(scannedItems[i], 40)
        if check:
            boxes.append(box.SmallBox(scannedItems))
        else:
            for i in range(len(scannedItems)):
                check = side_check(scannedItems[i], 75)
            if check:
                boxes.append(box.MediumBox(scannedItems))
            else:
                boxes.append(box.LargeBox(scannedItems))
    return boxes
