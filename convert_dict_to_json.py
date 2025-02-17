import json

# Python dictionary
data = {
    "name": "Zubayer Hossain",
    "age": 16,
    "language": ["Python", "JavaScript"],
    "is_student": True
}

# Convert dictionary to JSON
json_data = json.dumps(data, indent=4)

# Print JSON data
print("JSON Data:\n", json_data)

# Print object members
print("\nObject Members:")
for key, value in data.items():
    print(f"{key}: {value}")
