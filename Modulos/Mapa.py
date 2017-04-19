# Clase Mapa
class Mapa:
    # Constructor. Recibe como parámetro una lista de lista que
    # representa las casillas que tendrá y el tipo de casilla.
    def __init__(self, celdas):
        self.celdas = celdas

    # Método que devuelve cuántas columnas hay
    def tamaño_hor(self):
        return len(self.celdas[0])

    # Método que devuelve cuántas filas hay
    def tamaño_ver(self):
        return len(self.celdas)

    # Método que devuelve el tipo de celda
    def tipo_celda(self, fila, columna):
        return self.celdas[fila][columna]
