# Clase Ficha

class Ficha:
    # Constructor. Crea una ficha del juego
    def __init__(self, letraFicha, numero, listaPosiciones):
        self.letraFicha = letraFicha
        self.numero = numero
        self.listaPosiciones = listaPosiciones

    # Método que dibuja las ficha en pantalla
    def mostrarFicha(self):
        for i in range(0, 5, 1):
            for j in range(0, 5, 1):
                if (i, j) in self.listaPosiciones:
                    print(" x ", end="")
                else:
                    print("   ", end="")

            print("")

    # Representación como cadena
    def __str__(self):
        return str(self.letraFicha) + str(self.numero) + ": "+ str(self.listaPosiciones)