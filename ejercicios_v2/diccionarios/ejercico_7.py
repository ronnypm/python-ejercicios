
# Ejercicio 7
# Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato

from decimal import Decimal

# pregunta = True
productos = {}
while True:

    producto = input("PRODUCTO: ")
    precio = Decimal(input("PRECIO: "))

    productos[producto] = precio

    if input("Continuar? ").lower().strip() == "no":
        break
print(productos)

# creacion de multiples dcicionarion en una lista
# productos = []

# while True:
#     producto = {}
#     producto["nombre"] = input("Producto: ")
#     producto["precio"] = Decimal(input("Precio: "))

#     productos.append(producto)

#     if input("Continuar? ").lower().strip() == "no":
#         break

# print(productos)
# [
# {"nombre": "arroz", "precio": Decimal('12')},
# {"nombre": "pollo", "precio": Decimal('10')}
# ]
