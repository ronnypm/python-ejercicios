# clientes = [
#     {'nombre':'Juan','pago_total':200, 'Pago_parcial': 50},
#     {'nombre':'Ronny','pago_total':500, 'Pago_parcial': 100}
# ]

# for cliente in clientes:
#     if cliente['Pago_parcial'] < cliente['pago_total']:
#         saldo = cliente['pago_total'] - cliente['Pago_parcial']
#         print(f'Saldo pendiente de {cliente['nombre'] }: {saldo}')



# -------------------------------------------------------------------------




def mostrar_prendas():

    return  [
        {'id':1,'prenda':'Camisa de algodon','estado':False},
        {'id':2,'prenda':'Camisa de algodon','estado':False}
    ]



def enviar_notificacion(prenda):
    print(f'Notificacion: La prendad {prenda['prenda']} ya esta lista para ser entregada.')




def prendas_terminadas():
    prendas = mostrar_prendas()
    for prenda in prendas:
        if prenda['estado']:
            enviar_notificacion(prenda)
        else:
            print(f'La prenda {prenda['prenda']} aun no esta en proceso.')

prendas_terminadas()





# # Cambiar el estado cuando el pago sea completo
# def procesar_pago(prenda, pago_total):
#     if pago_total >= 100:  # Supongamos que el precio total de la prenda es 100
#         prenda["estado"] = True
#         print(f"Pago completo. La prenda {prenda['nombre']} está lista.")
#     else:
#         print(f"El pago no es suficiente para procesar la prenda {prenda['nombre']}.")

# # Proceso de pago
# procesar_pago(prendas[0], 100)  # La camisa de algodón ya está pagada y ahora estará lista
