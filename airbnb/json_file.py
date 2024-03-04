import json

# Prepare data to write
data = {
   "name": "John Doe",
   "age": 30,
   "city": "New York",
   "hobbies": ["reading", "hiking", "coding"]
}

# Write data to JSON file
with open("data.json", "w") as outfile:
   json.dump(data, outfile, indent=4)

# Read data from JSON file
with open("data.json", "r") as infile:
   data_from_file = json.load(infile)

# Access and print data
print("Name:", data_from_file)
# print("Hobbies:", data_from_file["hobbies"])