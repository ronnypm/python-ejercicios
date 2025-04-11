# Concepto Básico de Decoradores
# Un decorador es una función que recibe otra función como argumento y devuelve una nueva función que generalmente extiende o modifica el comportamiento de la función original.




# !def saludo():
#  !   return "¡Hola!"

# !print(saludo())

# def agregar_saludo(func):
#     def nueva_funcion():
#         return f'Bienvenido {func()}'  
#     return nueva_funcion


# @agregar_saludo
# def saludo():
#     return 'hola'


# print(saludo())


#------------------------------------------------------------


# def funcion_decorador(func):
    
#     def funcion_interior(*args,**kwargs):

#         #Acciones adicionales que decoran 

#         # print('Vamos a realizar un calculo:')

#         func(*args,**kwargs)

#         #accion final del decorador
#         # print('Se ha terminado el calculo')

#     return funcion_interior




# --------------------------------------------------------

# class MiExcepcion(Exception):
#     pass

# # Decorador
# def contar_llamadas(func):
#     def wrapper(*args, **kwargs):
#         wrapper.contador += 1
#         print(f"📞 La función '{func.__name__}' ha sido llamada {wrapper.contador} veces.")
#         return func(*args, **kwargs)
    
#     wrapper.contador = 0
#     return wrapper

# # Función de ejemplo
# @contar_llamadas
# def ejemplo():
#     print("¡Función ejecutada!")

# # Usando la clase de excepción en un lugar adecuado
# try:
#     raise MiExcepcion("¡Algo salió mal!")
# except MiExcepcion as e:
#     print(f"Excepción capturada: {e}")
# ------------------------------------------------------------

# Ejercicio 1: Decorador para verificar si todos los argumentos son números positivos
# Vamos a crear un decorador que verifique si todos los argumentos pasados a una función son números positivos. Si algún número no es positivo, lanzaremos una excepción personalizada. Después, usaremos este decorador en una función que calcule el promedio de los números pasados.

# Objetivo: Practicar el uso de decoradores y excepciones personalizadas.

# Crea una excepción personalizada llamada NumeroPositivoError.

# Escribe un decorador llamado verificar_positivos que verifique que todos los números pasados a la función sean positivos.

# Crea una función llamada promedio que calcule el promedio de los números pasados a ella.

# Aplica el decorador a la función promedio.


# class NumeroPositivoError(Exception):
#     pass


# def verificar_positivo(func):
#     def wrappe(*args,**kwargs):
#         if any (numero < 0 for numero in args):
#             raise NumeroPositivoError ('Todos los numeros tiene que ser positiv')
#         return func(*args,**kwargs)
#     return wrappe



# @verificar_positivo
# def promedios(*args):

#     promedios = sum(args)/len(args)
#     return promedios



# def promedio_resutaldo(promedio,*args):
#     try:
#         return round(promedio(*args),2)
#     except NumeroPositivoError as e:
#         return f'Error, {e}'




# print(promedio_resutaldo(promedios,14,5,16))
# print(promedio_resutaldo(promedios,14,-6,16))
        


# ------------------------------------------------------------


# Ejercicio 2: Decorador de conteo de ejecuciones
# Objetivo: Practicar el uso de decoradores para contar cuántas veces se ha ejecutado una función.

# Instrucciones:

# Crea un decorador llamado contador_ejecuciones que lleve un registro de cuántas veces se ha llamado una función.

# Aplica este decorador a una función llamada saludar que imprima un saludo.

# El decorador debe imprimir el número de veces que la función ha sido llamada cada vez que se invoque la función decorada.

# def contador_ejecuciones(func):
#     def wrappe(*args,**kwargs):
#         wrappe.contador += 1
#         print(f'La funcion {func.__name__} ha sido llamada {wrappe.contador}')
#         return func(*args,**kwargs)
#     wrappe.contador = 0
#     return wrappe



# @contador_ejecuciones
# def saludar ():
#     print('Hola')


# saludar()
# saludar()
# saludar()


# ------------------------------------------------------------

# Ejercicio 3: Calculadora con múltiples operaciones
# Objetivo: Practicar decoradores para validar los tipos de datos y usar funciones para múltiples operaciones.

# Enunciado:
# Crea una excepción personalizada llamada OperacionInvalidaError.

# Escribe un decorador validar_numeros que verifique que todos los argumentos de la operación sean números.

# Escribe funciones para realizar cada operación: sumar, restar, multiplicar, y dividir.

# Aplica el decorador validar_numeros a todas las funciones de operaciones.

# Usa un bloque try-except para manejar las excepciones.

# Requisitos:
# El decorador validar_numeros debe asegurarse de que todos los argumentos sean números (puedes usar isinstance(arg, (int, float))).

# Si los argumentos no son válidos, debe lanzarse la excepción personalizada OperacionInvalidaError.

# Las operaciones deben realizarse solo si todos los argumentos son válidos, de lo contrario debe manejarse el error.

# Puntos importantes:
# Asegúrate de manejar excepciones adecuadamente, lanzando la excepción personalizada cuando los argumentos no sean correctos.

# Aplica el decorador a todas las funciones de operaciones.

# Usa bloques try-except para gestionar los errores.



class OperacionesInvalidaError(Exception):
    pass


def validar_numero(func):
    def wrapper(*args,**kwargs):
        
        return func(*args,**kwargs)
    return wrapper


