# precios_base = [100, 250, 80, 150]

# # Aplicar IGV con una lambda
# precios_con_igv = list(map(lambda x: round(x * 1.18, 2), precios_base))

# print("Precios con IGV:")
# for precio in precios_con_igv:
#     print(precio)




# precios = [100, 200, 300]
# descuentos = [10, 20, 30]

# # Aplicar descuento a cada precio
# precios_con_descuento = list(map(lambda p, d: p - p * d / 100, precios, descuentos))

# print(precios_con_descuento)



# Ejercicio 1: Aplicar un descuento a una lista de precios
# Supón que tenemos una lista de precios y queremos aplicar un descuento de 15% a cada uno. Usaremos map() para calcular el precio con descuento.


precios = [100, 250, 80, 150, 200]


descuentos = list(map(lambda x : round(x-x * 0.15,2),precios))

for precio in descuentos:
    print(precio)


# precios = [100, 250, 80, 150, 200]

# # Aplicar un descuento del 15% usando map y lambda
# precios_con_descuento = list(map(lambda p: round(p - p * 0.15, 2), precios))

# # Mostrar resultados
# print("Precios con descuento:")
# for precio in precios_con_descuento:
#     print(precio)