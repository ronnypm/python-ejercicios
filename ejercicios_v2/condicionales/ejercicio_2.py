# Ejercicio 2
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.


def review_password(password: int):
    my_password = "hola"

    return "contrasena correcta" if password.lower() == my_password else "incorrecto"


password = str(input("Contrasena: "))
print(review_password(password))
