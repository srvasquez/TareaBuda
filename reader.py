import numpy as np


def load_file(file):
    data = open(file, 'r').readlines()
    name_stations = data[0].strip().split(" ")
    number_stations = len(name_stations)
    conections = np.empty((0, number_stations))
    for row in data[1:]:
        conections = np.append(conections, np.array([row.strip().split(" ")]), axis=0)
    return number_stations, name_stations, conections

    
if __name__ == "__main__":
    a = "Examples\\red1.txt"
    number_stations, name_stations, conections = load_file(a)
    print(number_stations)
    print(name_stations)
    print(conections)
