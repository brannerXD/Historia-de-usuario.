import csv

def guardar_csv(inventario, ruta, incluir_header=True):

    if len(inventario) == 0:
        print("El inventario está vacío. No se puede guardar un archivo CSV.")
        return
    with open(ruta, mode='w', newline='', encoding='utf-8') as archivo:
        campos = ['nombre', 'cantidad', 'precio']
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        if incluir_header:
            escritor.writeheader()
        for producto in inventario:
            escritor.writerow(producto)
    return "Guardado"

def cargar_csv(inventario, ruta):

    try:
        with open(ruta, mode='r', newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                producto = {
                    'nombre': fila['nombre'],
                    'cantidad': int(fila['cantidad']),
                    'precio': float(fila['precio'])
                }
                inventario.append(producto)
    except FileNotFoundError:
        print(f"El archivo {ruta} no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al cargar el archivo CSV: {e}")
    return "Cargado"