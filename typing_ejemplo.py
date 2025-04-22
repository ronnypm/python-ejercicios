edad: int = 30

from typing import List, Dict

nombres: List[str] = ["Ana", "Luis"]
edades: Dict[str, int] = {"Ana": 30, "Luis": 25}



from typing import Tuple

persona: Tuple[str, int] = ("Carlos", 40)


from typing import Union

def procesar(valor: Union[int, str]):
    print(valor)



from typing import TypedDict

# 📘 Útil para validar estructuras tipo JSON.

class Usuario(TypedDict):
    nombre: str
    edad: int

usuario: Usuario = {"nombre": "Ana", "edad": 30}



from typing import Callable

def ejecutar(f: Callable[[int, int], int]) -> int:
    return f(2, 3)

def sumar(a: int, b: int) -> int:
    return a + b

print(ejecutar(sumar))  # 5



from typing import Literal

#  Literal: restringir valores permitidos

def obtener_estado(estado: Literal['activo', 'inactivo']) -> str:
    return f"El usuario está {estado}"


from typing import Any

def debug(valor: Any) -> None:
    print("Valor:", valor)