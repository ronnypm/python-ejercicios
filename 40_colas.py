# 🚌 Usando Colas (Queues) con collections.deque en Python
# 🎯 Introducción amigable
# Imagina que estás haciendo fila para comprar entradas al cine. Llegas al final de la fila y cuando llega tu turno, eres el primero en ser atendido. Eso es una cola: el primero en entrar es el primero en salir, lo que en programación se conoce como FIFO: First In, First Out.

# En Python, para trabajar eficientemente con colas, se recomienda usar collections.deque en lugar de listas comunes.


# 🧠 Fundamentos técnicos
# ¿Qué es una cola?
# Una cola (queue) es una estructura de datos donde los elementos se insertan por un extremo (el final) y se eliminan por el otro (el inicio). Ideal para representar procesos en orden de llegada.

# ¿Por qué no usar listas normales?
# Aunque las listas tienen .append() y .pop(0), esta última operación es lenta porque todos los elementos deben moverse. Para evitarlo, usamos deque, que está optimizada para operaciones en ambos extremos.


# append(x) Agrega al final de la cola 
# popleft() Elimina del inicio (FIFO)
# appendleft(x) Agragar al inicio(opcional)
# pop() Elimina del final (poco usado aqui)


from collections import deque

# cola = deque()


# cola.append('Cliente 1')
# cola.append('Cliente 2')
# cola.append('Cliente 3')


# print(f'Cola actual {cola}')


# #Eliminar elementos (deque)

# atendido = (cola.popleft())
# print('Atendiendo a:', atendido)


# print('Cola despues de atender:', cola)







# 🎮 Aplicaciones reales de una cola
# ⏳ Simulación de impresora

# def simular_impresora(tareas):
#     cola_impresion = deque(tareas)

#     while cola_impresion:
#         tarea = cola_impresion.popleft()
#         print(f'Imprimiendo {tarea}')

# simular_impresora(['Factura 001', 'Carta presentacion', 'Informacion final'])


# 🚦 Control de tráfico (por orden de llegada)

vehiculos = deque()

vehiculos.append('Auto rojo')
vehiculos.append('camion azul')
vehiculos.append('Moto negra')

while vehiculos:
    print(f'Pasa {vehiculos.popleft()}')






# 🧪 Buenas prácticas
# Siempre usa deque si necesitas eficiencia en inserciones y extracciones al inicio de la estructura.
# No hagas pop(0) en listas si puedes evitarlo: es mucho más lento que popleft() en deque.
# Puedes establecer un máximo con deque(maxlen=n) para implementar buffers circulares o colas limitadas.