# ✨ Ejercicio 1: Área de un círculo
# ES:
# Escribe una función llamada calcular_area_circulo que tome el radio como parámetro y devuelva el área del círculo. Usa la fórmula:
 
# Llama a la función con diferentes valores de radio.

import math

# def calcular_area_circulo(radio):
#     area = 3.14 * radio**2 
#     print(area)

# calcular_area_circulo(7)
# calcular_area_circulo(5)
# calcular_area_circulo(8)


# def calcular_area_circulo(radio):
#     area = math.pi * pow(radio,2)
#     return area

# print(calcular_area_circulo(89))
# print(calcular_area_circulo(12))


# Ejercicio 2: Conversión de temperatura
# Problema:
# Crea una función llamada celsius_a_fahrenheit que convierta una temperatura en grados Celsius a Fahrenheit usando la fórmula:

# 𝐹=𝐶×9/5+32

# Llama a la función con diferentes valores de temperatura y muestra los resultados.

# def celsius_fahrenheit(celsius):
#     fahrenheit = celsius * 9/5 + 32
#     return fahrenheit

# print(celsius_fahrenheit(6))
# print(celsius_fahrenheit(7))
# print(celsius_fahrenheit(79))



# Ejercicio 3: Números pares e impares
# Problema:
# Crea una función llamada es_par que reciba un número entero como parámetro y devuelva True si el número es par y False si es impar.

# 🔹 Pistas:

# Un número es par si al dividirlo por 2 el residuo (%) es 0.
# Puedes usar return True y return False dentro de la función.


# def es_par(numero):
#     return numero % 2 == 0
    
# print(es_par(4))
# print(es_par(7))




# Ejercicio 4: Contar vocales en una palabra
# Problema:
# Crea una función llamada contar_vocales que reciba una cadena de texto (palabra o frase) y devuelva la cantidad de vocales (a, e, i, o, u) que contiene.

# 🔹 Pistas:

# Usa un bucle para recorrer la cadena.
# Usa un contador para sumar cada vocal encontrada.
# Recuerda que las vocales pueden estar en mayúscula o minúscula.

# for text in texts:
#     print(text.upper())

# print_text('Hola','Python','Ronny')
# print_text('Hola')





# def contar_vocales(texto):
#     contador_vocales = 0

#     for letra in texto:
#         if letra.lower() in  ['a','e','i','o','u']:
#             contador_vocales += 1

#     return contador_vocales


# print(contar_vocales('python'))
# print(contar_vocales('Hola mundo'))
# print(contar_vocales('ESTUDIO'))




# 🔹 Ejercicio:
# Crea una función que reciba una lista de números y devuelva el número más grande.





# def numero_mas_grande(lista_de_numeros):

#     num_max = lista_de_numeros[0]

#     for numero in lista_de_numeros[1:]:
#         if num_max < numero:
#             num_max = numero
#     return num_max

# print(numero_mas_grande([1,2,3,4,5]))



# 🔹 Ejercicio:
# Crea una función que reciba una cadena de texto y devuelva la misma cadena, pero al revés.

# def palabra_al_reves(texto):
#     texto_inverso = ''
#     for i in range(len(texto)-1,-1,-1):
#         texto_inverso += texto[i]
#     return (texto_inverso)

# print(palabra_al_reves('perro'))





# Ejercicio:

# Define una función llamada es_palindromo(palabra) que reciba una palabra y devuelva True si es un palíndromo (se lee igual al derecho y al revés) y False en caso contrario.


# def es_palindromo(palabra):
    
#     if palabra == palabra[::-1]:
#         print('Es palindrome')
#     else:
#         print('No es palindrome')
    
 
# es_palindromo('oso')




def es_palindromo(palabra):
    return palabra.lower() == palabra.lower()[::-1]

print(es_palindromo('Oso'))  # True
print(es_palindromo('Python'))  # False
