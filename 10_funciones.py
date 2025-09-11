#funciones

# def  my_funtion():
#     print('Esto es una funcion')

# my_funtion()


# #################################################################


# def sum_two_values(first_value,second_value):
#     print(first_value + second_value)

# sum_two_values('Hola', 'python')
# sum_two_values(4,7353)
# sum_two_values(54,7)


# #########################################

# def sum_two_values_with_return(first_value,second_value):
#     return first_value + second_value

# my_result = sum_two_values_with_return(10,5)                           

# print(my_result)   

# print(sum_two_values_with_return(10,5) )

# def print_name(name,sur_name):
#     print(f'{name} {sur_name}')

# print_name(sur_name = 'Pisfil',name = 'Ronny')



# def print_name_with_default (name,sur_name,alias = 'Sin alias'):
#     print(f'{name} {sur_name} {alias}')

# print_name_with_default('Ronny','Pisfil','Fito')
# print_name_with_default('Ronny','Pisfil')



# def print_text(*texts):
#     for text in texts:
#         print(text.upper())

# print_text('Hola','Python','Ronny')
# print_text('Hola')


# def suma(num1,num2):
    
#     resultado = num1 + num2
#     return resultado

# almacena_resultado = suma(5,8)
# print(almacena_resultado)



# # -------------------------------------------------------------------
# def format_message(original_message:str):
#     return f'Hola {original_message}'


# def send_menssage(fomatted_message:str):
#     return "Message sent successfully!" 


# def log_message(original_message:str, status:str) -> str:
#     return f"Registrado: {original_message}\nEstado: {status}"


# if __name__ == "__main__":
#     original_input_message = 'Ronny'
#     formatted_output = format_message(original_input_message)
#     print(f"Paso 1 (Formato): {formatted_output}")

#     send_status = send_menssage(formatted_output)
#     print(f"Paso 2 (Envio): {send_status}")

#     final_log = log_message(original_input_message, send_status)
#     print(f"Paso 3 (Registro Final): {final_log}")




# -------------------------------------------------------------------------------




# def duplicate_number(input_number: float)-> float:
#     duplicate = input_number * 2
#     return duplicate


# def plus_extra(input_number: float) -> float:
#     CONST_EXTRA = 10
#     extra = input_number + CONST_EXTRA
#     return extra

# def quadro(input_number: float) -> float:
#     qr = input_number ** 2
#     return qr

# if __name__ == "__main__":
#     number = 5
#     du_number =  duplicate_number(number)
#     print(f"Numero: {number}")
#     print(f"Numero duplicado: {du_number}")

#     extra = plus_extra(du_number)
#     print(f'Extra: {extra}')

#     qr = quadro(extra)
#     print(f"Cuadro: {qr}") 


# -------------------------------------------------------------------------------

def apply_fixed_discount(amount:float, discount_value:float) -> float:
    return  max(0, amount - discount_value)

def apply_porcentage_discount(amount:float, percentage:float) -> float:
    discount_amount = amount * percentage
    final_amount = amount - discount_amount
    return max(0, final_amount)


def procces_order(order_total:float, discount_function, *arg):
    