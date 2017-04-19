# Librerías
import Modulos.Mapa as map

# ------------------------ FUNCION PRINCIPAL ------------------------

# Atributos
filas = None
columnas = None
mapa_prueba = None

while not filas:
    try:
        filas = int(input("Elija el nº de filas: "))
    except ValueError:
        print("Los datos introducidos no son correctos")

while not columnas:
    try:
        columnas = int(input("Elija el nº de columnas: "))
    except ValueError:
        print("Los datos introducidos no son correctos")

mapa_prueba = map.Mapa(filas, columnas)
mapa_prueba.mostrarMapa()