# 🧩 Grupos: Organiza tus patrones
# Los grupos te permiten agrupar partes de tu expresión regular para trabajar con ellas como una unidad. Esto es útil tanto para hacer coincidencias complejas como para aplicar cuantificadores a partes específicas de tu patrón.


# 1. Agrupación con paréntesis (...)
# Cuando envuelves un patrón con paréntesis, se convierte en un grupo, y puedes referenciarlo o aplicar operaciones a todo el grupo.

import re

patron = r'(Hola) (mundo)'
texto = 'Hola mundo,Hola universo'
coincidencias = re.findall(patron,texto)
print(coincidencias)


# 2. Referencias a grupos: \1, \2, ...
# Puedes usar las referencias numéricas para hacer coincidir lo mismo que se encontró en un grupo anterior.

patron = r'(\b\w+\b) \1'  # Encuentra palabras repetidas
texto = 'hola hola mundo mundo'
coincidencias = re.findall(patron, texto)
print(coincidencias)