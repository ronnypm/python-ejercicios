# 🌱 Introducción amigable
# Imagina que estás organizando una fiesta y necesitas llevar el control de:

# Qué comida trajo cada invitado,
# Cuántas veces alguien fue a servirse pastel,
# Y una lista ordenada de los juegos que jugarán en el orden que se sugirió.
# Con estructuras básicas como list, dict y tuple podrías lograrlo... pero ¿y si tuvieras herramientas ya listas, súper eficientes y pensadas justo para esos casos comunes?

# Ahí entra la librería collections de Python, un pequeño tesoro escondido en la biblioteca estándar.

# 🧠 Fundamentos de la librería collections
# collections es un módulo que proporciona estructuras de datos especializadas, cada una diseñada para hacer tareas comunes más fáciles, legibles y rápidas.

# Entre las más utilizadas están:

# Counter
# defaultdict
# OrderedDict
# deque
# namedtuple


#forma de hacerlo sin count

# frutas:list = ['manzana', 'banana', 'manzana', 'pera', 'banana', 'manzana']
# dic_frutas = {}

# for fruta in frutas:
#     cuanta_actual = dic_frutas.get(fruta,0)
#     dic_frutas[fruta] = cuanta_actual +1

# print(dic_frutas)

# dic_frutas = {}
# for fruta in frutas:
#     if fruta in dic_frutas:
#         dic_frutas[fruta] += 1
#     else:
#         dic_frutas[fruta] = 1  

# print(dic_frutas) 

# ¿Cuándo usarlo? Cuando necesites contar elementos rápidamente sin tener que inicializar manualmente un diccionario.
print('-' * 30)
print('counter:Contador de elementos')

from collections import Counter
print()
frutas:list = ['manzana', 'banana', 'manzana', 'pera', 'banana', 'manzana']
conteo = Counter(frutas)
print(conteo)
print(conteo.most_common(1))
# ----------------------------------------------------------------------------------------------------------------------
# ¿Cuándo usarlo?
# Cuando estás agrupando datos y no quieres preocuparte por inicializar claves.
print('-' * 30)
print('\ndefaultdict: Diccionario con valores por defecto\n')

from collections import defaultdict
print('Creacion con listas')
alimentos_por_personas = defaultdict(list)
alimentos_por_personas['Ana'].append('tarta de queso')
alimentos_por_personas['Luis'].append('Sandiwch')

print(alimentos_por_personas)
print(alimentos_por_personas['Ana'])

print('-' * 30)

print('Creacion con string')
alimentos_por_personas = defaultdict(str)

alimentos_por_personas['Ana'] += 'tarta de queso'
alimentos_por_personas['Luis'] += 'sandiwch'

print(alimentos_por_personas)



print('-' * 30)
print('Creacion con int')
frutas = ['manzana', 'banana', 'manzana', 'pera', 'banana', 'manzana']

#usamos int() como valor por defecto, que nos devuelve 0
dict_frutras = defaultdict(int)

for fruta in frutas:
    dict_frutras[fruta] += 1
print(dict_frutras)



print('-' * 30)
print('Creacion con str/lambda')

alimentos_por_personas = defaultdict(lambda: '')  # Usamos una función lambda para definir el valor por defecto

alimentos_por_personas['Ana'] += 'tarta de queso, '
alimentos_por_personas['Luis'] += 'Sandwich, '

print(alimentos_por_personas)


print('-' * 30)

#Mas ejemplos con lambda

alimentos_por_personas = defaultdict(lambda: 0)
alimentos_por_personas['Juan'] += 1
alimentos_por_personas['Hade'] += 2
alimentos_por_personas['Ernesto']

print(alimentos_por_personas)


print('-' * 30)


# Usamos lambda para que cada persona empiece con un valor de 5 (por ejemplo)
alimentos_por_personas = defaultdict(lambda: 5)

# Agregamos cantidades
alimentos_por_personas['Ana'] += 2  # Ana ahora tiene 7
alimentos_por_personas['Luis'] += 3  # Luis ahora tiene 8

print(alimentos_por_personas)


print('-' * 30)

from collections import defaultdict

nombres = ["Ana", "Alberto", "Bruno", "Bea", "Carlos", "Carmen"]

agrupados = defaultdict(list)

for nombre in nombres:
    inicial = nombre[0]
    agrupados[inicial].append(nombre)

print(dict(agrupados))


print('-' * 30)
from collections import defaultdict


ventas = [
    ("pan", 1.0),
    ("leche", 2.5),
    ("pan", 1.1),
    ("huevos", 3.2),
    ("leche", 2.4),
    ("pan", 1.05),
    ("huevos", 3.5),
]

# Creamos un diccionario donde cada clave tendrá una lista como valor
historial_precios = defaultdict(list)

# Agrupamos los precios
for producto, precio in ventas:
    historial_precios[producto].append(precio)

# Mostramos el historial de precios por producto
for producto, precios in historial_precios.items():
    print(f"{producto}: {precios}")

print('-' * 30)



for producto, precios in historial_precios.items():
    promedio = sum(precios) / len(precios)
    print(f"{producto} - Promedio: {promedio:.2f}")


from collections import defaultdict

dd_list = defaultdict(list)
dd_list[2].append(1)
dd_list[3].append(2)

print(dd_list)

dd_dict = defaultdict(dict)
dd_dict['Ronny']['Ciudad'] = 'Lima'
dd_dict['Ronny']['Edad'] = 29
dd_dict['Hade']['Ciudad'] = 'Limad'
dd_dict['Hade']['Edad'] = 22

print(dd_dict)

dd_par = defaultdict(lambda: [0, 0])
dd_par[2][1] = 1

print(dd_par)

# -----------------------------------------------------------------------------------------
# Métodos adicionales:

# move_to_end(key, last=True): Mueve un elemento al final (o al principio si last=False).

# popitem(last=True): elimina un elemento, si last=True se elimina el último elemento, si last=False se elimina el primero.




from collections import OrderedDict

orden = OrderedDict()

orden['juego1'] = 'twister'
orden['juego4'] = 'lata'
orden['juego2'] = 'UNO'
orden['juego3'] = 'charadas'

print(orden)

od = OrderedDict([('manzana', 2), ('banana', 3), ('cereza', 5)])
od.move_to_end('banana')

print("Después de mover 'banana' al final:")
print(od)

# Salida esperada: OrderedDict([('manzana', 2), ('cereza', 5), ('banana', 3)])




# Crear un OrderedDict
od = OrderedDict([('manzana', 2), ('banana', 3), ('cereza', 5)])
print("OrderedDict:")
print(od)


# -------------------------------------------------------------------------------------

print('convinamos defaultdict con orderedDict')

from collections import defaultdict, OrderedDict

# Un OrderedDict que contiene defaultdicts
registro = OrderedDict()

# Agregamos clientes y sus prendas
registro['Ronny'] = defaultdict(list)
registro['Ana'] = defaultdict(list)

# Ronny trae una camisa
registro['Ronny']['camisa'].append('camisa azul')
registro['Ronny']['camisa'].append('camisa blanca')

# Ana trae un pantalón
registro['Ana']['pantalón'].append('jean negro')

# Mostrar registro
for cliente, prendas in registro.items():
    print(f"Cliente: {cliente}")
    for tipo, lista in prendas.items():
        print(f"  {tipo}: {lista}")
