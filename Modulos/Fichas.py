# Clase Fichas
#
import Modulos.Ficha as fic

class Fichas:
    # Constructor. Crea todas las fichas posibles del juego.
    # Nota: todas las fichas se han comprobado y están definidas correcta-
    #       mente
    def __init__(self):
        self.dicFichas = { 'F0': fic.Ficha('F', 0, [(0, 1), (0, 2), (1, 0), (1, 1), (2, 1)]),
                           'F1': fic.Ficha('F', 1, [(0, 1), (1, 0), (1, 1), (1, 2), (2, 2)]),
                           'F2': fic.Ficha('F', 2, [(0, 1), (1, 1), (1, 2), (2, 0), (2, 1)]),
                           'F3': fic.Ficha('F', 3, [(0, 0), (1, 0), (1, 1), (1, 2), (2, 1)]),
                           'F4': fic.Ficha('F', 4, [(0, 1), (1, 0), (1, 1), (2, 1), (2, 2)]),
                           'F5': fic.Ficha('F', 5, [(0, 2), (1, 0), (1, 1), (1, 2), (2, 1)]),
                           'F6': fic.Ficha('F', 6, [(0, 0), (0, 1), (1, 1), (1, 2), (2, 1)]),
                           'F7': fic.Ficha('F', 7, [(0, 1), (1, 0), (1, 1), (1, 2), (2, 0)]),

                           'I0': fic.Ficha('I', 0, [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]),
                           'I1': fic.Ficha('I', 1, [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]),

                           'L0': fic.Ficha('L', 0, [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1)]),
                           'L1': fic.Ficha('L', 1, [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0)]),
                           'L2': fic.Ficha('L', 2, [(0, 0), (0, 1), (1, 1), (2, 1), (3, 1)]),
                           'L3': fic.Ficha('L', 3, [(0, 3), (1, 0), (1, 1), (1, 2), (1, 3)]),
                           'L4': fic.Ficha('L', 4, [(0, 0), (0, 1), (1, 0), (2, 0), (3, 0)]),
                           'L5': fic.Ficha('L', 5, [(0, 0), (1, 0), (1, 1), (1, 2), (1, 3)]),
                           'L6': fic.Ficha('L', 6, [(0, 1), (1, 1), (2, 1), (3, 0), (3, 1)]),
                           'L7': fic.Ficha('L', 7, [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3)]),

                           'N0': fic.Ficha('N', 0, [(0, 1), (1, 0), (1, 1), (2, 0), (3, 0)]),
                           'N1': fic.Ficha('N', 1, [(0, 0), (0, 1), (0, 2), (1, 2), (1, 3)]),
                           'N2': fic.Ficha('N', 2, [(0, 1), (1, 1), (2, 0), (2, 1), (3, 0)]),
                           'N3': fic.Ficha('N', 3, [(0, 0), (0, 1), (1, 1), (1, 2), (1, 3)]),
                           'N4': fic.Ficha('N', 4, [(0, 0), (1, 0), (2, 0), (2, 1), (3, 1)]),
                           'N5': fic.Ficha('N', 5, [(0, 2), (0, 3), (1, 0), (1, 1), (1, 2)]),
                           'N6': fic.Ficha('N', 6, [(0, 0), (1, 0), (1, 1), (2, 1), (3, 1)]),
                           'N7': fic.Ficha('N', 7, [(0, 1), (0, 2), (0, 3), (1, 0), (1, 1)]),

                           'P0': fic.Ficha('P', 0, [(0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]),
                           'P1': fic.Ficha('P', 1, [(0, 0), (0, 1), (1, 0), (1, 1), (1, 2)]),
                           'P2': fic.Ficha('P', 2, [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0)]),
                           'P3': fic.Ficha('P', 3, [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2)]),
                           'P4': fic.Ficha('P', 4, [(0, 0), (0, 1), (1, 0), (1, 1), (2, 1)]),
                           'P5': fic.Ficha('P', 5, [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1)]),
                           'P6': fic.Ficha('P', 6, [(0, 0), (1, 0), (1, 1), (2, 0), (2, 1)]),
                           'P7': fic.Ficha('P', 7, [(0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]),

                           'T0': fic.Ficha('T', 0, [(0, 0), (0, 1), (0, 2), (1, 1), (2, 1)]),
                           'T1': fic.Ficha('T', 1, [(0, 2), (1, 0), (1, 1), (1, 2), (2, 2)]),
                           'T2': fic.Ficha('T', 2, [(0, 1), (1, 1), (2, 0), (2, 1), (2, 2)]),
                           'T3': fic.Ficha('T', 3, [(0, 0), (1, 0), (1, 1), (1, 2), (2, 0)]),

                           'U0': fic.Ficha('U', 0, [(0, 0), (0, 2), (1, 0), (1, 1), (1, 2)]),
                           'U1': fic.Ficha('U', 1, [(0, 0), (0, 1), (1, 0), (2, 0), (2, 1)]),
                           'U2': fic.Ficha('U', 2, [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2)]),
                           'U3': fic.Ficha('U', 3, [(0, 0), (0, 1), (1, 1), (2, 0), (2, 1)]),

                           'V0': fic.Ficha('V', 0, [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]),
                           'V1': fic.Ficha('V', 1, [(0, 0), (0, 1), (0, 2), (1, 0), (2, 0)]),
                           'V2': fic.Ficha('V', 2, [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]),
                           'V3': fic.Ficha('V', 3, [(0, 2), (1, 2), (2, 0), (2, 1), (2, 2)]),

                           'W0': fic.Ficha('W', 0, [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2)]),
                           'W1': fic.Ficha('W', 1, [(0, 1), (0, 2), (1, 0), (1, 1), (2, 0)]),
                           'W2': fic.Ficha('W', 2, [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2)]),
                           'W3': fic.Ficha('W', 3, [(0, 2), (1, 1), (1, 2), (2, 0), (2, 1)]),

                           'X0': fic.Ficha('X', 0, [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)]),

                           'Y0': fic.Ficha('Y', 0, [(0, 1), (1, 0), (1, 1), (2, 1), (3, 1)]),
                           'Y1': fic.Ficha('Y', 1, [(0, 2), (1, 0), (1, 1), (1, 2), (1, 3)]),
                           'Y2': fic.Ficha('Y', 2, [(0, 0), (1, 0), (2, 0), (2, 1), (3, 0)]),
                           'Y3': fic.Ficha('Y', 3, [(0, 0), (0, 1), (0, 2), (0, 3), (1, 1)]),
                           'Y4': fic.Ficha('Y', 4, [(0, 1), (1, 1), (2, 0), (2, 1), (3, 1)]),
                           'Y5': fic.Ficha('Y', 5, [(0, 0), (0, 1), (0, 2), (0, 3), (1, 2)]),
                           'Y6': fic.Ficha('Y', 6, [(0, 0), (1, 0), (1, 1), (2, 0), (3, 0)]),
                           'Y7': fic.Ficha('Y', 7, [(0, 1), (1, 0), (1, 1), (1, 2), (1, 3)]),

                           'Z0': fic.Ficha('Z', 0, [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)]),
                           'Z1': fic.Ficha('Z', 1, [(0, 2), (1, 0), (1, 1), (1, 2), (2, 0)]),
                           'Z2': fic.Ficha('Z', 2, [(0, 1), (0, 2), (1, 1), (2, 0), (2, 1)]),
                           'Z3': fic.Ficha('Z', 3, [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)])
                           }

    # Método que dibuja las fichas en pantalla de un tipo concreto
    def dibujarFichas(self, tipoFicha):
        # Por cada una de las fichas del tipo indicado...
        for ficha in self.dicFichas[tipoFicha]:
            # ...iremos dibujandolo casilla a casilla si corresponde
            for i in range(0, 5, 1):
                for j in range(0, 5, 1):
                    if (i,j) in ficha:
                        print(" x ", end="")
                    else:
                        print("   ", end="")

                print("")

    # Método que lista por pantalla todas las fichas disponibles
    def listadoFichas(self):
        for keys, values in self.dicFichas.items():
            print(keys)
            print(values)

    # Método que se utiliza para coger una ficha de todas las disponibles
    def cogerFicha(self, ficha):
        return self.dicFichas[ficha]

    # Método que se utiliza para coger una ficha de todas las disponibles
    def cogerFicha(self, ficha, numero):
        return self.dicFichas[str(ficha)+str(numero)]