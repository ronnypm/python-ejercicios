# Ejercicio 1
# Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

# diccionario = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

# divisa = input('Ingrese una divisa: ')

# if divisa.capitalize() in diccionario:
#     print(diccionario[divisa.capitalize()])
# else:
#     print('No existe')


# print(diccionario['Euro'])

# print(diccionario.get('Euro'))

# Ejercicio 2
# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

###*ESTO ES MI FORMA DE HACERO 


# ?user_data = ['nombre','edad','direccion','telefono']
# ?data_user = []
# ?for data in user_data:
#    ? input_date = (input(f'Ingrese el {data} porfavor: '))
#     ?data_user.append(input_date)

# ?dict_data = {'nombre':data_user[0],'edad':data_user[1],'direccion':data_user[2],'telefono':data_user[3]}

# ?print( f'{dict_data['nombre']} tiene {dict_data['edad']} años, vive en {dict_data['direccion']} y su número de teléfono es {dict_data['telefono']}')

# ?print(type(dict_data['edad']))


#*FORMA DE HACER MEJOR 


# !dict_data = {}

# !for data in ['nombre','edad','direccion','telefono']:
#     !dict_data[data] = input(f'Ingrese el campo {data}: ')

# !print(f"{dict_data['nombre']} tiene {dict_data['edad']} años, vive en {dict_data['direccion']} y su número de teléfono es {dict_data['telefono']}.")

#*CON LISTA COMPRESION

# !dict_data = {campo: input(f'Ingrese el {campo} por favor: ') for campo in ['nombre', 'edad', 'direccion', 'telefono']}

# !print(f"{dict_data['nombre']} tiene {dict_data['edad']} años, vive en {dict_data['direccion']} y su número de teléfono es {dict_data['telefono']}.")


# *campos = ['nombre', 'edad', 'direccion', 'telefono']
# *dict_data = {
#     *campo: int(input(f'Ingrese el {campo} por favor: ')) if campo == 'edad' else input(f'Ingrese el {campo} por favor: ') 
#     *for campo in campos
# *}

# *print(f"{dict_data['nombre']} tiene {dict_data['edad']} años, vive en {dict_data['direccion']} y su número de teléfono es {dict_data['telefono']}.")


# Ejercicio 3
# Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

# Fruu               
# Plåtano     1 35
# Manzana     0.80           
# Naranja     0.85
# Predo0      0.70

#!MI VERSION 

# !from decimal import Decimal

# !dict_fruit = {'platano':1.35,'manzana':0.80,'naranja':0.85,'pera':0.70}

# !fruit = input('Ingrese una fruta: ')
# !price = float(input(f"Ingrese el numero de kilos: "))

# !if fruit in dict_fruit.keys():
#    ! print(f'La  fruta {fruit} le sale {round(price*dict_fruit[fruit])}')
# !else:
#  !   print('Esa fruta no se esta disponible')


# dict_fruit = {'platano':1.35,'manzana':0.80,'naranja':0.85,'pera':0.70}

# #solicitamos la fruta
# fruit = input('Ingrese una fruta: ').lower()#convertimos a minusculas para evitar problemas

# #verificamos si la fruta est disponible
# if fruit in dict_fruit:
#     try :
#         #si la fruta esta dentro de la lista el programa nos pedira los kilos 
#         kilogram = float(input(f'Ingrese el numero de kilos de {fruit}: '))

#         if kilogram > 0:
#             total = round(kilogram*dict_fruit[fruit],2)
#             print(f'El precio total de {kilogram} kilos de {fruit} es {total:.2f}')
#         else:
#             print('Ingrese un numero positivo para l')
            
#     except ValueError:
#         print("Debe ingresar un valor numerico para los kilos")
# else:
#     print("Esa fruta no está disponible.")


# # Permitir varias frutas
# cart = {}
# while True:
#     fruit = input('Ingrese una fruta (o "salir" para terminar): ').lower()
#     if fruit == "salir":
#         break
#     if fruit in dict_fruit:
#         try:
#             kilos = float(input(f"Ingrese el número de kilos de {fruit}: "))
#             if kilos > 0:
#                 cart[fruit] = round(kilos * dict_fruit[fruit], 2)
#             else:
#                 print("Por favor, ingrese un número positivo para los kilos.")
#         except ValueError:
#             print("Debe ingresar un valor numérico para los kilos.")
#     else:
#         print("Esa fruta no está disponible.")

# # Mostrar resumen
# if cart:
#     print("\nResumen de compra:")
#     for fruit, total in cart.items():
#         print(f"- {fruit.capitalize()}: ${total:.2f}")
#     print(f"Total a pagar: ${sum(cart.values()):.2f}")
# else:
#     print("No se realizó ninguna compra.")


