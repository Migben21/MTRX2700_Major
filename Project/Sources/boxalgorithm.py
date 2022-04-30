import csv
from Includes import objecttypes as obj
from Includes import boxes as box

with open('../Includes/items/itemList.csv', newline='') as csvfile:
    contents = csv.reader(csvfile, delimiter=',', quotechar='|')
    for line in contents:
        for i in line:
            # Compares content of csv file to dictionary containing all item names to create objects
            print(obj.allItems[i.lower()]().name)

# scan = "Eggs"
# x = obj.allItems[scan]()
# print(x.name)

# pear = obj.Apples()
# print(pear.length)
#
# firstbox = box.LargeBox()
# print(firstbox.length)
#
# objects = []
#
# for x in range(10):
#     item = obj.Apples()
#
#     objects.append(item)
#
# print(objects[1].name)