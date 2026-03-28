from functools import lru_cache


def get_config():
    print("Leyendo configuracion...")
    return {"app": "MiApp", "Version": "1.0.0"}


config_1 = get_config()
config_2 = get_config()
config_3 = get_config()


print("\n------------------con Lru_Cache-------------------\n")


@lru_cache
def get_config():
    print("Leyendo configuracion con lru_cache...")
    return {"app": "MiApp", "Version": "1.0.0"}


config_1 = get_config()
config_2 = get_config()
config_3 = get_config()
