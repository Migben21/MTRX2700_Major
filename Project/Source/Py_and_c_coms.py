import os

def Init_send_data(num_array):
    string = ""

    for i in range(num_array):
        string = string + "," + str(num_array[i])

    send_data(string)
    return

def send_data(data):
    #getting the file directory
    path = os.getcwd()
    file_path = os.path.abspath(os.path.join(path, os.pardir))
    file_path = file_path + '\MTRX2700_Major\Project\Includes\data.txt'


    f = open(file_path, "w")
    f.write(data)
    f.close()

    return


