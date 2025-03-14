#TUPLES: ES UN CONJUSTO DE VALORES no pueden ser modificables es decir que no son mutables 
my_tuple = tuple()
my_other_tuple = ()

my_tuple = (12,1.70,"ronny","pisfil","ronny")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[3])
print(my_tuple[-1])



print(my_tuple.count("ronny"))
print(my_tuple.index("pisfil"))
