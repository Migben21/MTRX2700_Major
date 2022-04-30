import csv
import sys
from Includes import objecttypes as obj
from Includes import boxes as box


# Function to get the volume of an input object for use with later sorting
def vol(entry):
    return entry.volume


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

        everything.sort(key=vol)
        for i in range(len(everything)):
            print(everything[i].name)
        print("")


