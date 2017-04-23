# Clase Mapa
import Modulos.Fichas

class Mapa:
    # Constructor. Recibe como parámetro las coordenadas x, y
    # y crea un mapa.
    def __init__(self, filas, columnas):
        self.map = [([0] * columnas) for i in range(filas)]

    # Método que devuelve cuántas columnas hay
    def tamaño_filas(self):
        return len(self.map[0])

    # Método que devuelve cuántas filas hay
    def tamaño_columnas(self):
        return len(self.map)

    # Método que devuelve si una celda está ocupada o no
    def valor_celda(self, fila, columna):
        return self.map[fila][columna]

    # Método que marca una casilla del mapa
    def marcarCasilla(self, fila, columna):

        if self.map[fila][columna] == 1:
            raise ValueError("---> ERROR, la casilla ya está marcada <---")

        self.map[fila][columna] = 1

    # Método que desmarca una casilla del mapa
    def desmarcarCasilla(self, fila, columna):
        if self.map[fila][columna] == 0:
            raise ValueError("---> ERROR, la casilla ya está desmarcada <---")

        self.map[fila][columna] = 0

    """
    def anadirFicha(self, ficha):
        if isinstance(ficha, Modulos.Fichas):
            for tupla in ficha:
                print()
    """

    # Muestra en pantalla el mapa
    def mostrarMapa(self):
        for i in self.map:
            print("+-----" * self.tamaño_filas() + "+")

            for j in i:
                valorCasilla = " "

                if j == 1:
                    valorCasilla = "*"

                print("|  " + valorCasilla + "  ", end="")

            print("|")

        print("+-----" * self.tamaño_filas() + "+")



