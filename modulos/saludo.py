def hola(nombre):
    return f'Hola, {nombre}'

def adios(nombre):
    return f'Adios, {nombre}'


# -----------------------------------------------------
# from nombre_modulo import * (No recomendado)
# from math import *
# print(sqrt(36))  # Pero puede haber conflictos de nombres

# -----------------------------------------------------

# Alias con as

# import math as m
# print(m.pi)

# -----------------------------------------------------

import sys
print(sys.path)