import json
import uuid

with open('quotes.json', "r", encoding='utf-8') as quote_list:
    # load the json data into a python dictionary
    data = json.load(quote_list)


# Create a set to store the seen id values
seen = set()

# Loop through the objects in the data list
for obj in data:
  # Get the id value for the current object
  id = obj['id']

  # Check if the id value is already in the seen set
  if id in seen or id == "" or id == None:
    print(f"Duplicate id value: {id}")
    # The id value is a duplicate, so generate a new UUID
    new_id = uuid.uuid4()
    # Update the id value for the current object
    obj['id'] = str(new_id)
    print("New ID is: ", obj['id'])
    # Add the new id value to the seen set
    seen.add(new_id)
  else:
    # The id value is not a duplicate, so add it to the seen set
    seen.add(id)

# Save the updated data list to a JSON file
with open('quotes.json', 'w') as f:
  json.dump(data, f)