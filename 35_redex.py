# 🌱 Introducción amigable
# Las expresiones regulares (regex) son una forma de buscar patrones en texto, como si le dieras a Python una lupa inteligente.

# En vez de buscar una palabra exacta, puedes decirle cosas como:

# “Encuentra cualquier número”
# “Busca letras que estén al principio de una línea”
# “Detecta si un texto termina con .com”
# Y eso lo logras con clases de caracteres y aserciones, que son como los superpoderes del buscador de texto.


import re

patron = r'\d+' #con el signo mas si hay un numero con dos digitos no los separa[57] pero si no lo ponemos separa los numeros por separado [5,7]
texto = 'Hay 3 gatos y 57 perros.'
concidencia = re.findall(patron,texto)
# print(concidencia) #['3', '57']
# \D (mayúscula) es lo opuesto: cualquier cosa que no sea un dígito.

#--------------------------------------------------------------------------------------
#  \w — Carácter de palabra (letras, números y _)

patron = r'\w'
texto = 'Hola_123!'
concidencia = re.findall(patron,texto)
#print(concidencia) # ['H', 'o', 'l', 'a', '_', '1', '2', '3']

#tambien se puede hacer asi 
re.findall(r'\w', 'Hola_123!')  # ['H', 'o', 'l', 'a', '_', '1', '2', '3']

#--------------------------------------------------------------------------------------

# \s — Espacio en blanco (espacio, tab, salto de línea)

patron = r'\s' #busca todo que sea ' ', '\t', '\n' con la ese mayuscula /S todo lo contrario tod lo que no sea ' ', '\t', '\n'
texto = 'Hola mundo\t2025'
concidencia = re.findall(patron,texto)
#print(concidencia)# [' ', '\t']

#Tambien se puede hacer asi 

re.findall(r'\s', 'Hola mundo\t2025')  # [' ', '\t']



#--------------------------------------------------------------------------------------


re.findall(r'[aeiou]', 'Python es divertido')  # ['o', 'e', 'u', 'i', 'o']



#--------------------------------------------------------------------------------------


#busca todas las letras de a a la z en minusculas, de esta forma se agregan tambien a las letra mayusculas [A-Za-z]
re.findall(r'[a-z]', 'Hola123')  # ['o', 'l', 'a'])


#--------------------------------------------------------------------------------------

# Negación: [^...] (todo excepto),  El ^ dentro de [] niega la clase.

negacion = re.findall(r'[^0-9]', 'Casa 45') 
#print(negacion)#['C', 'a', 's', 'a', ' ']



#--------------------------------------------------------------------------------------

# 🧨 Aserciones: no consumen texto, solo lo verifican
# Las aserciones te permiten decir cosas como:

# "Solo si está al inicio"
# "Solo si está antes de algo"
# "Solo si está seguido por algo"
# 1. ^ — Inicio de línea

# ^ — Inicio de línea
resultado = re.findall(r'^Hola','Hola mundo') #inicio de cadena de texto
# print(resultado)#['Hola']

#$ — Fin de línea
resultado = re.findall(r'mundo$','Hola mundo') #finla de cadena de texto
# print(resultado)#['mundo']

# \b — Límite de palabras
#🚧 Útil para evitar falsos positivos como "Holanda".
limite_palabra = re.findall(r'\bHola\b', 'Hola mundo y Holanda')  # ['Hola']
# print(limite_palabra)


#(?=...) — Lookahead positivo: lo que viene después

lookahead = re.findall(r'\d(?=€)', '5€, 10€, 20$')  # ['5', '0']
# print(lookahead)

#(?!...) — Lookahead negativo: lo que no viene después

Lookahead_negativo = re.findall(r'\d(?!€)', '5€, 10€, 20$')  # ['1', '2', '0']
print(Lookahead_negativo)


#  (?<=...) y (?<!...) — Lookbehind positivo/negativo

# (?<=\$) → solo busca si antes hay un símbolo $
# \d+ → uno o más dígitos
uno = re.findall(r'(?<=\$)\d+', 'Total: $45')  # ['45']
dos = re.findall(r'(?<!\$)\d+', 'Total: $45 y 30')  # ['30']
# (?<!\$) → lookbehind negativo: busca dígitos que NO están precedidos por $


print(uno)
print(dos)