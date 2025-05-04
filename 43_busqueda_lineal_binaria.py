# 🧩 Introducción
# Imagina que tienes una lista de nombres y quieres saber si “Carlos” está en ella. ¿Revisarías uno por uno o irías al medio para reducir el esfuerzo? En programación, esto se traduce en algoritmos de búsqueda, y los dos más conocidos son:

# Búsqueda lineal (Linear Search)
# Búsqueda binaria (Binary Search)



# 1️⃣ Búsqueda Lineal: simple y directa
# ✅ ¿Qué es?
# La búsqueda lineal recorre uno por uno todos los elementos de una lista hasta encontrar el que buscas (o llegar al final).

# 📦 Ejemplo de la vida real: Buscar un número de teléfono en una libreta desordenada. Empiezas desde arriba y revisas uno a uno.

# 🧠 Características:
# Funciona con listas desordenadas o ordenadas
# Tiene una complejidad O(n) → empeora con listas largas
# Es fácil de implementar


# def busqueda_lineal(lista,objetivo):
    
#     for i in range(len(lista)):
#         if lista[i] == objetivo:
#             return i # Devuelve la posición donde lo encontró
#     return -1  # Si no lo encontró
    
# numeros = [10, 23, 45, 70, 11, 15]

# print(busqueda_lineal(numeros,1))


#Forma mas pythonica
# def busqueda_lineal(lista, objetivo):
#     for i, elemento in enumerate(lista):
#         if elemento == objetivo:
#             return i
#     return -1




# ❓ ¿Por qué se devuelve -1 si no lo encuentra?
# Porque -1 se usa como una señal clara de que no encontró el elemento en la lista.
# Python no tiene valores "nulos" para enteros como otros lenguajes, así que se usa -1 como código de error o ausencia.






# ----------------------------------------------------------------------


# 2️⃣ Búsqueda Binaria: precisa y eficiente
# ✅ ¿Qué es?
# La búsqueda binaria divide el arreglo a la mitad repetidamente, descartando la mitad que no puede contener el valor. Solo funciona si la lista está ordenada.

# 🗂 Ejemplo de la vida real: Buscar un nombre en un diccionario. Vas al medio, ves si está antes o después, y te enfocas solo en esa parte.
# 🧠 Características:
# Solo funciona en listas ordenadas
# Mucho más eficiente: complejidad O(log n)
# Usa recursión o iteración


# def busqueda_binari(lista,objetivo):
#     izquierda = 0 
#     derecha = len(lista) -1 

#     while izquierda <=  derecha:
#         medio = (izquierda + derecha) // 2
#         if lista[medio] == objetivo:
#             return medio
#         elif lista[medio] < objetivo:
#             izquierda = medio + 1
#         else:
#             derecha = medio - 1 
        
#     return -1

# numeros = [10, 15, 23, 45, 70]
# print(busqueda_binari(numeros, 45))


import bisect

lista = [10, 15, 23, 45, 70]
indice = bisect.bisect_left(lista, 23)
print(indice)  # Output: 2