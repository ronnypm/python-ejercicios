# def generar_pares(limite):
    
#     num = 1 


#     while num < limite:
#         yield num*2
#         num +=1 

   
# devulve_pares = generar_pares(10)

# print(next(devulve_pares))


# def devuleve_ciudades(*ciudades):
    
#     for elemento in ciudades:
#         #for sub_elemento in elemento:
#             yield from elemento

# ciudades_devueltas = devuleve_ciudades('Lima','Arequipa','Trujillo')

# print(next(ciudades_devueltas))
# print(next(ciudades_devueltas))



# Ejercicio 2:
# Crea un generador que reciba una lista de palabras y devuelva solo aquellas que tienen más de 5 letras.


# 🧩 Ejercicio 1: Generador de Palabras con Letra Inicial
# Objetivo:
# Tenés una lista de palabras. Querés generar solo aquellas que empiezan con una letra específica (por ejemplo, la letra "a"), una por una.

# Lógica:

# Tenés una lista de palabras (por ejemplo: "auto", "sol", "ave", "mesa", etc).

# Usás un generador (yield) que recorra esa lista.

# Solo yieldea las que empiezan con la letra que vos elegís.

# Luego las vas mostrando una a una con un for.

# 💡 Este ejemplo es perfecto para ver cómo se usa yield en vez de filtrar todo junto con filter o una lista.

# lista_palabra = ["auto", "sol", "ave", "mesa"]


# def palabras_con_a(lista):
#     for palabra in lista:
#         if palabra[0] == 'a':
#             yield palabra  

# palabras = palabras_con_a(lista_palabra)

# for p in palabras:
#     print(p)


# 🧩 Ejercicio 2: Generador de Números Pares hasta un Límite
# Objetivo:
# Querés generar todos los números pares hasta un número que el usuario indique, uno por uno.

# Lógica:

# El usuario ingresa un número límite (ej: 20).

# Usás una función con yield que recorra del 0 hasta ese número.

# Si el número es par (n % 2 == 0), lo yieldeás.

# Luego lo imprimís uno por uno, o lo usás como quieras.

# 💡 Esto sirve para entender cómo yield puede devolver elementos a demanda.


# def numero_pares(n):
#     for numero in range(1,n +1):
#         if numero % 2 == 0:
#             yield numero

# numeros = numero_pares(10)

# for n in numeros:
#     print(n)


# def eco():
#     while True:
#         mensaje = yield
#         print(f"Echo: {mensaje}")

# e = eco()
# next(e)  # Avanza hasta el primer yield
# e.send("Hola mundo")  # Imprime: Echo: Hola mundo


# 🎲 Ejercicio: Generador de palabras al revés en bucle
# Objetivo:
# Crear un generador que tome una frase y devuelva una palabra a la vez en orden invertido, repitiendo infinitamente


def palabra_invertida(palabra):

    lista_palabra = palabra.split()[::-1]

    while True:
        for palabras in lista_palabra:
            yield palabras

gen = palabra_invertida('Hola como estas')
print([next(gen) for _ in range(7)])