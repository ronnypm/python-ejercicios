# try:
#     numero = int(input("Ingresa un número: "))
#     print(10 / numero)
# except ValueError:
#     print("Debes ingresar un número.")
# except ZeroDivisionError:
#     print("No puedes dividir entre cero.")




# try:
#     numero = int(input("Número: "))
# except ValueError:
#     print("No es válido.")
# else:
#     print("Todo salió bien.")
# finally:
#     print("Este bloque siempre se ejecuta.")



# try:
#     1 / 0
# except ZeroDivisionError as e:
#     print(f"Ocurrió un error: {e}")



# Creamos una nueva clase que hereda de Exception
# class SaldoInsuficienteError(Exception):
#     pass

# def retirar(saldo, monto):
#     if monto > saldo:
#         raise SaldoInsuficienteError("No hay suficiente saldo para esta operación.")
#     return saldo - monto

# # Probando la función
# try:
#     retirar(100, 200)
# except SaldoInsuficienteError as e:
#     print(f"Error: {e}")

# # 💡 Esto genera un error específico que puedes capturar, loguear o mostrar al usuario según el contexto.



# try:
#     resultado = 10 /0
# except ZeroDivisionError:
#     print('No se puede dividir entre cero. ')


# def retirar(saldo, monto ):
#     if monto > saldo:
#         raise ValueError('Saldo insuficiente.')
#     else:
#         print(saldo - monto)

# retirar(200,50)


# try:
#     saldo = 400
#     monto = 200

#     if monto > saldo:
#         raise ValueError('Saldo insuficiente')
#     else:
#         print( saldo - monto)
# except ValueError as e:
#     print(f'Erro: {e}')


# def transferir(dinero_disponible, monto_transferible):
#     if monto_transferible > dinero_disponible:
#         raise ValueError('No tienes suficiente dinero para transferir')
#     return dinero_disponible - monto_transferible

# try:

#     transferir(1000,300)
# except ValueError as e:
#     print(f'Erro: {e}')


# 📌 Ejercicio 1 (Nivel básico)
# Tienes un programa que pide la edad de una persona. Si la edad ingresada es un número negativo, debe lanzarse un error con un mensaje que diga:
# ❌ "La edad no puede ser negativa."

# ✅ Objetivo:

# Usar raise para detectar este error.

# Usar try-except para manejar el error y evitar que el programa se cierre.

# def edad_de_usuario(edad):

#     if edad <= 0:
#         raise ValueError ('❌ La edad no puede ser negativa.')
#     return f'{edad} es correcta'

# try:
#     edad_usuario = int(input('Ingrese su edad: '))
#     print(edad_de_usuario(edad_usuario))
# except ValueError as e:
#     print(f'Error: {e}')

# 🔹 Enunciado:
# Imagina que estás programando un sistema bancario. Debes escribir una función que verifique si un usuario puede realizar un retiro de dinero. Si el monto a retirar es mayor que el saldo disponible, la función debe lanzar una excepción con un mensaje adecuado. Luego, maneja el error para que el programa no se detenga abruptamente.

# 📌 Preguntas para ayudarte a pensar:

# ¿Qué tipo de excepción podrías usar aquí?

# ¿Dónde colocarías raise?

# ¿Cómo manejarías el error con try-except?

# ¡Dale! Escríbelo y dime cómo te sale. 💪🔥


# def usuario_retiro(monto_retirar,Saldo_cuenta):
#     if monto_retirar > Saldo_cuenta:
#         raise ValueError ('Saldo insuficiente')
#     return f'Usted retiro {monto} S/.'


# while True:
#     try:
#         monto = int(input('Ingrese el monto a retirar: '))
#         print(usuario_retiro(monto,1000))
#         break
#     except ValueError:
#         print('❌ Error: Debe ingresar un número válido."')

# print('El programa sigue')



# Ejercicio: Validación de Correo Electrónico
# Un usuario debe ingresar su correo electrónico, pero queremos asegurarnos de que sea válido.

# 📌 Reglas:

# Debe contener un @.

# Debe tener un dominio válido (.com, .net, .org, etc.).

# No puede estar vacío.

# Si el correo no cumple estas condiciones, lanzaremos una excepción personalizada con raise.

# 💡 Objetivo:

# Usar raise para generar un error si el correo es inválido.

def validar_correo(correo):
    # Verificar que el correo contenga '@' y que termine con un dominio válido
    if '@' not in correo or not correo.endswith(('.com', '.net', '.org')):
        raise ValueError('❌ Correo no válido. Debe contener "@" y terminar en ".com", ".net" o ".org"')
    return '✅ Correo válido'

# Probando
try:
    while True:
        try:
            email = input('Ingrese su correo: ')
        
            # Verificar que el correo no sea solo números
            if email.isdigit():
                raise ValueError("❌ El correo no puede ser solo números.")
        
            # Verificar que el correo no sea solo letras
            if email.isalpha():
                raise ValueError("❌ El correo no puede ser solo letras.")
        
            print(validar_correo(email))
            break
        except ValueError as e:
            print(f'Error: {e}')
except KeyboardInterrupt:
    print('\n❌ Programa interrumpido por el usuario')

