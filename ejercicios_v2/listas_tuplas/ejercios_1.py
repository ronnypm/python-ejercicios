# Ejercicio 1

# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
class Cursos:
    def __init__(self,lista_curso:list) -> None:
        self.lista_curso = lista_curso


    def mostrar_Cursos(self):
        for i, curso, in enumerate(self.lista_curso, 1):
            print(f"{i}. {curso}")


cursos =Cursos(["Matemáticas", "Física", "Química", "Historia", "Lengua"])
cursos.mostrar_Cursos()


