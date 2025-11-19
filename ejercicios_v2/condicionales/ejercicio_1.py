# Ejercicio 1

# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

def get_age_user(age: int):
    return "Es mayor de edad" if age >= 18 else "Es menor"


age = int(input("Enter your age: "))
print(get_age_user(age))
