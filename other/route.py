import requests

url = "https://graphhopper.com/api/1/route"
api_key = "d9f5c07e-d416-4e13-a49a-c27d4a871345"
headers = {"Authorization": f"Bearer {api_key}"}
query = {
    "profile": "car",
    "point": ["51.131,12.414"],
    "locale": "en",
    "instructions": True,
    "calc_points": True,
    "points_encoded": True,
    "ch.disable": True,  # Disable speed mode
    "algorithm": "round_trip",
    "round_trip.distance": 10000,
    "round_trip.seed": 0,
    "alternative_route.max_paths": 2,
    "alternative_route.max_weight_factor": 1.4,
    "alternative_route.max_share_factor": 0.6,
  "key": "d9f5c07e-d416-4e13-a49a-c27d4a871345"
}

response = requests.get(url, headers=headers, params=query)
data = response.json()

# Print relevant information (you can customize this part)
print("Response status code:", response.status_code)
print("Route distance (meters):", data.get("paths", [{}])[0].get("distance", "N/A"))
print("Route time (seconds):", data.get("paths", [{}])[0].get("time", "N/A"))
print("Route instructions:")
for instruction in data.get("paths", [{}])[0].get("instructions", []):
    print(instruction.get("text", "N/A"))