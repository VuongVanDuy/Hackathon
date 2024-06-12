import requests
import folium
import webbrowser
import keyboard
from init_data import init_data

m = folium.Map(location=[59.9343, 30.3351], zoom_start=12)


def getCoords(routeId, direction):
    data_route = init_data(routeId, direction)
    return data_route.get_coords_route()


# def get_schedule(stop_id):
#     response = requests.get(f"https://spb-transport.gate.petersburg.ru/api/stop/{stop_id}")
#     data = response.json()
#     schedules = data["result"][0]["schedules"]
#     return schedules


def draw_route(route_coordinates):
    global m

    m = folium.Map(location=[59.9343, 30.3351], zoom_start=12)

    if route_coordinates and len(route_coordinates) >= 2:

        folium.PolyLine(locations=route_coordinates, color='blue').add_to(m)
        folium.Marker(location=route_coordinates[0], popup="Bus").add_to(m)
        
        map_file = "route_map.html"
        m.save(map_file)

        #webbrowser.open(map_file)
    else:
        print("Failed to retrieve route coordinates or insufficient coordinates.")


def main():
    while True:
        route_id = input("Enter the route ID (or type 'q' to quit): ")
        if route_id.lower() == 'q':
            break
        direction = input("Enter the direction route (or type 'q' to quit): ")
        if direction.lower() == 'q':
            break
        try:
            route_coordinates = getCoords(route_id, direction)
            draw_route(route_coordinates)
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
