
import json

mydict_1 = { "brand": "Ford",
"electric": False,
"year": 1964,
"colors": ["red", "white", "blue"]}

mydict_2 = "{ 'brand':   'Ford'," + \
"'electric': False," + \
"'year': 1964," + \
"'colors': ['red', 'white', 'blue']}"



def SerializaJson(dData,file_path):
    pass

def DeserializeJson(file_path):
    pass



json.dump()
str1 = json.dumps(mydict_1)

json.load
dict_1 = json.loads(mydict_2)