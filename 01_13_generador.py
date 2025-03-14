# def generar_pares(limite):
    
#     num = 1 


#     while num < limite:
#         yield num*2
#         num +=1 

   
# devulve_pares = generar_pares(10)

# print(next(devulve_pares))


def devuleve_ciudades(*ciudades):
    
    for elemento in ciudades:
        #for sub_elemento in elemento:
            yield from elemento

ciudades_devueltas = devuleve_ciudades('Lima','Arequipa','Trujillo')

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))



# Ejercicio 2:
# Crea un generador que reciba una lista de palabras y devuelva solo aquellas que tienen más de 5 letras.


