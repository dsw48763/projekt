import sys
import json

#task1
arguments = sys.argv[1:]
print("Passed arguments:", arguments)
#task2
json_file = "file.json"
try:
    with open(json_file, "r") as file:
        data = json.load(file)
    print("Loaded JSON data:", data)
except Exception as e:
    print("Failed to load JSON data from file:", e)