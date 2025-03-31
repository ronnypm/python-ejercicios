#SYNTAX
#newlist = [expression for item in iterable if condition == True]
# Para crear una nueva lista: Las list comprehensions son ideales cuando necesitas generar una nueva lista a partir de otra, aplicando una transformación o filtrado.

# Código simple y compacto: Cuando la lógica es sencilla y puede expresarse en una sola línea.


#Usa comprensión de listas para CREAR y FILTRAR listas nunca para imprimir resuldtados.

# Ejemplo 1: Crear una lista con los números del 1 al 10
# numero = [i for i in range(1,11)]
# print(numero)


# numero = []
# for i in range(1,11):
#     numero.append(i)

# print(numero)



# Ejemplo 2: Crear una lista con los cuadrados de los números del 1 al 5


# cuadrado = [i**2 for i in range(1,6)]
# print(cuadrado)


# Ejemplo 3: Filtrar solo los números pares del 1 al 10



# numero = [i for i in range(1,10) if i % 2 == 0]
# print(numero)




# fruit = ["apple","banana","cherry","kiwi","mango"]

# new_list = [i for i in fruit if i != 'apple']

# print(new_list)


# for i in fruit:
#     if i != "apple":
#         new_list.append(i)

# print(new_list)


# Ejercicio 1: Filtrar números pares
# Dada una lista de números [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], crea una nueva lista que contenga solo los números pares.

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# even_numbers = [number for number in numbers if number % 2 == 0 ]

# print(even_numbers)


# Ejercicio 2: Filtrar palabras largas
# Dada una lista de palabras ["apple", "banana", "kiwi", "mango", "strawberry", "blueberry"], crea una nueva lista que contenga solo las palabras que tienen más de 5 letras.

# words = ["apple", "banana", "kiwi", "mango", "strawberry", "blueberry"]


# long_words = [long for long in words if len(long) > 5 ]

# print(long_words)

# Ejercicio 3: Filtrar números mayores que un valor
# Dada una lista de números 25, 60, 10, 75, 30, 90, 40], crea una nueva lista que contenga solo los números mayores que 50.

# numbers = [25, 60, 10, 75, 30, 90, 40]

# greater_than_50 = [number for number in numbers if number > 50]

# print(greater_than_50)


# Ejercicio 4: Filtrar elementos que contengan una letra específica
# Dada una lista de palabras words = ["apple", "banana", "cherry", "kiwi", "mango"], crea una nueva lista que contenga solo las palabras que incluyen la letra "a".


# words = ["apple", "banana", "cherry", "kiwi", "mango"]

# word_with_a = [word for word in words if "a" in word]

# print(word_with_a)

# Ejercicio 5: Filtrar elementos únicos
# Dada una lista con elementos repetidos items = ["apple", "banana", "apple", "kiwi", "banana", "mango"], crea una nueva lista que contenga solo los elementos únicos (sin duplicados).

# items = ["apple", "banana", "apple", "kiwi", "banana", "mango"]
# unique_items = []
# [unique_items.append(item) for item in items if item not in unique_items]
# print(unique_items)

# OJO CON ESTO Las list comprehensions están diseñadas para crear nuevas listas, no para realizar acciones como .append().

# Versión mejorada:
# Aquí te dejo una versión más clara y "pythónica" usando un bucle for:

# python
# Copy
# items = ["apple", "banana", "apple", "kiwi", "banana", "mango"]
# unique_items = []

# for item in items:
#     if item not in unique_items:  # Si el elemento no está en la lista
#         unique_items.append(item)  # Agrégalo

# print(unique_items)


# Bonus: Usando conjuntos (set)
# Otra forma más eficiente de eliminar duplicados es convertir la lista en un conjunto (set), ya que los conjuntos no permiten elementos repetidos. Luego, puedes convertirlo de nuevo a una lista:

# python
# Copy
# items = ["apple", "banana", "apple", "kiwi", "banana", "mango"]
# unique_items = list(set(items))  # Convertir a conjunto y luego a lista

# print(unique_items)

# Ejercicio 6: Filtrar números negativos
# Dada una lista de números [10, -5, 20, -15, 30, -25], crea una nueva lista que contenga solo los números negativos.

# numbers = [10, -5, 20, -15, 30, -25]

# negative_numbers = [num for num in numbers if num < 0]
# print(negative_numbers)

# Ejercicio 7: Filtrar palabras que empiezan con una letra específica
# Dada una lista de palabras ["apple", "banana", "blueberry", "kiwi", "blackberry"], crea una nueva lista que contenga solo las palabras que empiezan con la letra "b".

# word = ["apple", "banana", "blueberry", "kiwi", "blackberry"]

# word_starting_with_b = [start for start in word if start.startswith("b")]

# print(word_starting_with_b)


# Ejercicio 8: Filtrar elementos que no están en otra lista
# Dada una lista de frutas ["apple", "banana", "cherry", "kiwi", "mango"] y una lista de frutas a excluir ["apple", "kiwi"], crea una nueva lista que contenga solo las frutas que no están en la lista de exclusiones.

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# exclude = ["apple", "kiwi"]

# filtered_fruits= []

# for fruit in fruits:
#     if fruit not in exclude:
#         filtered_fruits.append(fruit)

# print(filtered_fruits)

# fru = [fruit for fruit in fruits if fruit not in exclude]


# Ejercicio 9: Filtrar números divisibles por 3
# Dada una lista de números, crea una nueva lista que contenga solo los números divisibles por 3

# numbers = [9, 10, 12, 15, 20, 21, 25]

# divisible_by_3 = [number for number in numbers if number % 3 == 0]

# print(divisible_by_3)

# Ejercicio 10: Filtrar elementos que son cadenas de texto
# Dada una lista con elementos de diferentes tipos (números, cadenas, etc.) [10, "apple", 3.14, "banana", 42, "kiwi", 100], crea una nueva lista que contenga solo las cadenas de texto.

# items = [10, "apple", 3.14, "banana", 42, "kiwi", 100]


# strings_only = [item for item in items if type(item) == str]

# strings_only = [item for item in items if isinstance(item,str)]
# print(strings_only)

# print(strings_only)


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x if x != "banana" else "orange" for x in fruits]

# print(newlist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key=str.lower)
# print(thislist)




# Puedes usar un for si necesitas cambiar varios valores dentro de la lista:
# mi_lista = [10, 20, 30, 20, 40]  
# mi_lista = [99 if num == 20 else num for num in mi_lista]  # Cambia todos los 20 por 99  
# print(mi_lista)  
