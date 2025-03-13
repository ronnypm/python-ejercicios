
# class MyEmptyPerson:
#     pass

# print(MyEmptyPerson())



# class Person:
#     def __init__(self,name,surname):
#         self.name = name
#         self.surname = surname


# my_person = Person('ronny','pisfil')
# print(my_person.name)
# print(f'El nombre es: {my_person.name} El apellido es:{my_person.surname}')

# #######################################################################################

# class Person2:
#     def __init__(self,name,surname,alias = 'Sin alias'):
#         self.full_name = f'{name} {surname} ({alias})'


#     def walk(self):
#         print(f'{self.full_name} esta caminando')

# my_person = Person2('ronny','pisfil')
# print(my_person.full_name)
# my_person.walk()

# my_other_person = Person2('ronny','pisfil','fito')
# print(my_other_person.full_name)
# my_other_person.walk()
# my_other_person.full_name = 'itham david (el karateca)'
# print(my_other_person.full_name)


class Perro:
    def __init__(self,nombre,raza):
        self.nombre = nombre
        self.raza = raza

    def Ladrad(self):
        print(f'{self.nombre} esta ladrando.')

mi_perro = Perro('tony','doberman')
mi_perro.Ladrad()