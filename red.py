import numpy as np


class Station:

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.conections = np.array([])
     
    def details(self):
        return f"Nombre estación: {self.name} \nConexiones: {', '.join(i.name for i in self.conections)}"

    def __str__(self):
        return self.name

    def __len__(self):
        return self.conections.shape[0]

    def append(self, station):
        self.conections = np.append(self.conections, station)


class Red:

    def __init__(self, stations):
        self.stations = stations

    def __str__(self):
        line = "-"*18
        stations_information = f'\n{line}\n'.join(station.details() for station in self.stations)
        return f"Estaciones\n{line}\n{stations_information}\n{line}"

    def append(self, station):
        self.stations = np.append(self.stations, station)


if __name__ == "__main__":
    
    a = Station('A', 'red')
    b = Station('B', 'blank')
    c = Station('C', 'white')

    a.append(b)
    a.append(c)

    red = Red([a, b, c])
    print(red)


