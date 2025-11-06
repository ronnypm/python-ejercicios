# Ejercicio 3

# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.


lista_cursos = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
lista_notas = []
for index, curso in enumerate(lista_cursos):
    notas = input(f"{1}. Ingresa la nota de {curso}: ")
    lista_notas.append(notas)

# for nota in range(len(lista_cursos)):
#     print(lista_cursos[nota], lista_notas[nota])

lista_notas = [lista_cursos[nota], lista_notas[nota] for nota in range(len(lista_cursos)) nota]
