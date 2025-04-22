# Leer y escribir archivos json

import json


#guardar un diccionario en un Json 
persona = {'nombre':'juan', 'edad':40}
 
with open('persona.json', 'w') as archivo:
    json.dump(persona, archivo)



# Leer archivo JSON
with open('persona.json', 'r') as archivo:
    datos = json.load(archivo)
    print(datos)