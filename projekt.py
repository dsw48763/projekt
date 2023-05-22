import sys
import json
import yaml
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

#task3
output_file = "output.json"
try:
    with open(output_file, "w") as file:
        json.dump(data, file, indent=4)
    print("JSON data saved to", output_file)
except Exception as e:
    print("Failed to save JSON data:", e)

#task4
yml_file = "file.yml"
try:
    with open(yml_file, "r") as file:
        data = yaml.safe_load(file)
    print("Loaded YAML data:", data)
except Exception as e:
    print("Failed to load YAML data from file:", e)