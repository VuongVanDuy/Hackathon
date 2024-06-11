import json

# Function to read a JSON file and return its content
class init_data():
    def __init__(self, routeId):
        self.file_stops = './data/stops.json'
        self.file_route = f'./data/{routeId}_coords.json'
        self.data_route = self.read_data(self.file_route)
        self.create_data_stops()
        
           
    def read_data(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data['result']

    def get_coords_route(self):
        path_route = self.data_route[0]['path']
        coords = []
        for addr in path_route:
            coords.append([addr['lat'], addr['lon']])
        return coords
    
    def create_data_stops(self):
        stopsInfo = self.read_data(self.file_stops)
        self.data_stops = {}
        
        for i in range(len(stopsInfo)):
            info_stop = [stopsInfo[i]['name'], stopsInfo[i]['lat'], stopsInfo[i]['lon']]
            self.data_stops[stopsInfo[i]['id']] = info_stop

    def get_stops_of_route(self):
        stopID_of_route = self.data_route[0]['stopIDs']

        self.stops_route = {}
        for i in range(len(stopID_of_route)):
            stop_id = stopID_of_route[i]
            if stop_id in self.data_stops:
                info = self.data_stops[stop_id]
                self.stops_route[info[0]] = [info[1], info[2]]
        # with open('./data/1065_stops.json', 'w', encoding='utf-8') as file:
        #     json.dump(stops_1062, file, ensure_ascii=False, indent=4)
        return self.stops_route
        


if __name__ == '__main__':
    data_route = init_data(1062)
    #print(data_route.get_stops_of_route())
    res = data_route.get_coords_route()
    for i in res:
        print(i)


