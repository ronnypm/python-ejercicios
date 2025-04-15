# diccionario = {'nombre':'ronny','edad':28,'apellido':'pisfil',1:'python'}

# diccionario2 = {'nombre':'ronny',
#                 'edad':28,
#                 'apellido':'pisfil',
#                 'lenguajes':{'python','swift','kotlin'},
#                 1:1.70}


# print(diccionario)
# print(diccionario2)
# print(len(diccionario))
# print(len(diccionario2))
# print(diccionario['nombre'])

# diccionario['nombre'] = 'ROnald'
# print(diccionario2['lenguajes']) 
# print(diccionario['nombre'])
# print(diccionario2[1]) 

# diccionario['calle'] = 'calle 1'  #agregamos mas valores al diccionario
# print(diccionario)

# del (diccionario['calle'])
# print(diccionario)

# print(diccionario.items())
# print(diccionario.keys())
# print(diccionario.values())
# print(diccionario.fromkeys(('nombre',1))) #creamos diccionarios sin valores

# nuevo_diccionario = dict.fromkeys(diccionario)#nos crea un nuevo diccionario a partir del dicionario anterior pero sin sus valores solo las claves,util para cuando querramos usar un diccionario vacio y nosotros poder meter datos despues
# print(nuevo_diccionario)

# nuevo_diccionario = dict.fromkeys(diccionario,'kenyu')
# print(nuevo_diccionario)


#Ejercicicos diccionarions

# ✅ Ejercicio 1: Contar letras en una palabra

# palabra = 'banana'
# conteo = {}

# for letra in palabra:
#     actual = conteo.get(letra,0)
#     conteo[letra] = actual + 1

# print(conteo)

# frase = 'hola mundo hola programador mundo'
# palabras = frase.split()
# conteo_palabra = {}

# for palabra in palabras:
#     actual = conteo_palabra.get(palabra, 0)
#     conteo_palabra[palabra] = actual + 1

# print(conteo_palabra)


mi_dict = {'nombre': 'Ronny','edad':29}
# resultado = mi_dict.get('nombre','desconocido')#Ronny
resultado = mi_dict.get('altura',0)#No definido


print(resultado)



colores = {'rojo': '#FF0000', 'azul': '#0000FF'}

# ¿Qué devuelve esto?
print(colores.get('verde', 'No encontrado'))




