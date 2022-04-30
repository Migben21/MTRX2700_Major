import csv

with open('items/itemList.csv', newline='') as csvfile:
    contents = csv.reader(csvfile, delimiter=',', quotechar='|')
    for line in contents:
        for i in line:
            print(i)

