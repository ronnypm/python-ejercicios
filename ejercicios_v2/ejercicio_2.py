# Ejercicio 2

# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.


class Cursos:
    def __init__(self, *cursos: str) -> None:
        self.cursos = list(cursos)

    def mostrar_cursos(self) -> None:
        for i, curso in enumerate(self.cursos, 1):
            print(f"{i}. yo estudio {curso}")

cursos = Cursos("Matemáticas", "Física", "Química", "Historia", "Lengua")
cursos.mostrar_cursos()