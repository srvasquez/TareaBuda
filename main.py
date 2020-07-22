import sys
import numpy as np
from reader import load_file, color_stations, generate_red
from red import Station, Red


def recieve_params():
    if len(sys.argv) == 1:
        name_file = "Examples\\red1.txt"
        start_station = "A"
        goal_station = "F"
        vagon_color = "white"
    else:
        name_file = sys.argv[1]
        start_station = sys.argv[2]
        goal_station = sys.argv[3]
        if len(sys.argv) == 4:
            vagon_color = "white"
        else:
            vagon_color = sys.argv[4]
    return name_file, start_station, goal_station, vagon_color
    

if __name__ == "__main__":
    
    name_file, start_station, goal_station, vagon_color = recieve_params()
    number_stations, name_stations, color_stations, conections = load_file(name_file)
    red = generate_red(number_stations, name_stations, color_stations, conections)
    print(vagon_color)
    red.search_path("A", "F", "green")
    #print(red)
    
    

        

