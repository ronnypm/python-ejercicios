# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
   
#     return n * factorial(n-1)


# numero = int(input('Ingrese un numero: '))

# facturas = factorial(numero)

# print(facturas)






# 🛑 Este código es correcto, pero no eficiente para números grandes, ya que recalcula muchos valores.
# def fibonacci(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)

# numero = int(input('Ingrese un numero: '))

# fibo = fibonacci(numero)

# print(fibo)



memo = {}

def fibonacci(n):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0 
    if n == 1:
        return 1
    
    memo[n] = fibonacci(n-1) + fibonacci(n-2)
    return memo[n]

numero = int(input('Ingrese un numero: '))

fibo = fibonacci(numero)

print(fibo)
