class Station:

    def __init__(self, name, color, conections = []):
        self.name = name
        self.color = color
        self.conections = conections
    
    def __str__(self):
        return f"Nombre estación: {self.name} \nConexiones: {', '.join(i.name for i in self.conections)}"

    def __len__(self):
        return len(self.conections)

    def append(self, station):
        self.conections.append(station)


class Red:

    def __init__(self, stations):
        self.stations = stations


if __name__ == "__main__":
    a = Station('a', 'red')
    b = Station('b', 'blank')
    c = Station('c', 'green')
    a.append(b)
    #a.append(c)
    print(a)
    print(len(a))
