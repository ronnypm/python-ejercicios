import csv

#escritura 

with open('datos.csv', 'w', newline='') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(['nombre', 'edad'])
    escritor.writerow(['Ana', 30])
    escritor.writerow(['Luis', 25])


#lectura

with open('datos.csv', 'r') as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)