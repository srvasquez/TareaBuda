class Station:

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.conections = []
     
    def __str__(self):
        return f"Nombre estación: {self.name} \nConexiones: {', '.join(i.name for i in self.conections)}"

    def __len__(self):
        return len(self.conections)

    def append(self, station):
        self.conections.append(station)


class Red:

    def __init__(self, stations):
        self.stations = stations

    def __str__(self):
        line = "-"*18
        stations_information = f'\n{line}\n'.join(str(station) for station in self.stations)
        return f"Estaciones:\n\n{stations_information}"

    def append(self, station):
        self.stations.append(station)


if __name__ == "__main__":
    
    a = Station('A', 'red')
    b = Station('B', 'blank')
    c = Station('C', 'green')

    a.append(b)
    a.append(c)

    red = Red([a, b, c])
    print(red)

