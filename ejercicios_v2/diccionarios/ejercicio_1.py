# Ejercicio 1

# Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.


# divisas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}
#
#
# pregunta = input("ingrese su divisa: ")
# for i in divisas.get(pregunta.title()):
# if pregunta.title() == i:
# print("Divisa no encontrada.")
# break
# print(i)


# divisas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}
# new_divisas = divisas.copy()
# print(f"Diccionario copia {new_divisas}")
# new_divisas.update({"Sol": "s/"})
# print(f"Diccionairon con upadate: {new_divisas}")

def mis_diccionarion(un_dicionario: dict, fecha: str) -> dict:
    update_dict = un_dicionario.copy()
    update_dict.update({"fecha": fecha})


diccionario = mis_diccionarion({"saludo": "hola"}, "12/12/12")
print(diccionario)
