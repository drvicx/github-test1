import json

# some JSON:
json_data = '{ "name":"John", "age":30, "city":"New York"}'

# parse json_data:
python_dict = json.loads(json_data)

# the result is a Python dictionary:
print(python_dict["age"])
