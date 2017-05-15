# Clase Mapa
import Modulos.Fichas

class Mapa:
    # Constructor. Recibe como parámetro las coordenadas x, y
    # y crea un mapa.
    def __init__(self, filas, columnas):
        self.map = [([0] * columnas) for i in range(filas)]
        self.filas = filas
        self.columnas = columnas

    # Método que devuelve cuántas columnas hay
    def tamaño_filas(self):
        return len(self.map[0])

    # Método que devuelve cuántas filas hay
    def tamaño_columnas(self):
        return len(self.map)

    # Método que devuelve si una celda está ocupada o no
    def valor_casilla(self, fila, columna):
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

    # Método que añade una ficha en el mapa
    def anadirFicha(self, x,y, ficha):
        # Comprobamos que las variables de entrada son del tipo que se espera y si podemos añadir la ficha
        if isinstance(ficha, list) and isinstance(x, int) and isinstance(y, int) and self.verificarFichaEnMapa(x, y, ficha):

            # Por cada una de las posiciones de la ficha seleccionada...
            for tupla in ficha:

                # ...marco la casilla correspondiente
                self.marcarCasilla(x + tupla[0], y + tupla[1])
        else:
            print("No puedo añadir la ficha")

    # Método que quita una ficha en el mapa
    def quitarFicha(self, x, y, ficha):
        # Comprobamos que las variables de entrada son del tipo que se espera
        if isinstance(ficha, list) and isinstance(x, int) and isinstance(y, int):
            # [FALTA] Verificar si se puede añadir la ficha

            # Añadimos la ficha en el mapa

            # Por cada una de las posiciones de la ficha seleccionada...
            for tupla in ficha:
                # ...marco la casilla correspondiente
                self.desmarcarCasilla(x + tupla[0], y + tupla[1])

    # Método que verifica si podemos añadir una ficha en nuestro mapa
    def verificarFichaEnMapa(self, x, y, ficha):

        # Por cada una de las posiciones de la ficha...
        for tupla in ficha:

            # ...si la casilla ya se encuentra marcada...
            if self.map[x + tupla[0]][y + tupla[1]] == 1:

                # ...no puedo incluir la ficha
                return False

        # En caso de que todas las posiciones esten desmarcadas, entonces
        # puedo añadir la ficha.
        return True

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

    # Método que calcula las casillas que están marcadas en el mapa
    def numCasillasMarcadas(self):
        contador = 0            # Cuenta el nº casillas marcadas

        for i in self.map:
            for j in i:
                if j == 1:
                    contador += 1

        return contador

    # Método que calcula las casillas que están desmarcadas en el mapa
    def numCasillasDesmarcadas (self):
        return (self.filas * self.columnas) - self.numCasillasMarcadas()