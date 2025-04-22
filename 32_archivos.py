# Abrir y leer un archivo

# 📌 ¿Qué hace este código?
# 'r' significa "modo lectura".
# with se usa para abrir el archivo y cerrarlo automáticamente al terminar.
# ------------------------------------------------------------------

# with open('mi_archivo.txt', 'r') as archivo:
#     contenido = archivo.read()
#     print(contenido)

# ------------------------------------------------------------------

# Leer línea por línea

# with open('mi_archivo.txt','r') as archivo:
#     for linea in archivo:
#         print(linea.strip())


# ------------------------------------------------------------------
# Escribir en un archivo (¡cuidado, sobrescribe!)

# with open('mi_archivo.txt', 'w') as archivo:  # w sobre escribe
#     archivo.write('Hola .\n')
#     archivo.write('esto es otra linea.\n')
#     archivo.write('ronny.\n')

# Agregar contenido (modo append)


# with open ('mi_archivo.txt', 'a') as archivo: # a agrega
#     archivo.write('Agregamos mas texto sin borrar lo anterior.\n')


# ------------------------------------------------------------------

# 1. Leer archivos grandes con eficiencia

# def leer_grande(ruta):
#     with open(ruta, 'r') as archivo:
#         for linea in archivo:
#             yield linea.strip()  # Generador

# 👉 Ideal para archivos de muchos GB sin quedarte sin RAM.

# ------------------------------------------------------------------

# 2. Escritura condicional o segura

# import os

# if not os.path.exists('reporte.txt'):
#     with open('reporte.txt', 'w') as archivo:
#         archivo.write('Reporte inicial\n')



# ------------------------------------------------------------------

# 3. Codificación

# with open('archivo_utf8.txt', 'r', encoding='utf-8') as archivo:
#     print(archivo.read())


# 📌 Útil para leer archivos con tildes, eñes, caracteres especiales o emojis.
# Usa encoding='utf-8' siempre que trabajes con idiomas distintos al inglés.

# ------------------------------------------------------------------

# 🔐 Seguridad y errores
# Siempre es buena práctica capturar errores al trabajar con archivos:


# try:
#     with open('no_existe.txt', 'r') as archivo:
#         contenido = archivo.read()
# except FileNotFoundError:
#     print("¡El archivo no se encuentra!")
# except Exception as e:
#     print("Ocurrió un error:", e)