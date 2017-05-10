# Librerías
import Modulos.Mapa as map
import Modulos.Fichas as fic

# ------------------------ FUNCION PRINCIPAL ------------------------

# Atributos
filas = None
columnas = None
mapa_prueba = None

# Mientras filas no tenga un valor asignado...
while not filas:
    try:
        filas = int(input("Elija el nº de filas: "))
    except ValueError:
        print("Los datos introducidos no son correctos")

# Mientras columnas no tenga un valor asignado...
while not columnas:
    try:
        columnas = int(input("Elija el nº de columnas: "))
    except ValueError:
        print("Los datos introducidos no son correctos")

# Líneas de prueba
mapa_prueba = map.Mapa(filas, columnas)
mapa_prueba.marcarCasilla(1, 2)
# mapa_prueba.marcarCasilla(1, 1)
mapa_prueba.mostrarMapa()

# Probando la clase fichas
ficha = fic.Fichas()
# ficha.listadoFichas()
ficha.dibujarFichas('Z')
