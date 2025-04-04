# ✅ Ejemplo 1: Filtrar alumnos aprobados (usando filter)
# 🎓 Contexto:
# Tienes una lista de alumnos con sus notas y quieres filtrar solo aquellos que hayan aprobado (nota ≥ 11).

# alumnos = [
#     {"nombre": "Carlos", "nota": 15},
#     {"nombre": "Ana", "nota": 9},
#     {"nombre": "Luis", "nota": 11},
#     {"nombre": "Valeria", "nota": 8}
# ]

# #Filtra aprobados

# aprovados = list(filter(lambda x:x['nota'] >= 11,alumnos))

# for a in aprovados:
#     print(f'{a["nombre"]} - {a["nota"]}')



# Ejercicio 1: Números pares
# Dada una lista de números, usa filter() para obtener solo los números pares.

# numeros = [10, 23, 45, 66, 78, 91, 100, 12, 17, 33]


# numero_pares = list(filter(lambda x: x % 2 == 0, numeros))

# print(numero_pares)



# Ejercicio 2: Palabras largas
# Tienes una lista de palabras. Usa filter() para obtener solo las palabras que tengan más de 5 letras.


# palabras = ["elefante", "sol", "universo", "luz", "estrella", "cielo", "guitarra"]



# palabra_longitud = list(filter(lambda x: len(x) >= 5 , palabras ))


# print(palabra_longitud)



# Ejercicio 3: Productos en stock
# Dado un inventario de productos, usa filter() para obtener solo los productos que tengan más de 10 unidades en stock.

# productos = [
#     {"nombre": "Laptop", "stock": 5},
#     {"nombre": "Teclado", "stock": 12},
#     {"nombre": "Mouse", "stock": 20},
#     {"nombre": "Monitor", "stock": 8},
#     {"nombre": "Silla", "stock": 15}
# ]

# producto_stock = list(filter(lambda x:x['stock'] > 10,productos))


# for p in producto_stock:
#     print(f'{p["nombre"]} - {p["stock"]} unidades.')


# Ejercicio 4: Filtrar adultos
# Dada una lista de edades, usa filter() para obtener solo las edades mayores o iguales a 18 años.


# edades = [12, 18, 25, 8, 30, 17, 21, 15, 40]
# mayores_edad = list(filter(lambda x: x > 18, edades))

# for e in mayores_edad:
#     print(e)


# Ejercicio 5: Temperaturas bajo cero
# Dada una lista de temperaturas, usa filter() para obtener solo las temperaturas por debajo de 0°C.

# temperaturas = [-5, 10, 3, -12, 0, 7, -8, 2, -1]

# lista_temperatura = list(filter(lambda x: x < 0 , temperaturas))

# lista_ordenadda = sorted(lista_temperatura,reverse=True)

# print(lista_ordenadda)




# Un número perfecto es un número que es igual a la suma de sus divisores propios positivos (excluyendo al mismo número). Un ejemplo de número perfecto es el 6, ya que sus divisores son 1, 2, 3, y 1 + 2 + 3 = 6.

# Ejercicio: Filtrar números perfectos
# Instrucciones:
# Crear una función que reciba un número y determine si es un número perfecto.

# Usar filter() y lambda para filtrar los números perfectos de una lista dada.

# Ejemplo:
# Entrada: [6, 8, 12, 28, 15]

# Salida: [6, 28] (Los números perfectos en la lista son 6 y 28).

# Pasos para resolverlo:
# Definir una función que verifique si un número es perfecto. Esta función debe:

# Sumar los divisores propios del número.

# Si la suma de los divisores es igual al número, entonces es un número perfecto.

# Filtrar la lista con la función auxiliar usando filter() y lambda.



