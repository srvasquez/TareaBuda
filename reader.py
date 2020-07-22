import numpy as np
from red import Station, Red


def color_stations(conections):
    color_stations = np.array([])
    for color_station in conections.diagonal():
        if color_station == "0":
            color_stations = np.append(color_stations, "white")
        elif color_station == "1":
            color_stations = np.append(color_stations, "red")
        else:
            color_stations = np.append(color_stations, "green")
    return color_stations

def load_file(file):
    recieved = open(file, 'r')
    data = recieved.readlines()
    recieved.close()
    name_stations = data[0].strip().split(" ")
    number_stations = len(name_stations)
    conections = np.empty((0, number_stations))
    for row in data[1:]:
        conections = np.append(conections, np.array([row.strip().split(" ")]), axis=0)
    return number_stations, name_stations, color_stations(conections), conections

def generate_red(number_stations, name_stations, color_stations, conections):
    stations = np.array([])
    for i in range(number_stations):
        stations = np.append(stations, Station(name_stations[i], color_stations[i]))
        for j in range(i):
            if conections[i][j] == "1":
                stations[i].append(stations[j])
                stations[j].append(stations[i])
    return Red(stations)


if __name__ == "__main__":
    a = "Examples\\red1.txt"
    number_stations, name_stations, color_stations, conections = load_file(a)
    print(number_stations)
    print(name_stations)
    print(conections)
    print(color_stations)
    red = generate_red(number_stations, name_stations, color_stations, conections)
    print(red)



