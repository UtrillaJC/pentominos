# Clase Mapa
#
import Modulos.Fichas
import Modulos.Ficha as fic
import copy

class Mapa:
    # Constructor. Recibe como parámetro las coordenadas x, y
    # y crea un mapa.
    # Nota: cada elemento de fichasColocadas debe contener:
    #       Posición + Ficha
    def __init__(self, filas, columnas):
        self.map = [([0] * columnas) for i in range(filas)]
        self.filas = filas
        self.columnas = columnas
        self.fichasColocadas = []

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
        # Comprobamos que las variables de entrada son del tipo que se espera y si podemos añadir la ficha...
        if isinstance(ficha, fic.Ficha) and isinstance(x, int) and isinstance(y, int) and self.verificarFichaEnMapa(x, y, ficha):
            # ...añado la ficha y su posición en la lista fichasColocadas
            self.fichasColocadas.append(((x,y),ficha))
            #print("Entraaa")

            # Por cada una de las posiciones de la ficha seleccionada...
            for tupla in ficha.listaPosiciones:
                # ...marco la casilla correspondiente
                self.marcarCasilla(x + tupla[0], y + tupla[1])
        else:
            print("No puedo añadir la ficha")

    # Método que verifica si podemos añadir una ficha en nuestro mapa
    def verificarFichaEnMapa(self, x, y, ficha):

        # Si no corresponden con las instancias...
        if isinstance(ficha, fic.Ficha) and isinstance(x, int) and isinstance(y, int):

            # Recorre cada una de las casillas de la ficha...
            for tupla in ficha.listaPosiciones:

                # ...comprobamos que no nos salimos del mapa ...

                try:
                    if x + tupla[0] > self.columnas - 1 or y + tupla[1] > self.filas - 1:
                        return False                     # ...no puedo incluir la ficha
                    # ...y si la casilla ya se encuentra marcada...
                    elif self.map[x + tupla[0]][y + tupla[1]] == 1:
                        return False                     # ...no puedo incluir la ficha
                # Si al intentar acceder a las posiciones salta la excepción...
                except IndexError:
                    # ... es que nos hemos salido del mapa
                    return False

        else:
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
        return (self.filas * self.columnas) - self.numCasillasMarcadas(

    def numFilasPorRellenar(self):
        contador = 0

        for

    def numColumnasPorRellenar(self):
        contador = 0

    def __str__(self):
        self.mostrarMapa()
        return "Datos del Mapa:" \
               "\n\tCasillas marcadas: " + str(self.numCasillasMarcadas()) + \
               "\n\tCasillas restantes: " + str(self.numCasillasDesmarcadas())

