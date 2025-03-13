#funciones

def  my_funtion():
    print('Esto es una funcion')

my_funtion()


#################################################################


def sum_two_values(first_value,second_value):
    print(first_value + second_value)

sum_two_values('Hola', 'python')
sum_two_values(4,7353)
sum_two_values(54,7)


#########################################

def sum_two_values_with_return(first_value,second_value):
    return first_value + second_value

my_result = sum_two_values_with_return(10,5)                           

print(my_result)   

print(sum_two_values_with_return(10,5) )

def print_name(name,sur_name):
    print(f'{name} {sur_name}')

print_name(sur_name = 'Pisfil',name = 'Ronny')



def print_name_with_default (name,sur_name,alias = 'Sin alias'):
    print(f'{name} {sur_name} {alias}')

print_name_with_default('Ronny','Pisfil','Fito')
print_name_with_default('Ronny','Pisfil')



def print_text(*texts):
    for text in texts:
        print(text.upper())

print_text('Hola','Python','Ronny')
print_text('Hola')


def suma(num1,num2):
    
    resultado = num1 + num2
    return resultado

almacena_resultado = suma(5,8)
print(almacena_resultado)