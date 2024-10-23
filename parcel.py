import ast, json

def SerializzaLista(lVar) -> str:
        
        return (str(lVar))
    

def Deserializza(sVar) -> list:

        sVar = ast.literal_eval(sVar)

        return sVar


mydict_1 = { "brand": "Ford","electric": False,"year": 1964,"colors": ["red", "white", "blue"]}

mydict_2 = "{ 'brand':   'Ford'," + \
    "'electric': False," + \
    "'year': 1964," + \
    "'colors': ['red', 'white', 'blue']}"

def SerializaJson(dData,) -> bool:


    with open("ciao.json","w") as file:
    
        json.dumps(dData)

        return True
    
    return False


def DeserializeJson(file_path) -> dict:
    

    json.load
    adict_1 = json.loads(mydict_2)