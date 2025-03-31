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


# alturas = [170, 165, 180, 175, 160, 185, 172]

# alt_min = alt_max = alturas[0]

# for altura in alturas[1:]:
#     if altura < alt_min:
#         alt_min = altura
#     if altura > alt_max:
#         alt_max = altura


# print(alt_min)
# print(alt_max)
# print(alt_max - alt_min)


# Listas (1) - 1
# Escriba un programa que permita crear una lista de palabras. Para ello, el programa tiene que pedir un número y luego solicitar ese número de palabras para crear la lista. Por último, el programa tiene que escribir la lista.






# for palabra in range(1,numero_palabra +1 ):
#     palabras = input(f'Ingrese la palabra {palabra}: ')
#     lista_palabra.append(palabras)

# print(f'La lista creadad es {lista_palabra}')

# try:
#     while True:
#         try:
#             numero_palabra = int(input('Ingres el numero de plabras: '))
#             if numero_palabra > 0:
#                 break
#             print('Imposible, ingrese un numero positivo')
#         except ValueError:
#             print('Error Ingrese un numero')

#     lista_palabra = []

#     for indice_palabra, _ in enumerate(range(numero_palabra),start=1):
#         input_palabra = input(f'Ingrese la palabra {indice_palabra}: ')
#         lista_palabra.append(input_palabra)

#     print(f'La lista creada es: {lista_palabra}')

# except  KeyboardInterrupt:
#     print("\nPrograma interrumpido por el usuario.")




# Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y diga cuántas veces aparece esa palabra en la lista.



# try:
#     while True:
#         try:
#             numero_palabra = int(input('Ingrese el numero de plabras: '))
            
#             if numero_palabra > 0:
#                 break
#             print('Imposible ingrese un numero positvo')
#         except ValueError:
#             print('Error, solo se permiten numeros') 

#     lista_palabra = []

#     for palabra, _ in enumerate(range(numero_palabra),start=1):
#         palabras = input(f'Ingrese la palabra {palabra}: ')
#         lista_palabra.append(palabras)

#     print(f'Palabras creadas {lista_palabra}')

#     palabra_buscar = input("Digame la palabra a buscar: ").lower()
#     contador = 0
#     for palabra in lista_palabra:
#         if palabra == palabra_buscar:
#             contador += 1

#     if contador == 0:
#         print(f'La palabra {palabra_buscar} aparece {contador} veces')
#     elif contador == 1:
#         print(f'La palabra {palabra_buscar} aparece {contador} veces')
#     else:
#         print(f'La palabra {palabra_buscar} aparece {contador} veces')


# except KeyboardInterrupt:
#     print('\nPrograma interrumpido por el usuario.')


# Listas (1) - 3
# Escriba un programa que permita crear una lista de palabras y que, a continuación, pida dos palabras y sustituya la primera por la segunda en la lista.

# try:
#     while True:
#         try:
#             numero_palabra = int(input('Ingrese el numero de plabras: '))
#             if numero_palabra > 0 :
#                 break
#             print('Ingrese un numero positivo.')
#         except ZeroDivisionError:
#             print('Ingrese un numero positivo.')
#         except ValueError:
#             print('Error solo se permiten numeros')


#     lista_numero = []


#     for numero in range(1,numero_palabra + 1):
#         while True:
#             palabra = input(f'Ingrese la palabra {numero}: ')
#             if palabra.isalpha():
#                 lista_numero.append(palabra)
#                 break
#             print('Error, solo se permiten letras')

#     print('-' * 30)

#     for indice, palabra in  enumerate(lista_numero,start=1):
#         print(f'El nombre {indice} es {palabra}') 


#     palabra_lista = input('Ingrese la palabra a sustituir: ') 
#     palabra_sustituir = input('Por la palabra: ')

#     for palabra in range(len(lista_numero)):
#         if lista_numero[palabra] == palabra_lista:
#             lista_numero[palabra] = palabra_sustituir

#     print(lista_numero)


# except KeyboardInterrupt:
#     print('\nPrograma interrumpido por el usuario.')



# Listas (1) - 4
# Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y elimine esa palabra de la lista.

# try:
#     while True:
#         try:
#             numero_palabra = int(input('Dígame cuántas palabras tiene la lista: '))
#             if numero_palabra > 0 :
#                 break
#             print('Ingrese un numero positivo.')
#         except ValueError:
#             print('Error solo se permiten numeros.')

        
#     lista_palabras = []


#     for palabra in range(1,numero_palabra + 1):
#         while True:
#             palabras = input(f'Dígame la palabra {palabra}: ')
#             if palabras.isalpha():
#                 lista_palabras.append(palabras)
#                 break
#             print('Solo se permiten letras.')

    
#     print('-' * 30)


#     for indice,valor in enumerate(lista_palabras,start=1):
#         print(f'{indice}.el nombre creado es {valor}. ')


#     palabra_eliminar = input('Palabra a eliminar: ')


#     while palabra_eliminar in lista_palabras:
#         lista_palabras.remove(palabra_eliminar)
    

#     # lista_palabras = [palabra for palabra in lista_palabras if palabra != palabra_eliminar]

#     print('-' * 30)

#     for indice,valor in enumerate(lista_palabras,start=1):
#         print(f'{indice}.lista actualizada es {valor}. ')


# except KeyboardInterrupt:
#     print('\nProgama interrumpido por el usuario.')


# Listas (1) - 5
# Escriba un programa que permita crear dos listas de palabras y que, a continuación, elimine de la primera lista los nombres de la segunda lista.

try:
    
    while True:
        try:
            numero_palabra = int(input('Dígame cuántas palabras tiene la lista: '))
            if numero_palabra > 0:
                    break
            print('Error, solo se permiten numeros positivos.')
        except ValueError:
            print('Error, no se permiten letras, solo numeros.')


    lista_palabra = []

    for palabra in range(1,numero_palabra + 1):
         while True:
              nombre = input(f'Dígame la palabra {palabra}: ')
              if nombre.isalpha():
                    lista_palabra.append(nombre)
                    break
              print('No se permiten numeros.')  


    print(f'La lista creada es {lista_palabra}')

    while True:
        try:
            numero_palabra = int(input('Dígame cuántas palabras tiene la lista de palabras a eliminar: '))
            if numero_palabra > 0:
                    break
            print('Error, solo se permiten numeros positivos.')
        except ValueError:
            print('Error, no se permiten letras, solo numeros.')

    lista_eliminar = []

    for palabra in range(1,numero_palabra + 1):
         while True:
              nombre = input(f'Dígame la palabra {palabra}: ')
              if nombre.isalpha():
                    lista_eliminar.append(nombre)
                    break
              print('No se permiten numeros.')


    for i in lista_eliminar:                
        for palabra in range(len(lista_palabra)-1,-1,-1):
            if lista_palabra[palabra] == i:
                    del lista_palabra[palabra]


    # lista_palabra = [palabra for palabra in lista_palabra if palabra not in lista_eliminar]

    # for palabra_eliminar in lista_eliminar:
    #   while palabra_eliminar in lista_palabra:
    #     lista_palabra.remove(palabra_eliminar)


    print(lista_palabra)
         
         


except KeyboardInterrupt:
    print('Programa interrumpido por el usuario.')


#Ejercicios6