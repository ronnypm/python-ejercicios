import mysql.connector

conexion = mysql.connector.connect(
    host ="localhost",
    user = "root",
    password = "Genaro96#",
    database ="mi_base_nueva",
)

cursor = conexion.cursor()

cursor.execute("SHOW TABLES;")
tablas = cursor.fetchall()

if tablas:
    print("📌 Tablas en la base de datos:")
    for tabla in tablas:
        print("-", tabla[0])
else:
    print("❌ No hay tablas en la base de datos")