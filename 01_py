list_1 = [1,4,9,16,25]

print(list_1[0]) #muestra 1
print(list_1[2]) #muestra 3
print(list_1[-1]) #muesta el ultimo numero de la lista 25
print(list_1[-3]) #muesta el numero 9 ya que ese numero es el que esta en la posicion del 3 contando desde atras



# SLICING:¿Por qué funciona [::-1]?
# El slicing [::-1] es una forma de obtener una secuencia (en este caso, una cadena) en orden inverso:

# El primer : indica que se toma toda la cadena.

# El segundo : indica que no se salta ningún carácter.

# El -1 indica que se recorre la cadena en orden inverso.

print(list_1[-3:]) #muestra los tres primeros numeros contando desde atras [9,16,25


suma_lista = list_1 + [25,34,63,63]
print(suma_lista)      # nos devuelve la suma de las dos listas


# a diferencia de las cadenas las listas son mutables es decir se pueden modificar en este caso modificaremso el 65 
# raiz cubica de 4 es 64 
cubes = [1,8,27,65,125]
t = 4**3
cubes[3] = t # cambiamos 65 qye estara en la poscicion 3 

print(cubes) # se cambio el 65 por 64


letras = ["a","b","C","d","e","f","g"]
print(letras)
#ramplasamos valores 
letras[2:5] = ["C","D","E"]
print(letras) 

#removemos letras de la lista
letras[2:5] = [] 
print(letras)

#limpiamos toda la lista 

letras[:]=[]
print(letras)#la lista esta vacia 



#listas anidadas 

a = ["a","b","c"]
n = [1,2,3]
x = [a,n]
print(x) #muestra [['a', 'b', 'c'], [1, 2, 3]]

print (x[0]) #muestra la primera lista ['a', 'b', 'c']
print(x[0][1])#muestra 'b'
print(x[1][1])#muestra '2'


a,b=0,1 




while a  < 10:
    print(a, end= " ")
    a,b = b, a+b
   


#unpacking List Items
lst = ['item1','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']


# First Example
fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
first_fruit, second_fruit, third_fruit, *rest = fruits 
print(first_fruit)     # banana
print(second_fruit)    # orange
print(third_fruit)     # mango
print(rest)           # ['lemon','lime','apple']
# Second Example about unpacking list
first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)          # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4,5,6,7,8,9]
print(tenth)          # 10
# Third Example about unpacking list
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)


#Slicing Items from a List

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] # it returns all the fruits
# this will also give the same result as the one above
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3] # it does not include the first index
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2] # here we used a 3rd argument, step. It will take every 2cnd item - ['banana', 'mango']


fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:] # it returns all the fruits
orange_and_mango = fruits[-3:-1] # it does not include the last index,['orange', 'mango']
orange_mango_lemon = fruits[-3:] # this will give starting from -3 to the end,['orange', 'mango', 'lemon']
reverse_fruits = fruits[::-1] # a negative step will take the list in reverse order,['lemon', 'mango', 'orange', 'banana']



#Checking Items in a List

fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False



#Inserting Items into a List

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # insert apple between orange and mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']
print(fruits)


#Removing Items from a List

fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon', 'banana'] - this method removes the first occurrence of the item in the list
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango', 'banana']



#Removing Items Using Pop
# syntax
# lst = ['item1', 'item2']
# lst.pop()       # last item
# lst.pop(index)


fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)       # ['banana', 'orange', 'mango']

fruits.pop(0)
print(fruits)       # ['orange', 'mango']



# Removing Items Using Del

# syntax
# lst = ['item1', 'item2']
# del lst[index] # only a single item
# del lst        # to delete the list completely



fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)       # ['orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[1]
print(fruits)       # ['orange', 'lemon', 'kiwi', 'lime']
del fruits[1:3]     # this deletes items between given indexes, so it does not delete the item with index 3!
print(fruits)       # ['orange', 'lime']
del fruits
print(fruits)       # This should give: NameError: name 'fruits' is not defined


# Counting Items in a List


fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3