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

# creamos la función de ordenamiento por inserción
def insercion_sort(datos):
    for i in range(1, len(datos)):
        actual = datos[i]
        j = i - 1
        while j >= 0 and (int(datos[j]['time_spend_company']) < int(actual['time_spend_company']) or (int(datos[j]['time_spend_company']) == int(actual['time_spend_company']) and float(datos[j]['satisfaction_level']) < float(actual['satisfaction_level']))):
            datos[j + 1] = datos[j]
            j -= 1
        datos[j + 1] = actual

# Cargamos los datos desde el archivo
archivo_csv = "HR_capstone_dataset.csv"
print("Abriendo archivo:", archivo_csv)
datos = cargar_datos(archivo_csv)

# inicializamos el tiempo antes de ejecutar el algoritmo
inicio = time.time()

# llama a la función de ordenamiento
insercion_sort(datos)

# Medimos el tiempo después de ejecutar el algoritmo de ordenamiento
fin = time.time()
tiempo_total = fin - inicio

# Escribimos los datos ordenados en un nuevo archivo CSV
archivo_csv_ordenado = "HR_capstone_dataset_ordenado_insercion.csv"
print("Creando CSV: 0 completado")
escribir_datos_ordenados(archivo_csv_ordenado, datos)

print("Datos ordenados y guardados en", archivo_csv_ordenado)
print("Tiempo de ejecución:", tiempo_total, "segundos")
