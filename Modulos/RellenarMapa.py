import Modulos.problema_espacio_estados as probee
import copy

class RellenarMapa(probee.Acción):
    # Constructor
    def __init__(self, x, y, ficha):
        nombre = 'Ficha {} en pos.({},{})'.format(ficha, x, y)
        super().__init__(nombre)
        self.x = x
        self.y = y
        self.ficha = ficha

    def es_aplicable(self, estado):
        # El mapa tiene los huevos vacíos de una ficha a partir de las coordenadas x, y
        return estado.verificarFichaEnMapa(self.x, self.y, self.ficha)

    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)  # Paso 1: realizamos una copia del estado actual

        # Paso 2: definimos el nuevo estado sobre esa copia
        nuevo_estado.anadirFicha(self.x, self.y, self.ficha)  # Añadimos la ficha correspondiente

        # El nuevo estado será el mapa actualizado
        return nuevo_estado

    def coste_de_aplicar(self, estado):
        if self.ficha.letraFicha == 'F' or self.ficha.letraFicha=="P":
            return 30
        else:
            return 1

