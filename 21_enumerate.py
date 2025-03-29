# 🔹 Ejemplo 1: Lista de estudiantes
# Tienes una lista con los nombres de los estudiantes en un curso, y quieres numerarlos automáticamente para hacer una lista ordenada.

# Entrada:
# 👉 ["Ana", "Carlos", "Luis", "María"]

# Usarías enumerate() en un for para recorrer la lista y agregar un número a cada estudiante.


lista_estudiantes = ["Ana", "Carlos", "Luis", "María"]
lista_estudiantes.sort(key=len)

for indice,nombre in enumerate(lista_estudiantes):
    print(f'{indice + 1}. {len(nombre)}') 



# 🔹 Ejemplo 2: Números pares en una lista
# Tienes una lista de números y quieres encontrar cuáles son pares, pero también necesitas saber en qué posición están dentro de la lista.

# Entrada:
# 👉 [10, 15, 20, 25, 30]


lista_numero = [10, 15, 20, 25, 30]

for 