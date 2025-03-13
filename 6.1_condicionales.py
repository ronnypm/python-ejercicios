# Ejercicio 1:
# !Un cine ofrece descuentos en el precio de las entradas según la edad del cliente:

# !Menores de 12 años pagan 50% menos.
# !Mayores de 60 años pagan 30% menos.
# !Los demás pagan el precio completo.
# !Escribe un programa que pida al usuario su edad y el precio base del boleto, y luego calcule el precio final con el descuento aplicado.

#MI SOLUCION 

# *age= int(input("Ingrese la su edad: "))
# *price = float(input("Ingrese el precio del boleto para calcular su descuento:"))


# *if age > 12 and age <60:
#     *print(f'Usted pagara {price} S/')
# *elif age < 12 :
#     *print(f"el precio final de su boletao con el descuento incluido es {price - (price*50/100)} S/")
# *else:
#     *print(f"el precio final de su boletao con el descuento incluido es {price - (price*30/100)} S/")


# 
# !def calcular_precio_entrada(edad,preci0_base):
#     !if edad < 12:
#         !precio_final = precio_base * 0.5
#     !elif edad >= 60:
#         !precio_final = preci0_base * 0.7
#     !else:
#       !  precio_final = preci0_base

#     !return precio_final

# !edad = int(input("Ingrese su eadad: "))
# !precio_base = float(input("Ingrese el precio del boleto: "))

# !precio_final = calcular_precio_entrada(edad,precio_base)

# !print(f"el precio fian del boleto es: {precio_final} S/")

# Ejercicio 2: Clasificación de triángulos
# Escribe un programa que pida al usuario tres longitudes y determine si pueden formar un triángulo.
# Si pueden formar un triángulo, clasifícalo en:

# Equilátero (los tres lados iguales).
# Isósceles (dos lados iguales).
# Escaleno (todos los lados diferentes).
# Si no pueden formar un triángulo, muestra un mensaje diciendo que no es válido.
# 📌 Recuerda la condición para que sea un triángulo:
# 👉 La suma de dos lados siempre debe ser mayor al tercer lado.

#MI SOLUCION 

# lado_1 = int(input('Ingrese el primer lado: '))
# lado_2 = int(input('Ingrese el segundo lado: '))
# lado_3 = int(input('Ingrese el tercer lado: '))

# if lado_1 == lado_2 == lado_3:
#     print('Es un triangulo Equilatero ')
# elif lado_1 == lado_2 !=lado_3:
#     print('Es un trianguo Isoceles')
# else:
#     print("Es un triangulo Escaleno")


# Entrada de los lados/ soulucion de chat
# lado_1 = int(input('Ingrese el primer lado: '))
# lado_2 = int(input('Ingrese el segundo lado: '))
# lado_3 = int(input('Ingrese el tercer lado: '))

# # Verificación si los lados forman un triángulo
# if lado_1 + lado_2 > lado_3 and lado_1 + lado_3 > lado_2 and lado_2 + lado_3 > lado_1:
#     # Clasificación del triángulo
#     if lado_1 == lado_2 == lado_3:
#         print('Es un triángulo Equilátero.')
#     elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
#         print('Es un triángulo Isósceles.')
#     else:
#         print('Es un triángulo Escaleno.')
# else:
#     print('Los lados ingresados NO forman un triángulo.')

# *Ejercicio 3: Clasificación de números
# *Escribe un programa que reciba tres números enteros y determine:

# *Si son todos positivos, todos negativos o mixtos.
# *# Si alguno de ellos es cero, debe indicarlo.

# Ejemplo 1:
# Ingrese el primer número: 5  
# Ingrese el segundo número: 10  
# Ingrese el tercer número: 2  
# Todos los números son positivos.

# Ejemplo 2:
# Ingrese el primer número: -3  
# Ingrese el segundo número: 0  
# Ingrese el tercer número: 8  
# El conjunto de números es mixto. Además, hay al menos un cero.

# list_numeros =[]

# #contaodr
# positivos = 0
# negativos = 0
# ceros = 0

# for num in range(3):
#     numero = int(input(f'Ingrese el {num+1} numero: '))
#     list_numeros.append(numero)

# for nume in list_numeros:
#     if nume > 0:
#         positivos += 1
#     elif nume < 0:
#         negativos += 1
#     else:
#         ceros += 1

# if positivos == 3:
#     print('Todos los nuermos son positivos')
# elif negativos == 3:    
#     print('Todos los nuermos son negativos')
# else:
#     print('El conjunto es mixto')

# if ceros > 0:
#     print('Ademas, hay almenos un cero')



# 🔹 Ejercicio 4: Verificación de credenciales
# Crea un programa que pida al usuario un nombre de usuario y una contraseña.

# Si el nombre de usuario es "admin" y la contraseña es "1234", el programa debe imprimir "Acceso concedido".
# Si el usuario es correcto pero la contraseña no, debe imprimir "Contraseña incorrecta".
# Si el usuario es inwcorrecto, debe imprimir "Usuario no encontrado" y ni siquiera preguntar por la contraseña.

# usuario = 'admin'
# contrasena = '1234'


# nombre_usuario = input("Ingrese el usuario: ")

# if nombre_usuario != usuario:
#     print('Usuario incorrecte')

# else:
#     contrasena_usuario = input('Ingrese su contrasena: ')  

#     if contrasena_usuario == contrasena:
#         print('Acceso concedido')
#     else:
#         print('Contraseña incorrecta')
 

# Ejercicio 5: Calculadora simple
# Crea un programa que solicite dos números y una operación (+, -, *, /). Luego, usa condicionales para realizar la operación y mostrar el resultado. Si el usuario ingresa un operador no válido, debe mostrar un mensaje de error.

# Dime si quieres una pista o si prefieres intentarlo por tu cuenta. 🚀

# num1 = int(input('Ingrese el primer numero: '))
# num2 = int(input('Ingrese el segundo numero: '))
# operacion = input('Ingrese una opereacion (+,-,*,/): ')

# if operacion == '+':
#     print(f'La suma de {num1} y {num2} es: {num1 + num2}')
# elif operacion == '-':
#     print(f'La resta de {num1} y {num2} es: {num1 - num2}')
# elif operacion == '*':
#     print(f'La multiplicacion de {num1} y {num2} es: {num1 * num2}')
# else:
#    print(f'La division de {num1} y {num2} es: {num1 / num2}')



# num1 = int(input('Ingrese el primer número: '))
# num2 = int(input('Ingrese el segundo número: '))
# operacion = input('Ingrese una operación (+, -, *, /): ')

# if operacion == '+':
#     print(f'La suma de {num1} y {num2} es: {num1 + num2}')
# elif operacion == '-':
#     print(f'La resta de {num1} y {num2} es: {num1 - num2}')
# elif operacion == '*':
#     print(f'La multiplicación de {num1} y {num2} es: {num1 * num2}')
# elif operacion == '/':
#     if num2 != 0:
#         print(f'La división de {num1} entre {num2} es: {num1 / num2}')
#     else:
#         print('Error: No se puede dividir entre cero.')
# else:
#     print('Operación no válida.')
