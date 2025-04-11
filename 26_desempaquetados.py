# def mostrar(*args):
#     for arg in args:
#         print(f"🔹 {arg}")

# mostrar("Juan", "Antonio", "Pedro", 42, [1, 2, 3])


#-----------------------------------------------------------

# def saludar(*nombres):
#     for nombre in nombres:
#         print(f"Hola, {nombre}")

#-------------------------------------------------------------

# def contar_nombres(*nombres):
#     print(f"Total de nombres recibidos: {len(nombres)}")
#     for nombre in nombres:
#         print(f"📛 {nombre}")

# contar_nombres("Juan", "Pedro", "Juan", "Ana", "Pedro")

#--------------------------------------------------------------

# def contar_repetidos(*nombres):
#     conteo = {}
#     for nombre in nombres:
#         conteo[nombre] = conteo.get(nombre, 0) + 1
#     for nombre, cantidad in conteo.items():
#         print(f"{nombre} aparece {cantidad} veces")

# contar_repetidos("Juan", "Pedro", "Juan", "Ana", "Pedro")

# --------------------------------------------------------------

# def contar_nombres(*nombres):
#     conteo = {}
#     for nombre in nombres:
#         conteo[nombre] = conteo.get(nombre, 0) + 1
#     return conteo

# print(contar_nombres("Juan", "Pedro", "Juan", "Ana", "Pedro", "Ana", "Ana"))

# --------------------------------------------------------------

# def decorador(func):
#     def wrapper(*args, **kwargs):
#         print(f"Has llamado a la función con los argumentos: {args}")
#         return func(*args, **kwargs)
#     return wrapper

# @decorador
# def sumar(*args):
#     return sum(args)

# # Llamando a la función con diferentes números de argumentos
# print(sumar(1, 2, 3, 4, 5))  # Suma todos los números
