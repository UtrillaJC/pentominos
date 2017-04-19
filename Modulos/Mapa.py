# Clase Mapa
class Mapa:
    # Constructor. Recibe como parámetro una lista de listas que
    # representa las casillas que tendrá y el tipo de casilla.
    def __init__(self, filas, columnas):
        self.celdas = [([0] * columnas) for i in range(filas)]

    # Método que devuelve cuántas columnas hay
    def tamaño_hor(self):
        return len(self.celdas[0])

    # Método que devuelve cuántas filas hay
    def tamaño_ver(self):
        return len(self.celdas)

    # Método que devuelve el tipo de celda
    def tipo_celda(self, fila, columna):
        return self.celdas[fila][columna]
