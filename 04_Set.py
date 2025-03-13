#SSET es como una lista pero que no es modificable
#LOS SET NO ADMITEN ELEMENTOS REPETIDOS
#los set son desordenados no podemos acceder a sus indices


my_set = set()
my_other_set = {}
print(type(my_set))
print(type(my_other_set))



my_set = {'juan','pedro',10}

my_set.add('ronny')

print(my_set)

print('ronny' in my_set)
print('ronn' in my_set)



my_set.remove(10)
print(my_set)

my_set.clear()

print(my_set)
print(len(my_set))
