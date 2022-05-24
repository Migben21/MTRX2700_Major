import os

def Init_send_data(num_array):
    string = ""

    string = str(num_array[0])

    for i in range(1,len(num_array)):
        string = string + "," + str(num_array[i])

    send_data(string)
    
    return

def send_data(data):
    #getting the file directory
    file_path = "Project\Includes\data.txt"

    f = open(file_path, "w")
    f.write(data)
    f.close()

    return

def waiting():
    file_path = "data.txt"

    i = 0
    str = ""

    while i == 0:
        f = open(file_path, "r")
        f.read(str)

        if len(str) == 0:
            i = 1
        
        f.close()
    
    return



