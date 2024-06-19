import json

# read customers.json
with open('./customers.json', 'r') as f:
    data = json.load(f)

# Create a dictionary to store the email and id
id_email_map = {}

# Traverse the customer list
for customer in data['result']['customers']:
    # Check if the 'company' key is in the customer dictionary
    if 'company' in customer and customer['company']:
        # Check if the 'name' key is in the 'company' dictionary
        if 'name' in customer['company'] and customer['company']['name']:
            # Check if the 'name' key is 'Smartshares'
            if customer['company']['name'] == 'Smartshares':
                # Check if the 'email' key is in the customer dictionary
                id_email_map[customer['email']] = customer['id']

print("All Done with customers")


# Write the id_email_map dictionary to a file
with open('./id_email_map.json', 'w') as f:
    json.dump(id_email_map, f)


