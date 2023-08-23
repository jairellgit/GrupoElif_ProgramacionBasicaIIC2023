# Archivo para tener funciones repetitivas en los
# diferentes módulos del programa, con la finalidad
# de reciclarlas.

def returnToMainMenu():
    from index import start
    start()

# Obtener el tipo de cambio del archivo Configuración Avanzada
def confAvanzada():
    fileConfiguracionAvanzada = "configuracion_avanzada.txt"

    # Abrir el archivo en modo lectura (r) y guardarlo en una variable usando 'with'
    with open(fileConfiguracionAvanzada, 'r') as archivo:
        # 3. Leer el contenido del archivo línea por línea y almacenarlo en una lista
        lineas = archivo.readlines()

    # Crear un array vacío donde almacenaremos las líneas del archivo
    listaConfAvanzada = []

    # Recorrer la lista de líneas y agregar cada línea al array
    for linea in lineas:
        # strip() elimina los caracteres de nueva línea al final de cada línea
        listaConfAvanzada.append(linea.strip())

    return listaConfAvanzada
