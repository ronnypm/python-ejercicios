"""
🧩 Ejercicio 1: Contador de apariciones
📌 Temas: diccionario, bucles, condiciones

Dada una lista de palabras, crea un diccionario que cuente cuántas veces aparece cada palabra.
palabras = ["perro", "gato", "perro", "pájaro", "gato", "gato"]

Resultado esperado:
{"perro": 2, "gato": 3, "pájaro": 1}
"""

lista_palabras = ["perro", "gato", "perro", "pájaro", "gato", "gato"]
diccionario_palabra = {}


for palabra in lista_palabras:
    if palabra in diccionario_palabra:
        diccionario_palabra[palabra] += 1
    else:
        diccionario_palabra[palabra] = 1


print(diccionario_palabra)
