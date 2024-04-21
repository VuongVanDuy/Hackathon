import requests
import folium
import webbrowser
import datetime

m = folium.Map(location=[59.9343, 30.3351], zoom_start=12)


def getCoords(RouteId):
    response = requests.get(f"https://spb-transport.gate.petersburg.ru/api/stops/{RouteId}/1")
    data = response.json()
    coordinates = [[point["lon"], point["lat"]] for point in data["result"][0]["path"]]
    return coordinates


def get_schedule(stop_id):
    response = requests.get(f"https://spb-transport.gate.petersburg.ru/api/stop/{stop_id}")
    data = response.json()
    schedules = data["result"][0]["schedules"]
    return schedules


def draw_route(route_coordinates, schedule, num_stars):
    global m

    m = folium.Map(location=[59.9343, 30.3351], zoom_start=12)

    if route_coordinates and len(route_coordinates) >= 2:
        now = datetime.datetime.now().time()

        all_times = []
        for schedule_entry in schedule:
            for time in schedule_entry["arrivalTime"]:
                if time == "24:01:00":
                    all_times.append("00:01:00")  # Convert to next day's time
                else:
                    all_times.append(time)

        closest_time = min(all_times, key=lambda x: (datetime.datetime.strptime(x, "%H:%M:%S") - datetime.datetime.strptime(now.strftime("%H:%M:%S"), "%H:%M:%S")).total_seconds())

        index = all_times.index(closest_time)

        position = index / len(all_times)

        bus_coords = route_coordinates[int(position * len(route_coordinates))]

        folium.PolyLine(locations=route_coordinates, color='blue').add_to(m)

        folium.Marker(location=bus_coords, popup="Bus").add_to(m)

        html = f"""
        <div style="position: fixed; bottom: 50px; left: 50px; z-index: 9999; background-color: white; padding: 10px; border-radius: 5px; border: 1px solid #ccc;">
            <p>Select the number of stars:</p>
            <div>
                {''.join(['&#9733;' if i < num_stars else '&#9734;' for i in range(5)])}
            </div>
            <input type="range" min="0" max="5" value="{num_stars}" id="starRange" onchange="updateStars()">
            
        </div>
        <script>
            function updateStars() {{
                var slider = document.getElementById("starRange");
                var output = document.getElementById("selectedStars");
                output.innerHTML = slider.value;
                var starsDiv = slider.previousElementSibling;
                starsDiv.innerHTML = '';
                for (var i = 0; i < 5; i++) {{
                    if (i < slider.value) {{
                        starsDiv.innerHTML += '&#9733;';
                    }} else {{
                        starsDiv.innerHTML += '&#9734;';
                    }}
                }}
            }}
        </script>
        """
        m.get_root().html.add_child(folium.Element(html))


        map_file = "route_map.html"
        m.save(map_file)

        webbrowser.open(map_file)
    else:
        print("Failed to retrieve route coordinates or insufficient coordinates.")


def main():
    while True:
        route_id = input("Enter the route ID (or type 'exit' to quit): ")
        if route_id.lower() == 'exit':
            break
        try:
            route_coordinates = getCoords(route_id)
            route_coordinates = [(coord[1], coord[0]) for coord in route_coordinates]
            stop_id = "15464"  # Your stop ID here
            schedule = get_schedule(stop_id)
            num_stars = int(input("Enter the number of stars to color yellow (0-5): "))
            if 0 <= num_stars <= 5:
                draw_route(route_coordinates, schedule, num_stars)
            else:
                print("Invalid number of stars. Please enter a number between 0 and 5.")
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
