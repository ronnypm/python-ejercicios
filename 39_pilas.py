# 🧩 Introducción amigable
# Imagina que estás apilando platos limpios uno encima de otro en la cocina. Cada nuevo plato va arriba de la pila, y cuando necesitas uno, tomas el de arriba. Eso es exactamente cómo funciona una pila (stack) en programación.

# Una pila es una estructura de datos que sigue el principio LIFO: Last In, First Out — el último en entrar, es el primero en salir. En la vida real, además de platos, también usamos pilas con libros, bandejas, o incluso con ropa recién doblada.

# En Python, no necesitas una estructura especial para hacer esto: ¡puedes usar listas!


# stack = []

# stack.append('Plato 1')
# stack.append('Plato 2')
# stack.append('Plato 3')

# print('Pila actual:', stack)

# ultimo = stack.pop()
# print('Elemento retirado: ', ultimo)

# print('Pilas actual despues del pop: ', stack)


# stack = []

# for i in range(5):
#     stack.append(i)

# print('Pilas antes de vaciarla: ', stack)

# #vaciando la pila 

# while stack:
#     print('pop: ', stack.pop())


# print('Pila vacia: ', stack)



# 🧠 Simulación real: Deshacer cambios (undo)
# Muchos editores de texto usan pilas para permitir deshacer acciones:


# acciones = []

# acciones.append('Escribio "hola"')
# acciones.append('Agrego una coma')
# acciones.append('Escribio "mundo"')

# #deshacer la ultima accion

# ultima_accion = acciones.pop()
# print('Deshacer:', ultima_accion)
# print('Acciones restantes: ', acciones)



