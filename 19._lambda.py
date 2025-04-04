# QUE ES LAMBDA
# Exactamente, lambda te permite definir funciones en una sola línea sin necesidad de usar def. Es útil cuando necesitas funciones pequeñas y rápidas.

# !suma = lambda a,b: a+b
# !print(suma(5,2))


# !raiz_cuadrada = lambda x: x * 2
# !print(raiz_cuadrada(6))
# !print(raiz_cuadrada(19))

# * 1. Lambda con listas (ordenar una lista de tuplas)

# persona = [('Ana',25),('Juan',12),('Pedro',20)]

# #ordenar por edad(segun elementos de la tupla)

# persona.sort(key=lambda x:x[1])
# print(persona)

#* 🔹 Ejemplo 1: Ordenar por la segunda letra de un nombre

# !nombres = ['Pedro','Ana','Maria','Ronny']

# !nombres.sort(key=lambda x: x[1])
# !print(nombres)

#* 🔹 Ejemplo 2: Ordenar una lista de diccionarios por edad

# ! peronas = [
# !     {'nombre':'Ana', 'Edad':25},
# !     {'nombre':'Luis', 'Edad':20},
# !     {'nombre':'carlos', 'Edad':30},
# !     {'nombre':'Ronny', 'Edad':45},
# !     {'nombre':'Nico', 'Edad':60},
# !     {'nombre':'Kenyu', 'Edad':89},
# ! ]

# ! peronas.sort(key=lambda x: x['nombre'])
# ! print(peronas)


#* 🔹 Ejemplo 3: Ordenar por el último número de una tupla

#! numeros = [(3,5,8),(1,2,3),(4,6,1)]

#! numeros.sort(key=lambda x : x[-1])

#! print(numeros)


# 🔹 4. Verificar si un número es primo
# Premisa (ES): Escribe un programa que determine si un número dado es primo.
# 🔹 1. Verificar si un número es primo
# Premisa (ES): Escribe un programa que determine si un número dado es primo.


# *numero = int(input('Ingrese un numero:  '))
# *numero_primo = lambda num: all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)) and num > 1
# *resultado = numero_primo(numero)
# *print(f"El numero:{numero} es primo") if resultado is True else print(f"El numero:{numero} no es primo")



# 🔹 Ejercicio 2: Encontrar el número mayor en una lista
# Premisa (ES): Dada una lista de números, encuentra el número más grande sin usar max().
# Premise (EN): Given a list of numbers, find the largest number without using max().

# 💡 Pista: Puedes usar un bucle para recorrer la lista y actualizar el número mayor encontrado.

# list_numero = []

# for numero in range(5):
#     numero = int(input(f"Ingrese el numero {numero +1}: "))
#     list_numero.append(numero)

# print(list_numero)

# num_mayor = lambda lista: lista[0] if len(lista) == 1 else max(lista[0], num_mayor(lista[1:]))

# resultado = num_mayor(list_numero)
# print(resultado)


# ✅ Ejemplo 1: Ordenar productos por descuento (usando sorted)
# 🛍️ Contexto:
# Tienes una tienda online y quieres ordenar una lista de productos según el porcentaje de descuento, de mayor a menor.

# 👇 Código:



# producto = [
#     {'nombre' : 'Laptop','precio' : 1500 ,'descuento' : 10},
#     {'nombre' : 'Tablet','precio' : 1000 ,'descuento' : 50},
#     {'nombre' : 'Celular','precio' : 3000 ,'descuento' : 19},
#     {'nombre' : 'Parlantes','precio' : 500 ,'descuento' : 57}
# ]

# #Ordenar por descuento 

# ordenes= sorted(producto, key=lambda x:x['descuento'])

# for p in ordenes:
#     print(f'{p['nombre']} - {p['descuento']}% de descuento')
 

# print('-' * 40)

# Ejercicio 1: Ordenar productos por precio
# Tienes la siguiente lista de productos con su nombre y precio. Usa lambda para ordenar los productos por precio en orden ascendente.


# productos = [
#     {'nombre': 'Laptop', 'precio': 1500},
#     {'nombre': 'Tablet', 'precio': 1000},
#     {'nombre': 'Celular', 'precio': 3000},
#     {'nombre': 'Parlantes', 'precio': 500}
# ]

# precios = sorted(productos, key=lambda x:x['precio'],reverse=False)

# for precio in precios:
#     print(f'{precio["nombre"]} - {precio["precio"]}')



# Ejercicio 2: Ordenar estudiantes por calificación
# Tienes la siguiente lista de estudiantes con su nombre y calificación. Usa lambda para ordenar a los estudiantes por calificación en orden descendente.

# estudiantes = [
#     {'nombre': 'Juan', 'calificacion': 85},
#     {'nombre': 'Ana', 'calificacion': 92},
#     {'nombre': 'Pedro', 'calificacion': 78},
#     {'nombre': 'Maria', 'calificacion': 90}
# ]


# notas = sorted(estudiantes, key=lambda x:x['calificacion'],reverse=True)

# for nota in notas:
#     print(f'{nota["nombre"]} - {nota["calificacion"]}')



# Ejercicio 3: Ordenar productos por nombre
# Tienes la siguiente lista de productos con su nombre y cantidad disponible. Usa lambda para ordenar los productos por nombre en orden alfabético (de la A a la Z).


# productos = [
#     {'nombre': 'Laptop', 'cantidad': 15},
#     {'nombre': 'Tablet', 'cantidad': 10},
#     {'nombre': 'Celular', 'cantidad': 50},
#     {'nombre': 'Parlantes', 'cantidad': 25}
# ]


# producto = sorted(productos, key=lambda x:x['cantidad'] ,reverse=True)

# for p in producto:
#     print(f'{p["nombre"]} - {p["cantidad"]} S/')



# Ejercicio 4: Ordenar empleados por antigüedad
# Tienes la siguiente lista de empleados con su nombre y antigüedad en años. Usa lambda para ordenar los empleados por antigüedad en orden ascendente.
# Objetivo: Ordenar los empleados por antigüedad de menor a mayor utilizando

# empleados = [
#     {'nombre': 'Carlos', 'antiguedad': 5},
#     {'nombre': 'Laura', 'antiguedad': 2},
#     {'nombre': 'Luis', 'antiguedad': 8},
#     {'nombre': 'Marta', 'antiguedad': 3}
# ]

# empleado = sorted(empleados, key=lambda x:x['antiguedad'])

# for e in empleado:
#     print(f"{e['nombre']} - {e['antiguedad']}")