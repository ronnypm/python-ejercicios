# Ejercicio 2

# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.


dict_users = {}
list_users = ["nombre", "edad", "dirección", "teléfono"]

for date in list_users:
    date_user = input(f"Ingrese {date}: ")
    dict_users[date] = date_user


# for key, value in dict_users.items():
#     print(f"{key} {value}")
