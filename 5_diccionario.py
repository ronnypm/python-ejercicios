diccionario = {'nombre':'ronny','edad':28,'apellido':'pisfil',1:'python'}

diccionario2 = {'nombre':'ronny',
                'edad':28,
                'apellido':'pisfil',
                'lenguajes':{'python','swift','kotlin'},
                1:1.70}


print(diccionario)
print(diccionario2)
print(len(diccionario))
print(len(diccionario2))
print(diccionario['nombre'])

diccionario['nombre'] = 'ROnald'
print(diccionario2['lenguajes']) 
print(diccionario['nombre'])
print(diccionario2[1]) 

diccionario['calle'] = 'calle 1'  #agregamos mas valores al diccionario
print(diccionario)

del (diccionario['calle'])
print(diccionario)

print(diccionario.items())
print(diccionario.keys())
print(diccionario.values())
print(diccionario.fromkeys(('nombre',1))) #creamos diccionarios sin valores

nuevo_diccionario = dict.fromkeys(diccionario)#nos crea un nuevo diccionario a partir del dicionario anterior pero sin sus valores solo las claves,util para cuando querramos usar un diccionario vacio y nosotros poder meter datos despues
print(nuevo_diccionario)

nuevo_diccionario = dict.fromkeys(diccionario,'kenyu')
print(nuevo_diccionario)


