# Librerías
import Modulos.Mapa as map

filas = None
while not filas:
    try:
        filas = int(input("Elija la coordenada x: "))
    except ValueError:
        print("Los datos introducidos no son correctos")

columnas = None
while not columnas:
    try:
        columnas = int(input("Elija la coordenada y: "))
    except ValueError:
        print("Los datos introducidos no son correctos")

mapa_prueba = map.Mapa(filas, columnas)
print(mapa_prueba.celdas)