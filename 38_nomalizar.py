import unicodedata

# Función para quitar tildes (acentos) de una cadena
def normalizar(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    ).lower()

# Prueba de normalización
nombre_base = "José"
nombre_ingresado = "jose"

if normalizar(nombre_base) == normalizar(nombre_ingresado):
    print("Coinciden")
else:
    print("No coinciden")
# ------------------------------------------------------
import unicodedata

def normalizar(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    ).lower()

clientes = [
    {"nombre": "Lucía", "celular": "123456"},
    {"nombre": "Martín", "celular": "789012"},
    {"nombre": "Sofía", "celular": "345678"}
]

def buscar_cliente(lista_clientes, nombre):
    for cliente in lista_clientes:
        if normalizar(cliente["nombre"]) == normalizar(nombre):
            return True, cliente
    return False, None

# Búsqueda de cliente
while True: 
    nombre_cliente = input("¿Qué cliente deseas buscar? ")
    existe, datos = buscar_cliente(clientes, nombre_cliente)
    if existe:
        print(f"Cliente encontrado: {datos['nombre']} - Celular: {datos['celular']}")
        break
    else:
        print("Cliente no encontrado.")

# ----------------------------------------------------------------
import unicodedata

# Función para normalizar texto (quita tildes y convierte a minúsculas)
def normalizar(texto):
    # Quitar tildes
    texto_sin_tildes = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )
    # Convertir a minúsculas para evitar distinción entre mayúsculas y minúsculas
    return texto_sin_tildes.lower()

# Lista de clientes
clientes = [
    {"nombre": "Lucía", "celular": "123456"},
    {"nombre": "Martín", "celular": "789012"},
    {"nombre": "Sofía", "celular": "345678"}
]

# Función para buscar un cliente, con normalización
def buscar_cliente(lista_clientes, nombre):
    for cliente in lista_clientes:
        if normalizar(cliente["nombre"]) == normalizar(nombre):
            return True, cliente
    return False, None

# Búsqueda de cliente
while True: 
    nombre_cliente = input("¿Qué cliente deseas buscar? ")
    existe, datos = buscar_cliente(clientes, nombre_cliente)
    if existe:
        print(f"Cliente encontrado: {datos['nombre']} - Celular: {datos['celular']}")
        break
    else:
        print("Cliente no encontrado.")


# 🔎 ¿Qué hace el código?
# unicodedata.normalize('NFD', texto) convierte el texto a una forma normalizada que separa los caracteres de los acentos.

# unicodedata.category(c) != 'Mn' filtra los caracteres de tipo "Mark, Nonspacing" (es decir, los acentos y otros signos diacríticos).

# Luego, lower() convierte todo a minúsculas para que no haya distinción entre mayúsculas y minúsculas.

# 🔄 ¿Cómo se aplica a tu 

# --------------------------------------------------------


import unicodedata

# Función para normalizar texto (quita tildes y convierte a minúsculas)
def normalizar(texto):
    texto_sin_tildes = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )
    return texto_sin_tildes.lower()

# Función de búsqueda de cliente
def buscar_cliente(lista_clientes, nombre):
    for cliente in lista_clientes:
        if normalizar(cliente["nombre"]) == normalizar(nombre):
            return True, cliente
    return False, None

# Función de búsqueda de producto
def buscar_producto(lista_productos, nombre):
    for producto in lista_productos:
        if normalizar(producto["nombre"]) == normalizar(nombre):
            return True, producto
    return False, None

# Función de búsqueda de dirección
def buscar_direccion(lista_direcciones, direccion):
    for dir in lista_direcciones:
        if normalizar(dir["direccion"]) == normalizar(direccion):
            return True, dir
    return False, None

# Ejemplo de uso
clientes = [{"nombre": "Lucía", "celular": "123456"}, {"nombre": "Sofía", "celular": "345678"}]
productos = [{"nombre": "Laptop", "precio": 1000}, {"nombre": "Tablet", "precio": 300}]
direcciones = [{"direccion": "Calle Falsa 123"}, {"direccion": "Avenida Siempre Viva 742"}]

# Llamadas a las funciones de búsqueda
nombre_cliente = input("¿Qué cliente deseas buscar? ")
existe_cliente, cliente = buscar_cliente(clientes, nombre_cliente)
if existe_cliente:
    print(f"Cliente encontrado: {cliente['nombre']} - Celular: {cliente['celular']}")
else:
    print("Cliente no encontrado.")

nombre_producto = input("¿Qué producto deseas buscar? ")
existe_producto, producto = buscar_producto(productos, nombre_producto)
if existe_producto:
    print(f"Producto encontrado: {producto['nombre']} - Precio: {producto['precio']}")
else:
    print("Producto no encontrado.")

direccion = input("¿Qué dirección deseas buscar? ")
existe_direccion, dir = buscar_direccion(direcciones, direccion)
if existe_direccion:
    print(f"Dirección encontrada: {dir['direccion']}")
else:
    print("Dirección no encontrada.")

