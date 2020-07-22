def insert_open(open_queque, visited, station):
    distance_new_station = visited[station]['distance']
    for i in range(len(open_queque)):
        compared_station = open_queque[i]
        distance_station = visited[compared_station]['distance']
        if distance_station and distance_new_station <= distance_station:
            open_queque.insert(i, station) 
            return open_queque
    open_queque.append(station)
    return open_queque


def solve_path(start_station, goal_station, vagon_color, visited):
        open_queque = [start_station]
        visited[start_station]['distance'] = 0
        while open_queque:
            actual_station = open_queque.pop(0)
            visited[actual_station]['visited'] = True
            if str(actual_station) == goal_station:
                    return actual_station
            for station in actual_station.get_conections():
                if visited[station]['visited']:
                    continue
                color_station = station.get_color()
                if vagon_color != 'white' and color_station != 'white' and vagon_color != color_station:
                    distance = 0
                else:
                    distance = 1
                total_distance = visited[actual_station]['distance'] + distance
                if visited[station]['distance'] and total_distance >= visited[station]['distance']:
                    continue
                visited[station]['distance'] = total_distance
                visited[station]['parent'] = actual_station
                open_queque = insert_open(open_queque, visited, station)
        return False