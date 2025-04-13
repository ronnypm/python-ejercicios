# Hay 4 clases principales:

# datetime.date: solo fecha (año, mes, día).
# datetime.time: solo hora (hora, minuto, segundo).
# datetime.datetime: fecha y hora.
# datetime.timedelta: diferencia entre dos fechas/horas.

from datetime import datetime,date,time, timedelta
# import pytz
print('import now')
ahora = datetime.now() #nos da el momento actual del sistema.
print(ahora)


print('-' * 30)
print('import date')
mi_cumple = date(1996, 8, 9)#date(año, mes, día) permite crear fechas manualmente.
print(f'Mi cumpleanos es {mi_cumple}')

print('-' * 30)
print('import time')
hora_almuerzo = time(13,30)
print(f'Hora del almuerzo es {hora_almuerzo}')


print('-' * 30)
# ¿Quieres saber cuántos días faltan para un evento? Aquí va:
print('Import timedelta')
hoy = date.today()
navidad = date(2025,12,25)
falta = navidad - hoy
print(f'Falta {falta.days} dias para navidad')


print('-' * 30)

manana = hoy + timedelta(days=3) #También puedes sumar o
ayer = hoy - timedelta(days=1) # restar días

print(manana)
print(ayer)

print('-' * 30)

print('import datatime')
print('strftime')
ahora = datetime.now()
print(ahora.strftime('%d/%m/%y %H:%M'))#%d: día, %m: mes, %Y: año completo, %H:%M: hora y minuto.


print('-' * 30)

fecha_str = "11/04/2025"
fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
print("Fecha convertida:", fecha)

print('-' * 30)

# zonas horarias y precisión
#Necesitas instalar pytz con pip install pytz.

# print('from datetime import datetime')
# print('import pytz')


# zona_lima = pytz.timezone('America/Lima')
# ahora_lima = datetime.now(zona_lima)
# print(f'Hora en lima {ahora_lima}')

ahora = datetime.now()
print("Microsegundos:", ahora.microsecond)


print('''🧠 Casos reales y buenas prácticas
En aplicaciones web, siempre convierte todo a UTC para guardar en base de datos y luego muestra en zona local.
Evita manejar fechas como strings para cálculos.
Usa timedelta para agendar tareas automáticas (ej: notificaciones, vencimientos).''')
