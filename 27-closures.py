# def make_avarages():
#     series = []

#     def avarages(new_Values):
#         series.append(new_Values)
#         total = sum(series)
#         return total / len(series)
    
#     return avarages


# avg = make_avarages()
# print(avg(10))
# print(avg(11))
# print(avg(12))


# def saludar(nombre):
#     def mensaje():
#         return f'Hola, {nombre}'
#     return mensaje

# saludo = saludar('Ana')
# print(saludo())

# --------------------------------------------------------------------

# Ejercicio 1: Contador con closure
# Un contador es una función que, al ser llamada varias veces, incrementa su valor. Usaremos un closure para que la función conserve el valor del contador entre llamadas.

# def contador():
#     cuenta = 0

#     def incrementar():
#         nonlocal cuenta
#         cuenta += 1
#         return cuenta
#     return incrementar

# mi_contador = contador()

# print(mi_contador())
# print(mi_contador())
# print(mi_contador())

# --------------------------------------------------------------------
# Ejercicio 2: Función que genera multiplicadores
# Vamos a crear una función multiplicador que devuelva una función que multiplica un número dado por un valor específico. El valor de multiplicación se guarda en un closure.


# def multiplicador(factor):
#     def multiplicar(numero):
#         return numero * factor
#     return multiplicar

# doblar = multiplicador(2)
# triplicar = multiplicador(3)

# print(doblar(5))
# print(triplicar(5))


# --------------------------------------------------------------------


# Ejercicio 3: Función de suma con múltiples valores
# Imagina que queremos crear una función que sume varios valores. Podemos usar un closure para mantener un acumulador de las sumas.

# def acumulador():
#     suma = 0 
#     def agregar(valor):
#         nonlocal suma
#         suma += valor
#         return suma
#     return agregar 

# sumar = acumulador()

# print(sumar(5))
# print(sumar(10))
# print(sumar(100))



# --------------------------------------------------------------------

# Ejercicio 4: Función de potencia
# Vamos a crear una función que devuelve una función para elevar un número a una potencia específica.

# def potencian(exponente):
#     def elevar(base):
#         return pow(base,exponente)
#     return elevar

# mi_cuadrado = potencian(2)

# print(mi_cuadrado(5))


# --------------------------------------------------------------------

# Ejercicio 5: Función que devuelve una secuencia de operaciones
# Supongamos que queremos aplicar varias operaciones matemáticas en un número. Podemos usar un closure para encadenar las operaciones.

# def operaciones_iniciales(valor_iniciales):

#     valor = valor_iniciales

#     def agregar(num):
#         nonlocal valor
#         valor += num
#         return valor


#     def restar(num):
#         nonlocal valor 
#         valor -= num
#         return valor
    

#     def multiplicar(num):
#         nonlocal valor 
#         valor *= num 
#         return valor
    
#     def dividir(num):
#         nonlocal valor
#         valor /=  num
#         return valor
    
#     return agregar, restar, multiplicar, dividir


# agregar, restar , multiplicar, devidir = operaciones_iniciales(10)

# print(agregar(10))
# print(restar(3))
# print(multiplicar(2))
# print(devidir(10))


# --------------------------------------------------------------------

# 🔹 Ejercicio 1: Closure básico
# Objetivo: Crear una función que devuelva otra función, y que esta función interna recuerde un valor que se le pasó a la externa.


# def crera_funcion(valor_que_recordar):
#     def funcion_interna(parametro):
#         return parametro + valor_que_recordar
#     return funcion_interna

# suma_5 = crera_funcion(5)

# print(suma_5(10))

# suma_20 = crera_funcion(20)

# print(suma_20(13))

# --------------------------------------------------------------------

# 🔹 Ejercicio 2: Contador usando Closure
# Objetivo: Crear una función que devuelva un contador. El contador debe empezar en un número dado y cada vez que llames a la función, debe incrementar ese número

# def crear_contador():
#     suma = 0


#     def wrapper(valor):
#         nonlocal suma
#         suma += valor
#         return suma
#     return wrapper


# total_final = crear_contador()

# print(total_final(10))
# print(total_final(20))
# print(total_final(50))
# print(total_final(50))






# --------------------------------------------------------------------

# 🔹 Ejercicio 3: Calculadora básica con Closure
# Objetivo: Crear una función que devuelva otra función para realizar una operación matemática (como suma, resta, multiplicación, etc.) y que mantenga el primer valor de la operación para realizar la operación cada vez que se le pase otro número.

def calculadora(valor_inicial):

    valor = valor_inicial

    def suma(numero):
        nonlocal valor
        valor += numero
        return valor


    def resta(numero):
        nonlocal valor
        valor -= numero
        return valor


    def multiplicacion(numero):
        nonlocal valor
        valor *= numero
        return valor
    
    return suma, resta, multiplicacion


suma, restar, multi = calculadora(10)


print(suma(10))
print(restar(10))
print(multi(10))

















# --------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------
