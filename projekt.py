import sys
import json
import yaml
#Task1
argumenty = sys.argv[1:]
print("zadane argumenty:", argumenty)
#task2
plikjson = "file.json"
try:
    with open(plikjson, "r") as file:
        data = json.load(file)
    print("Zaladowano dane", data)
except Exception as e:
    print("Nie udalo sie zaladowac danych", e)

#task3
plikw = "output.json"
try:
    with open(plikwyjscie, "w") as file:
        json.dump(data, file, indent=4)
    print("Dane zapisane do: ", plikwyjscie)
except Exception as e:
    print("Nie udalo sie zapisac danych: ", e)

#task4
plikyml = "file.yml"
try:
    with open(plikyml, "r") as file:
        data = yaml.safe_load(file)
    print("Zaladowano YAML: ", data)
except Exception as e:
    print("Nie udalo sie zaladowac YAML: ", e)
#task5
plikw = "output.yml"
try:
    with open(plikw, "w") as file:
        yaml.dump(data, file)
    print("Dane zapisane do: ", plikw)
except Exception as e:
    print("Nie udalo sie zapisac danych: ", e)
#task6
plikxml = "file.xml"
try:
    x = ET.parse(plikxml)
    root = x.getroot()
    print("Zaladowano dane:")
    for i in root:
        print(i.tag, i.text)
except Exception as e:
    print("Nie udalo sie zaladowac danych:", e)
#task7
plikw = "output.xml"
try:
    with open(plikw, "w") as file:
        x.write(file)
    print("Dane zapisano w: ", plikw)
except Exception as e:
    print("Nie udalo sie zapisac danych", e)
