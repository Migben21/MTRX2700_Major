from Includes import boxes

def send_data(data):
    f = open("data.txt", "w")
    f.write(data)
    f.close()

send_data("12,45,23")