import csv
from Includes import objecttypes as obj
from Includes import boxes as box

with open('../Includes/items/itemList.csv', newline='') as csvfile:
    contents = csv.reader(csvfile, delimiter=',', quotechar='|')
    for line in contents:
        for i in line:
            print(i)

pear = obj.Apples()
print(pear.length)

objects = []

for x in range(10):
    item = obj.Apples()

    objects.append(item)
