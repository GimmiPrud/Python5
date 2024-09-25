
import json

mydict_1 = { "brand": "Ford",
"electric": False,
"year": 1964,
"colors": ["red", "white", "blue"]}

mydict_2 = "{ 'brand':   'Ford'," + \
"'electric': False," + \
"'year': 1964," + \
"'colors': ['red', 'white', 'blue']}"



def SerializzaJson(dData: dict, file_path: str)-> bool:
    try:
        with open(file_path,"w") as file:
            file.write(json.dumps(dData))
        return True
    except:
        return False
    
print(SerializzaJson(mydict_1,"JSON/dict.json"))
    

def DeserializzaJson(file_path: str)-> dict:
    dict1 = {}
    with open(file_path,"r") as file:
        dict1 = json.loads(file.read())
    return dict1

print(DeserializzaJson("JSON/dict.json"))





json.dump()
str1 = json.dumps(mydict_1)

json.load
dict_1 = json.loads(mydict_2)