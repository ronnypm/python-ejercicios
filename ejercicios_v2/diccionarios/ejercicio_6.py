# Imagina que estás desarrollando un pequeño sistema de gestión de tareas.
# Las tareas se almacenan en una lista de diccionarios, donde cada tarea tiene:

#     id → un número entero único

#     descripcion → texto ingresado por el usuario

#     urgencia → número entero entre 1 y 5

#     estado → booleano (False por defecto, significa “pendiente”)

# El usuario no puede elegir el ID.
# El ID debe generarse automáticamente simulando el comportamiento de una base de datos, es decir, debe ser autoincremental: si la última tarea tiene id 5, la siguiente debe tener id 6.
# Tu tarea

# Crear un programa en Python que:

#     Tenga una lista inicial de tareas (puede estar vacía o con algunas tareas cargadas).

#     Permita al usuario agregar una nueva tarea pidiendo:

#         la descripción

#         el nivel de urgencia (1 a 5)

#     Genere automáticamente un id autoincremental.

#     Establezca por defecto el campo estado como False.

#     Agregue la nueva tarea a la lista.

#     Finalmente, muestre la lista actualizada de todas las tareas.


tareas = [
    {
        "id": 1,
        "descripcion": "Revisar correos pendientes",
        "urgencia": 2,
        "estado": False
    },
    {
        "id": 2,
        "descripcion": "Llamar al proveedor de internet",
        "urgencia": 4,
        "estado": False
    },
    {
        "id": 3,
        "descripcion": "Actualizar inventario del almacén",
        "urgencia": 3,
        "estado": False
    },
    {
        "id": 4,
        "descripcion": "Preparar informe semanal",
        "urgencia": 5,
        "estado": False
    },
    {
        "id": 5,
        "descripcion": "Hacer copia de seguridad del sistema",
        "urgencia": 1,
        "estado": False
    },
    {
        "id": 6,
        "descripcion": "Hacer copia de seguridad del sistema",
        "urgencia": 1,
        "estado": False
    }
]


def obtener_ultimo_id():
    # if not tareas:
    #     return 0
    # id = tareas[-1]
    # ultimo_id = id.get("id")
    # return ultimo_id
    return tareas[-1]["id"] if tareas else 0


def creando_nueva_tarea(descripcion: str, urgencia: int, estado: bool = False) -> dict:
    mi_id = obtener_ultimo_id() + 1
    nuevo_id = mi_id
    return {
        "id": nuevo_id,
        "descripcion": descripcion,
        "urgencia": urgencia,
        "estado": estado
    }


def agregar_nueva_tarea(nueva_tarea):
    tareas.append(nueva_tarea)


tarea = creando_nueva_tarea(descripcion="Formatera PC", urgencia=1)
agregar_nueva_tarea(tarea)
print(tareas)
