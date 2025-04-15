tabla = str.maketrans("aeiou", "12345")
texto = "hola mundo"
nuevo_texto = texto.translate(tabla)

print(nuevo_texto)  # h4l1 m5nd4


# 🔁 Cambia las vocales por números. 'a'→'1', 'e'→'2', etc.


# ------------------------------------------------------------------------------

# ❌ Ejemplo: eliminar caracteres
tabla = str.maketrans("", "", "aeiou")
texto = "hola mundo"
nuevo_texto = texto.translate(tabla)

print(nuevo_texto)  # hl mnd

# Tercer argumento en maketrans() indica los caracteres que se eliminarán.



# ------------------------------------------------------------------------------

# 🧠 Traducción combinada (reemplazo y eliminación)

tabla = str.maketrans("aeiou", "12345", " ")
texto = "hola mundo"
nuevo_texto = texto.translate(tabla)

print(nuevo_texto)  # h4l1m5nd4


# Cambia vocales por números y elimina espacios.