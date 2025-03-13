# # Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.



# list_cursos = ["Matemáticas", "Física", "Química" , "Historia" , "Lengua"]

# for i in list_cursos
#     print(f"Yo estudio {i}")

# cursos = [ (f"Yo estuido {i}") for i in list_cursos]

# print(cursos)



# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.

# list_cursos = ["Matemáticas", "Física", "Química" , "Historia" , "Lengua"]
# list_note = []

# for i in list_cursos:
#     note = input(f'Ingrese la nota del curso {i}: ')
#     list_note.append(note)


# for curso, nota in zip(list_cursos,list_note):
#     print(f"en {curso} haz sacado {nota}")

# for i in range(len(curs)):
#     print(curs[i],notas[i])


# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.


# list_number = []

# for i in range(5):
#     question = int(input(f"Ingrese los numeros de la loteria: "))
#     list_number.append(question)


# list_number.sort()

# print(list_number)


# Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas



# list_number = [1,2,3,4,5,6,7,8,9,10]


# list_number.reverse()

# print(*list_number, sep= ",")




# Ejercicio 6
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.


# Forma 1 de hacerlo 

# list_curs = ["Matemáticas", "Física", "Química" , "Historia" , "Lengua"]
# list_failed = []


# for i in list_curs:
#     score = int(input(f"Ingrese la nota del curso {i}:  "))
#     if score <= 12:
#         list_failed.append(i)

# print(f"Cursos jalados: {", ".join(list_failed)}")


# Forma 2

# list_curs = ["Matemáticas", "Historia", "Física", "Química"]  # Lista de cursos
# list_failed = []  # Inicializa la lista de cursos jalados

# for i in list_curs:
#     while True:
#         try:
#             score = int(input(f"Ingrese la nota del curso {i} (0-20): "))
#             if 0 <= score <= 20:
#                 break  # Sale del bucle si la nota está en el rango válido
#             else:
#                 print("⚠️ La nota debe estar entre 0 y 20.")
#         except ValueError:
#             print("Error: Ingresa un número válido.")

#     if score <= 12:
#         list_failed.append(i)

# # Imprimir los cursos jalados sin corchetes
# if list_failed:
#     print(f"Cursos jalados: {', '.join(list_failed)}")
# else:
#     print("No jalaste ningún curso. ¡Felicidades! 🎉")



# Ejercicio 7
# Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

# alphabet = ["A","B","C","D","F","G","H","I","J","K","L","M","N","O","P","K","R","S","T","U","V","W","X","Y","Z"]

# delete = [ i for i in alphabet if i % 3 != 0]
# alphabet = []
# for i in range(97,123):
#     if (i-96) % 3 != 0:
#         alphabet.append(chr(i))

# print(alphabet)


# alphabet = [chr(i) for i in range(97,123)if (i-96) % 3 != 0]

# print(alphabet)


# Ejercicio 8
# Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.


# word = input("Ingrese un palabra: ")

# if word == word[::-1]:
#     print("Es palindromo")
# else:
#     print("No es  palindromo")


# Ejericio 9
# Escribe un programa que pida al usurio una palabra y muestre por pantalla el numero de veces que contiene cada vocal 


# vowels = ["a","e","i","o","u"]
# word = input("Ingrese una palabra: ").lower()
# # contador = 0

# for i in word:
#     if i in vowels:
#         contador+=1

# print(f"La palabra {word} tiene {contador} vocales")


# for i in word:
#     contador =0
#     for j in word:
#         if j == i :
#             contador+=1

#     print("La vocal " + i + " aparece " + str(contador) + " veces")

# Ejercicio 10

# Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

# prices = [50, 75, 46, 22, 80, 65, 8]

# min = max = prices[0]


# for price in prices[1:]:
#     if price < min:
#         min = price 
#     if price > max:
#         max = price

# print(min)
# print(max)




# menor = min(prices)
# mayor = max(prices)


# print(menor)
# print(mayor)

# EJERCICIOS CON BUSQUEDA LINEAL PARA MEJORAR EN ESTE TIPO DE ALGORITMO

# ENCUENTRA EL MENOR Y EL MAYOR DADA LA LISTA DE NUMERPOS
# Encuentra el número menor y el mayor recorriendo la lista solo una vez.

# numeros = [15, 3, 9, 20, 7, 2, 18, 5]

# mayor = menor = numeros[0]

# for numero in numeros[1:]:
#     if numero < menor:
#         menor = numero
#     if numero > mayor:
#         mayor = numero

# print(menor)
# print(mayor)

# 2️⃣ Temperaturas extremas
# Un sensor de temperatura ha registrado las siguientes mediciones en un día: [32, 28, 35, 30, 31, 29, 34, 33]


# Escribe un programa que recorra la lista y determine la temperatura más baja y la más alta.


# temperatura = [32, 28, 35, 30, 31, 29, 34, 33]

# tem_min = tem_max = temperatura[0]

# for Temperatura in temperatura[1:]:
#     if Temperatura < tem_min:
#         tem_min = Temperatura
#     if Temperatura > tem_max:
#         tem_max = Temperatura



# print(tem_min)
# print(tem_max)



# 3️⃣ Mayor diferencia
# Tienes una lista de alturas de personas en centímetros: [170, 165, 180, 175, 160, 185, 172]
# Encuentra la mayor diferencia entre la persona más alta y la más baja.


alturas = [170, 165, 180, 175, 160, 185, 172]

alt_min = alt_max = alturas[0]

for altura in alturas[1:]:
    if altura < alt_min:
        alt_min = altura
    if altura > alt_max:
        alt_max = altura


print(alt_min)
print(alt_max)
print(alt_max - alt_min)
