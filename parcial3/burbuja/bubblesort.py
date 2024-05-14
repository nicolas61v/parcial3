#usamos las librerias necesarias
import csv
import time

# creamos una función para cargar los datos desde un archivo CSV
def cargar_datos(archivo):
    with open(archivo, 'r', newline='') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

# creamos una función para escribir los datos ordenados en un archivo CSV
def escribir_datos_ordenados(archivo, datos):
    with open(archivo, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=datos[0].keys())
        writer.writeheader()
        writer.writerows(datos)

# creamos una función para ordenar los datos usando el algoritmo bubble sort
def bubble_sort(datos):
    n = len(datos)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            # Comparar los valores de tiempo y satisfaction
            if (int(datos[j]['time_spend_company']), float(datos[j]['satisfaction_level'])) < (int(datos[j + 1]['time_spend_company']), float(datos[j + 1]['satisfaction_level'])):
                datos[j], datos[j + 1] = datos[j + 1], datos[j]

# cargamos los datos desde el archivo 
archivo_csv = "HR_capstone_dataset.csv"
print("Abriendo archivo:", archivo_csv)
datos = cargar_datos(archivo_csv)

# inicializamos el medida del tiempo
inicio = time.time()

# llamamos la función bubble_sort para ordenar los datos
bubble_sort(datos)

# medimos el tiempo que tarda en ejecutarse el algoritmo
fin = time.time()
tiempo_total = fin - inicio

# Escribimos los datos ordenados en un nuevo archivo CSV
archivo_csv_ordenado = "HR_capstone_dataset_ordenado_bubble.csv"
print("Creando CSV: 0 completado")
escribir_datos_ordenados(archivo_csv_ordenado, datos)

print("Datos ordenados y guardados en", archivo_csv_ordenado)
print("Tiempo de ejecución:", tiempo_total, "segundos")
