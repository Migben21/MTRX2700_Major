from ...Project.Includes.boxes import boxSizes

def send_data(data):
    f = open("data.txt", "w")
    f.write(data)
    f.close()

send_data("12,45,23")