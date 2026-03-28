from functools import lru_cache
import random


@lru_cache
def generar_token(username: str):
    token = random.randint(1000, 9999)
    print(f"Generando token para {username}: {token}")
    return token


token_1 = generar_token("ronny")
token_2 = generar_token("ronny")
token_3 = generar_token("nico")
token_4 = generar_token("ronny")


print(f"Token1: {token_1}")
# print(f"Token2: {token_2}")
# print(f"Token3: {token_3}")
# print(f"Token4: {token_4}")