# def get_price(fruit, kilos):
#     """Calcula el precio total de una fruta."""
#     return round(kilos * dict_fruit[fruit], 2)

# def get_cart_summary(cart):
#     """Muestra el resumen de la compra."""
#     print("\nResumen de compra:")
#     for fruit, total in cart.items():
#         print(f"- {fruit.capitalize()}: ${total:.2f}")
#     print(f"Total a pagar: ${sum(cart.values()):.2f}")



# Ejercicio 4
# Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.





# months = {'01':'enero','02':"febrero",'03':'marzo','04':'abril','05':'mayo','06':'junio','07':'julio','08':'agosto','09':'setiembre','10':'octubre','11':'noviembre','12':'diciembre'}


# date = input('Ingrese una fecha en formato"dd/mm/aaaa": ')
# if '/' in date :
#     part = date.split('/')
#     if part[1] in months.keys():
#         print(f"{part[0]} de {months[part[1]]} del ano {part[2]}")
# else:
#     print('Error al ingresar la fecha')



# Ejercicio 5
# Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.

# score_student =  { 'Matemáticas': 6,
#              'Física': 4,
#              'Química': 5
#              }
# contador = 0
# for score in score_student:
#      contador+=score_student[score]
#      print(f'{score} tiene {score_student[score]}')
# print(f"Su promedio es {contador}")
    




#*IMPRIMIR CLAVE Y VALOR 
# *for subject, score in score_student.items():
#     *print(f'{subject} tiene {score}')


# for subject in sorted(score_student):
    # print(f'{subject} tiene {score_student[subject]}')




# Ejercicio 6
# Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
 
# user_data = ['edad', 'sexo', 'teléfono', 'correo_electrónico']

# dict_user_data = {data:(input(f'Ingrese el {data}')) for data in user_data }

# print(dict_user_data)
# dict_data_user ={}
# for data in user_data:
#     input_data = input(f'Ingrese el {data}: ')
#     dict_data_user[data] = input_data
    
#     print(f'El dato ingresado es : {dict_data_user[data]}')

# print(dict_data_user)


# Ejercicio 7
# Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato


#!debo este ejercicio




# Ejercicio 8
# Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.


# dict_words = {}

# # Construcción del diccionario
# while True:
#     word = input('Ingrese una palabra en formato "espanol:ingles" (o escriba "salir" para terminar): ')
    
#     if word.lower() == 'salir':
#         print('Gracias por crear el diccionario!')
#         break
#     if ':' in word:
#         palabra, traduccion = word.split(':')
#         dict_words[palabra.strip()] = traduccion.strip()
#     else:
#         print('Formato incorrecto. Por favor, use "espanol:ingles".')

# # Traducción de una frase
# word_traduction = input('Ingrese una frase en español para traducir: ')
# palabras = word_traduction.split()  # Divide la frase en palabras

# # Traducción palabra por palabra
# !frase_traducida = [
#    !dict_words.get(palabra, palabra)  # Si no está en el diccionario, deja la palabra original
#     !for palabra in palabras
# ]

# # Mostrar la frase traducida
# print('Traducción:', ' '.join(frase_traducida))


# Ejercicio 9
# Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.


# import os
# dic_fatura = {5:23,46:23}

# def agregar_factura():
#     while True:
#         print('Anada un factura')
#         numero_factura = int(input('Ingrese el numero de factura: '))
#         precio_factura = float(input('Ingrese el precio de la factura: '))
#         dic_fatura[numero_factura]=precio_factura  
#         print(f'Factura {numero_factura} se anadio con el precio de {precio_factura}')
        
#         option = input("desea seguir agregando mas facturas? (s/n) ").lower()
#         os.system('cls')
#         if option != 's':
#             print("Volviendo a menu principal")
#             break


# def pagar_factura():
#     print(dic_fatura)


#     while True: 

#         numero_factura = int(input('Ingrese el numero de factura: '))

#         if numero_factura in dic_fatura:
#             del dic_fatura[numero_factura]
#             print(f'La factura {numero_factura} ha sido pagada')
#         else:
#             print(f'La factura {numero_factura} no existe en el diccionario')


#         option = input("desea seguir eliminando facturas? (s/n) ").lower()
#         os.system('cls')
#         if option != 's':
#             print("Volviendo a menu principal")
#             break

# def eliminar_factura():
#     pass



# while True:

#     print(
#         """Ingrese una opcion porfavor
# 1)  Anadir factura
# 2)  Pagar factura
# 3)  Eliminar factura
# 4)  Salir
#          """
#     )

#     option = int(input('Seleccione una opcion porfavor (1-2-3-4): ')) 


#     if option == 1:
#         os.system('cls')
#         agregar_factura() 
#     elif option == 2:
#         os.system('cls')
#         pagar_factura()
#     elif option == 3:
#         pass
#     elif option== 4:
#         break


