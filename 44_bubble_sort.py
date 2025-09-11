# numeros = [5, 3, 4,8,13]

# print("Lista original:", numeros)

# for i in range(len(numeros) - 1):
#     print(f"\nComparando {numeros[i]} y {numeros[i+1]}")
#     if numeros[i] > numeros[i + 1]:
#         print(" → Están desordenados. Intercambiando...")
#         numeros[i], numeros[i + 1] = numeros[i + 1], numeros[i]
#     else:
#         print(" → Están bien ordenados. No se hace nada.")
    
#     print("Estado actual de la lista:", numeros)

# print("\nLista final después de una pasada:", numeros)

# numero = [5,3,8,1,6]

# for i in range(len(numero)-1):
#     print({i+1})
#     for j in range(len(numero)-1):
#         print(numero[j]-numero[j+1])
#         if numero[j] > numero[j+1]:
#             numero[j],numero[j+1] = numero[j+1],numero[j]
#             print(f'Intercambio: {numero}')
# print(numero)


def bubble_sort(lista):
    n = len(list)
    for i in range(n):
        for j in range(n) 