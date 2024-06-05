import json

# Function to read a JSON file and return its content
def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

# Path to your JSON file
file_path = './data/stops.json'

# Read the JSON file
data = read_json(file_path)

file_path_1 = './data/1062_coords.json'
data_1 = read_json(file_path_1)
# Print the data
stopsInfo = data['result']

IdStop_name = {}
for i in range(len(stopsInfo)):
    IdStop_name[stopsInfo[i]['id']] = stopsInfo[i]['name']

#print(IdStop_name)

info1062 = data_1['result'][0]
stopId1062 = info1062['stopIDs']

nameStops = []
for i in range(len(stopId1062)):
    stop_id = stopId1062[i]
    if stop_id in IdStop_name:
        name = IdStop_name[stop_id]
        nameStops.append(name)

print(nameStops)