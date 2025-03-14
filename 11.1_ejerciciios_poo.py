# !Ejercicio 1: Control de una Bicicleta 🚴
# !Crea una clase Bicicleta con los siguientes atributos y métodos:

# !Atributos:
# !color (cadena de texto)
# !tipo (montaña, ruta, urbana)
# !velocidad (inicialmente en 0 km/h)
# !Métodos:
# !pedalear(vel) → Aumenta la velocidad en vel km/h.
# !frenar() → Reduce la velocidad a 0 km/h.
# !estado() → Muestra el color, tipo y la velocidad actual de la bicicleta.
# 📌 !Tu tarea: Implementa la clase y prueba crear una bicicleta, !hacer que pedalee y frene.

# !Cuando lo tengas listo, envíame tu código y revisamos antes de darte el siguiente ejercicio. ¡Tú puedes! 🚀


# class Bicicleta():
#     def __init__(self,color, tipo):
#         self.__color = color
#         self.__tipo =  tipo
#         self.__velocidad = 0
    
#     def pedalear(self,vel):
#         self.__velocidad += vel
#         print(f'La bicicleta ha acelerado, nueva velocidad {self.__velocidad} km')


#     def frenar(self,decremento):
#         self.__velocidad = max(0, self.__velocidad - decremento)
        

#     def estado(self):
#         return f'Color: {self.__color}, tipo: {self.__tipo}, velocidad: {self.__velocidad} Km/h'
    
# mi_bicileta = Bicicleta('verde','Montana')
# print(mi_bicileta.estado())

# mi_bicileta.pedalear(10)
# mi_bicileta.frenar(5)
# print(mi_bicileta.estado())


# !🚀 Ejercicio:
# !Crea una clase Avion con los siguientes atributos privados:

# !__modelo (por ejemplo, "Boeing 747")
# !__capacidad (cantidad de pasajeros)
# 1__altitud (inicia en 0)
# !Y métodos:

# !despegar(altura): Aumenta la altitud.
# !aterrizar(): Reduce la altitud a 0.
# !estado(): Muestra el modelo, capacidad y altitud actual.
# !💡 Prueba creando un avión y hazlo despegar y aterrizar.



# class Avion():
#     def __init__(self,modelo, capacidad):
#         self.__modelo = modelo 
#         self.__capacidad = capacidad 
#         self.__altitud = 0

#     def depegar(self,altura):
#         self.__altitud += altura 
#         print(f'El avion se encuentra a un altura de {self.__altitud} metros')
        

#     def aterrizar(self,aterrizaje):
#         self.__altitud = max(0, self.__altitud - aterrizaje )

#         if self.__altitud == 0:
#             print('El avión ha aterrizado completamente.')
#         else:
#             print(f'El avión ha descendido, pero aún está a {self.__altitud} metros')


#     def estado(self):
        
#         return f'El avion esta en este momento en vuelo!' if self.__altitud > 0 else 'El avion ya aterrizo' 



#     def resumen(self):
#         return f'Modelo: {self.__modelo}, Capacidad: {self.__capacidad}, Altidud: {self.__altitud}'

# mi_avion = Avion('Avianca',2000)

# mi_avion.depegar(1500)
# mi_avion.aterrizar(1500)
# print(mi_avion.estado())
# print(mi_avion.resumen())


# Ejercicio 3: La Cafetera ☕
# Crea una clase Cafetera con los siguientes atributos y métodos:

# Atributos:
# __capacidad_maxima: la cantidad máxima de café que puede contener la cafetera.
# __cantidad_actual: la cantidad actual de café en la cafetera.
# Métodos:
# llenar_cafetera(): llena la cafetera hasta su capacidad máxima.
# servir_taza(cantidad): resta la cantidad de café servida. Si no hay suficiente, sirve lo que quede y avisa que la cafetera está vacía.
# vaciar_cafetera(): deja la cafetera sin café.
# agregar_cafe(cantidad): añade café a la cafetera sin sobrepasar la capacidad máxima.
# estado(): muestra la cantidad actual de cafe


# class Cafetera():
#     def __init__(self, capacidad_maxima, cantidad_actual):
#         self.__capacidad_maxima = int(capacidad_maxima)
#         self.__cantidad_actual = int(cantidad_actual)

#     def llenar_cafetera(self):
#         self.__cantidad_actual = self.__capacidad_maxima  # Llena la cafetera al máximo

#     def servir_taza(self, cantidad):
#         if cantidad > self.__cantidad_actual:
#             print("No hay suficiente café, se sirve lo que queda.")
#             self.__cantidad_actual = 0
#         else:
#             self.__cantidad_actual -= cantidad
#             print(f"Se sirvieron {cantidad} ml de café.")

#     def agregar_cafe(self, cantidad):
#         if self.__cantidad_actual + cantidad > self.__capacidad_maxima:
#             print("Se desborda la cafetera, se llena al máximo.")
#             self.__cantidad_actual = self.__capacidad_maxima
#         else:
#             self.__cantidad_actual += cantidad
#             print(f"Se agregaron {cantidad} ml de café.")

#     def estado(self):
#         return f'La cafetera tiene una capacidad máxima de {self.__capacidad_maxima} ml y actualmente contiene {self.__cantidad_actual} ml de café.'

# mi_cafetera = Cafetera(1000, 500)

# mi_cafetera.llenar_cafetera()  # Llenar la cafetera
# print(mi_cafetera.estado())  # Ver el estado actual
# mi_cafetera.servir_taza(300)  # Servir una taza de 300 ml
# print(mi_cafetera.estado())  
# mi_cafetera.agregar_cafe(200)  # Agregar 200 ml de café
# print(mi_cafetera.estado())  
