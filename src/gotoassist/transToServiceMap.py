import json

# read services.json
with open('./services.json', 'r') as f:
    data = json.load(f)

# Create a dictionary to store the name and id
servicesName_id_map = {}

# Traverse the service list
for service in data['result']['services']:
    # Check if the 'company' key is in the service dictionary
    servicesName_id_map[service['name']] = service['id']

print("All Done with services")


with open('./servicesName_id_map.json', 'w') as f:
    json.dump(servicesName_id_map, f)


# Read the value from the dictionary
with open('./servicesName_id_map.json', 'r') as f:
    servicesName_id_map = json.load(f)
value = servicesName_id_map.get('Smartshares - Test Service')

# Print the value
print(value)

