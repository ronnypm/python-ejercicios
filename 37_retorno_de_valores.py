# 🧪 Ejercicio 1: función que verifica si un número está en una lista

# def buscar_numero(lista,numero):
#     if numero in lista:
#         return True ,numero
#     else:
#         return False, numero


# mis_numeros = [4,7,2,6,7,22]

# existe, valor = buscar_numero(mis_numeros,4)

# if existe:
#     print(f'Si esta el numero: {valor}')
# else:
#     print(f'{valor}No existe')



# ---------------------------------------------------------------------------

# productos = [
#     {"nombre": "Laptop", "precio": 1000},
#     {"nombre": "Smartphone", "precio": 500},
#     {"nombre": "Tablet", "precio": 300},
#     {"nombre": "Auriculares", "precio": 50}
# ]

# def buscar_producto(lista_producto,nombre_producto):
#     for producto in lista_producto:
#         if producto['nombre'].lower() == nombre_producto.lower():
#             return True, producto
#     return False, None

# while True:
#     buscar = input('Que producto desea buscar? ')
#     existe,producto = buscar_producto(productos,buscar)


#     if existe:
#         print(f'Producto encontrado: {producto["nombre"]} Precio:{producto['precio']}')
#     else:
#         print('No existe')





# ---------------------------------------------------------------------------


clientes = [
    {"nombre": "Lucía", "celular": "123456"},
    {"nombre": "Martín", "celular": "789012"},
    {"nombre": "Sofía", "celular": "345678"}
]

def buscar_cliente(lista_clientes, nombre):
    for cliente in lista_clientes:
        if cliente["nombre"].lower() == nombre.lower():
            return True, cliente
    return False, None





while True: 
    nombre_cliente = input("¿Qué cliente deseas buscar? ")
    existe, datos = buscar_cliente(clientes, nombre_cliente)
    if existe:
        print(f"Cliente encontrado: {datos['nombre']} - Celular: {datos['celular']}")
        break
    else:
        print("Cliente no encontrado.")


