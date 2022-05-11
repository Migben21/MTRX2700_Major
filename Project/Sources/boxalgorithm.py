import csv
import sys
from Includes import objecttypes as obj
from Includes import boxes as box


# Opens csv file and reads what items need to be sorted and parses them into determine_boxes()
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
                # Remove spaces from input
                i = i.translate({ord(' '): None for j in ' '})

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


# Functions to be used for .sort() key parameter
# Returns the volume of an input object for use with later sorting
def vol(entry):
    return entry.volume


# Returns the type of the input object
def get_type(entry):
    return entry.type


# Returns the size of the smallest side of a rotatable object
def smallest_side(entry):
    if entry.type != 'o':
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
def side_check(item, side):
    if largest_side(item) > side:
        return 0
    else:
        return 1


# Function to determine the amount of and size of boxes needed for a list of items
def determine_boxes(items):
    boxes = []
    scannedItems = []
    totalVolume = 0

    for i in range(len(items)):
        totalVolume += items[i].volume
        scannedItems.append(items[i])

        if totalVolume >= 100 * 100 * 40:  # Volume of large box
            if len(scannedItems) == 1:
                sys.stderr.write("Item too large to fit in a box")
                exit(2)  # Item too large for any box
            else:
                scannedItems.pop(len(scannedItems)-1)
                boxes.append(box.LargeBox(scannedItems))
                scannedItems = [items[i]]
                totalVolume = 0

    if totalVolume > (40 * 40 * 40):
        if totalVolume > (75 * 75 * 40):
            boxes.append(box.LargeBox(scannedItems))
        else:
            boxes.append(box.MediumBox(scannedItems))
    elif totalVolume:
        boxes.append(box.SmallBox(scannedItems))

    return boxes


# x = box_algorithm('itemList.csv')
# print(x)
# print(x[0].volume)
# print(x[0].contentsVolume)
# for j in range(len(x[0].contents)):
#     print(x[0].contents[j].name)
# print(x[0].contents[0])
# print(largest_side(x[0].contents[0]))

# a = 9
# b = 3
# y = [['o'] * a for i in range(b)]
# for i in range(len(y)):
#     print(y[i])
# coordinate_x = 10
# matrix_length = 5
# p = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#
# for i in range((coordinate_x - matrix_length), coordinate_x):
#     print(p[i])
