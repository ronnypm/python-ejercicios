"""
🧩 Ejercicio 1: Contador de apariciones
📌 Temas: diccionario, bucles, condiciones

Dada una lista de palabras, crea un diccionario que cuente cuántas veces aparece cada palabra.
palabras = ["perro", "gato", "perro", "pájaro", "gato", "gato"]

Resultado esperado:
{"perro": 2, "gato": 3, "pájaro": 1}
"""

# lista_palabras = ["perro", "gato", "perro", "pájaro", "gato", "gato"]
# diccionario_palabra = {}


# for palabra in lista_palabras:
#     if palabra in diccionario_palabra:
#         diccionario_palabra[palabra] += 1
#     else:
#         diccionario_palabra[palabra] = 1


# print(diccionario_palabra)


# Imagina que tienes una lista con números repetidos y quieres eliminar los duplicados sin perder el orden.

# 💡 Pistas:

# Usa un set para rastrear qué números ya viste.

# Usa una lista para guardar los resultados en orden.

# Recorre la lista y añade cada número solo si no está en el set.

# numeros = [4, 2, 7, 4, 8, 2, 3, 7, 9, 1]
# set_numeros = set()
# lista_numero = []

# for numero in numeros:
#     if numero not in set_numeros:
#         lista_numero.append(numero)
#         set_numeros.add(numero)
    
    

# print(lista_numero)


# 🔹 Enunciado:

# Tienes una lista de nombres de personas que se registraron en un evento, pero algunos se registraron más de una vez con el mismo nombre. Tu tarea es crear una nueva lista donde cada nombre aparezca solo una vez, pero manteniendo el orden en el que se registraron por primera vez.

# ✏ Pistas:

# Usa un set para rastrear los nombres que ya agregaste.

# Recorre la lista y solo agrega los nombres si no están en el set.


# nombres = ["Ana", "Luis", "Pedro", "Ana", "Maria", "Luis", "Carlos", "Pedro", "Maria", "Juan"]

# set_nombre = set()

# lista_nombre = []

# for nombre in nombres:
#     if nombre not in set_nombre:
#         lista_nombre.append(nombre)
#         set_nombre.add(nombre)


# print(lista_nombre)


# Tienes una lista de colores donde algunos se repiten. Tu tarea es eliminar los duplicados manteniendo el orden en el que aparecen por primera vez.

# Lista de ejemplo:


# colores = ["rojo", "azul", "verde", "rojo", "amarillo", "azul", "verde", "naranja", "rojo"]

# set_colores = set()

# lista_colores = []


# for color in colores:
#     if color not in set_colores:
#         lista_colores.append(color)
#         set_colores.add(color)

# print(lista_colores)

# Dada la siguiente lista de palabras, crea una nueva lista donde solo se guarden las palabras que aparecen un número impar de veces en la lista original.

# Lista inicial
# palabras = ["sol", "luna", "estrella", "sol", "nube", "luna", "sol", "mar", "nube", "mar", "cielo"]

palabras = ["sol", "luna", "estrella", "sol", "nube", "luna", "sol", "mar", "nube", "mar", "cielo"]

# set_palabra = set()

# lista_palabra = []

# for palabra in range(len(palabras)):
#     if palabra % 2 != 0:
#         lista_palabra.append(palabras[palabra])
#         set_palabra.add(palabras[palabra])

# print(lista_palabra)




