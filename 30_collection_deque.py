from collections import deque

cola_juego = deque(['UNO', 'twister'])
cola_juego.append('charadas')#Agrafa al final
cola_juego.appendleft('pictionary')#Agrega al inicio

print(cola_juego)


from collections import deque

# Crear una deque
dq = deque()

# Agregar al final
dq.append('camisa')
dq.append('pantalón')

# Agregar al inicio
dq.appendleft('chaqueta')

print(dq)  # deque(['chaqueta', 'camisa', 'pantalón'])

# Quitar del final
dq.pop()  # 'pantalón'

# Quitar del inicio
dq.popleft()  # 'chaqueta'

print(dq)  # deque(['camisa'])


# --------------------------------------------------------------------------------
# Ejemplo de rotate:
print('\nrotate')
print('deque([1, 2, 3, 4, 5])')
dq = deque([1,2,3,4,5])
dq.rotate(2)
print(dq)

dq.rotate(-1)
print(dq)


print('-' * 30)
print('Cola (FIFO – First In, First Out)')
from collections import deque

cola = deque()

# Agregamos elementos
cola.append("cliente1")
cola.append("cliente2")
cola.append("cliente3")

print("Cola inicial:", cola)

# Atendemos al primero que llegó
primero = cola.popleft()
print("Atendiendo a:", primero)
print("Cola después de atender:", cola)

# -------------------------------------------------------------
print('-' * 30)
print(' Pila (LIFO – Last In, First Out)')

from collections import deque

pila = deque()

# Apilamos elementos
pila.append("archivo1")
pila.append("archivo2")
pila.append("archivo3")

print("Pila inicial:", pila)

# Sacamos el último que pusimos
ultimo = pila.pop()
print("Desapilando:", ultimo)
print("Pila después de sacar:", pila)

# -------------------------------------------------------------
print('-' * 30)

from collections import deque

# Cola de clientes que llegan a la sastrería
cola_clientes = deque()

# Llegan clientes
cola_clientes.append("Ronny")
cola_clientes.append("Lucía")
cola_clientes.append("Pedro")

print("Clientes en espera:", cola_clientes)

# Atendemos al primero que llegó
atendido = cola_clientes.popleft()
print("Atendiendo a:", atendido)
print("Clientes restantes:", cola_clientes)


# -------------------------------------------------------------
print('-' * 30)

from collections import deque

# Pila de camisas para planchar
pila_prendas = deque()

# Se apilan prendas
pila_prendas.append("Camisa blanca")
pila_prendas.append("Camisa azul")
pila_prendas.append("Camisa negra")

print("Prendas apiladas:", pila_prendas)

# Se toma la última prenda para planchar
ultima_prenda = pila_prendas.pop()
print("Planchando:", ultima_prenda)
print("Prendas restantes:", pila_prendas)
