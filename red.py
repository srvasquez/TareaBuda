import numpy as np
from dijkstra import solve_path


class Station:

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.conections = np.array([])
     
    def details(self):
        return f"Nombre estación: {self.name} \nColor estación: {self.color} \nConexiones: {', '.join(i.name for i in self.conections)}"

    def __str__(self):
        return self.name

    def __len__(self):
        return self.conections.shape[0]

    def append(self, station):
        self.conections = np.append(self.conections, station)

    def quantity_conections(self):
        return self.conections.shape[0]

    def get_conections(self):
        return self.conections

    def get_station(self, index):
        return self.conections[index]

    def get_color(self):
        return self.color

class Red:

    def __init__(self, stations):
        self.stations = stations

    def __str__(self):
        line = "-"*18
        stations_information = f'\n{line}\n'.join(station.details() for station in self.stations)
        return f"Estaciones\n{line}\n{stations_information}\n{line}"

    def append(self, station):
        self.stations = np.append(self.stations, station)

    def initialize_visited(self):
        visited = {}
        for station in self.stations:
            visited[station] = {'distance': False, 'visited': False, 'parent': False}
        return visited
     
    def search_path(self, start_station, goal_station, vagon_color):
        for station in self.stations:
            if str(station) == start_station:
                visited = self.initialize_visited()
                final_station = solve_path(station, goal_station, vagon_color, visited)
                if final_station:
                    path = []
                    while visited[final_station]['parent']:
                        color_station = final_station.get_color()
                        if color_station == 'white' or vagon_color == 'white' or vagon_color == color_station or str(final_station) == goal_station:
                            path.insert(0, str(final_station))
                        final_station = visited[final_station]['parent']
                    path.insert(0, start_station)
                    return path
                else:
                    return false
    

if __name__ == "__main__":
    
    a = Station('A', 'red')
    b = Station('B', 'green')
    c = Station('C', 'white')

    a.append(b)
    b.append(c)
    a.append(c)
    c.append(a)

    red = Red(np.array([a, b, c]))
    print(red)
    print("->".join(red.search_path("B", "A", "white")))


