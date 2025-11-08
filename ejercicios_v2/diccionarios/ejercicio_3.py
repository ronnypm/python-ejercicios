# Ejercicio 3

# Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

# Fruta 	 |  recio
# ----------------------
# Plátano 	 |  1.35
# Manzana 	 |  0.80
# Pera 	     |  0.85
# Naranja 	 |  0.70


fruit_dict = {
    "Platano":	1.35,
    "Manzana":	0.8,
    "Pera": 0.85,
    "Naranja": 0.70
}

fruit = input(f"fruta: ").title()
cantidad = int(input("ingrese la cantida: "))
if fruit.title() not in fruit_dict:
    print(f"lo sentimos no contamos con la fruta {fruit}")
else:
    print(fruit_dict[fruit] * cantidad)
