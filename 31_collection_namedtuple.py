# namedtuple: Tuplas con nombre
# !¿Cuándo usarlo?
# !Cuando necesitas una estructura ligera tipo objeto, inmutable y fácil de entender.


from collections import namedtuple

persona = namedtuple('Persona', ['nombre','edad'])
#creamos instancias
ronny = persona(nombre='Ronny', edad=29)

print(ronny.nombre)
print(ronny[1])

# -----------------------------------------------------------------------------------------------------

prenda = namedtuple('Prenda', ['tipo','color','cliente'])
#creamos instancias
p1 = prenda(tipo='Pantalon', color='Negro', cliente='Ronny')
p2 = prenda(tipo='Camisa', color='Plomo', cliente='Genaro')

print(p1)
print(p1.tipo)
print(p1[0])
print(p1.cliente)
print(p1.color)
#Extra: convertir a diccionario
print(p1._asdict())



# -----------------------------------------------------------------------------------------------------
print('-' * 70)


from collections import namedtuple, defaultdict

#Paso 1:  defenimos la estructura de una prenda
Prenda = namedtuple('Prenda', ['Tipo', 'Color', 'Fecha_entrega'])

#Paso 2: Creamos un defaultdict donde la clave es el cliente el valos es una lista de prendas
registro_prenda = defaultdict(list)

#Paso 3: Agregamos prendas para distintos clientes

registro_prenda['Ronny'].append(Prenda('Pantalon','Negro','2025-04-10'))
registro_prenda['Ronny'].append(Prenda('Camisa','Blanco','2025-04-10'))
registro_prenda['Juan'].append(Prenda('Pantalon','Azul','2025-04-15'))


#Paso 4: Mostramos las prendas de cada cliente

for cliente, prendas in registro_prenda.items():
    print(f'\n cliente: {cliente}')
    for prenda in prendas:
        print(f"👕 Tipo: {prenda.Tipo}, 🎨 Color: {prenda.Color}, 📅 Entrega: {prenda.Fecha_entrega}")











