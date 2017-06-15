# ----------------------------- MODULOS -----------------------------
import Modulos.Mapa as map
import Modulos.Fichas as fic
import Modulos.RellenarMapa as accion
import Modulos.problema_espacio_estados as probee
import Modulos.búsqueda_espacio_estados as busquee
import copy

#

"""
Para implementar un problema de espacio de estados se pueden hacer uso de las
clases de objetos proporcionadas por el modulo problema_espacio_estados.

Los alg. de búsqueda están implementados en el módulo busqueda_espacio_estados.

El módulo copy será de utilidad para copiar un estado en otro estado igual, pe-
ro completamente nuevo e independiente.
"""

# ------------------------ SCRIPT PRINCIPAL ------------------------
"""
 Supondremos que mapa es una constante fija que no está contenida dentro de un
 estado. Esto no quiere decir que no se pueda incluir, pero haría que el pro-
 blema fuese más complejo de resolver.

 Seguiremos los siguientes pasos que se muestran a continuación:

 - Paso 1: definir cómo va a ser la representación de los estados del problema.
           Debe contener información relevante.

 - Paso 2: definimos las funciones de aplicabilidad y aplicación para cada una
           de las acciones del problema.

 - Paso 2.1: definimos el coste de las acciones (si es necesario).

 - Paso 3: definir las acciones correspondientes del problema.

 - Paso 4: crear las instancias de la clase problema_espacio_estados.
"""
# Atributos
fichas = fic.Fichas()
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

# Paso 1: definición de los estados del problema.
mapa = map.Mapa(filas, columnas)
estadoInicial = mapa
estadoInicial.mostrarMapa()
# estadoInicial.marcarCasilla(0,0)
# print(str(estadoInicial.verificarFichaEnMapa(0,0,fichas.cogerFicha('I', 0))))

miFicha = fichas.cogerFicha('I', 0)
x = 0
y = 0

# Paso 2: definición de las funciones aplicabilidad y aplicación
#    - Método rellenarMapa:
#         · Aplicabilidad: el mapa tiene los huecos vacíos de la ficha a
#                          partir de las coordenadas x, y.

# - Paso 2.1: definimos el coste de las acciones (si es necesario).

# - Paso 3: definir las acciones correspondientes del problema.

# Mejora: eliminamos acciones que sabemos que no se van aplicar nunca
acciones = []

for keys, values in fichas.dicFichas.items():
    for x in range(0, columnas, 1):
        for y in range(0, filas, 1):
            # Borramos aquellas acciones que de antemano no sean posibles
            # porque el hecho de aplicarlo ya nos dice que no se puede a-
            # plicar.

            fueraLimites = False

            for tupla in values.listaPosiciones:
                if x + tupla[0] > columnas - 1 or y + tupla[1] > filas - 1:
                    fueraLimites = True
            # Si la acción no está fuera de los límites...
            if not fueraLimites:
                # ...creamos la acción
                acciones.append(accion.RellenarMapa(x, y, values))

# - Paso 4: crear las instancias de la clase problema_espacio_estados.

ProblemaPentominos = probee.ProblemaEspacioEstados(
    acciones, estadoInicial, []
)

# Dime el nombre de todas las acciones que sean aplicables
for accion in ProblemaPentominos.acciones_aplicables(estadoInicial):
    print(accion.nombre)



# Definiendo la heurística necesaria para el algorimo de A*
def h1(nodo):
    estado = nodo.estado

    huecosCerrados = 0

    for i in range(0, estado.tamaño_filas(), 1):
        if __name__ == '__main__':
            for j in range(0, estado.tamaño_columnas(), 1):
                # Si la casilla está desmarcada...
                if estado.valor_casilla(i, j) == 0:
                    # Calculamos los índices...
                    arriba = j - 1
                    abajo = j + 1
                    derecha = i + 1
                    izquierda = i - 1

                    # Comprobamos si nos salimos del rango...
                    if (arriba <0 ) or (izquierda<0) or (abajo > estado.tamaño_filas() - 1) or (derecha > estado.tamaño_columnas() - 1):
                        if (arriba < 0) and (izquierda < 0):
                            # Comprobamos casillas: derecha, abajo
                            if estado.valor_casilla(derecha, j) == 1 and estado.valor_casilla(i, abajo) == 1:
                                huecosCerrados += 1
                        elif izquierda < 0 and (abajo > estado.tamaño_filas() - 1):
                            # Comprobamos casillas: derecha, arriba
                            if estado.valor_casilla(derecha, j) == 1 and estado.valor_casilla(i, arriba) == 1:
                                huecosCerrados += 1

                        elif (abajo > estado.tamaño_filas() - 1) and (derecha > estado.tamaño_columnas() - 1):
                            # Comprobamos casillas: arriba, izquierda
                            if estado.valor_casilla(i, arriba) == 1 and estado.valor_casilla(izquierda, j) == 1:
                                huecosCerrados += 1

                        elif arriba < 0 and (derecha > estado.tamaño_columnas() - 1):
                            # Comprobamos casillas: abajo, izquierda
                            if estado.valor_casilla(i, abajo) == 1 and estado.valor_casilla(izquierda, j) == 1:
                                huecosCerrados += 1

                        elif arriba < 0:
                            # Comprobamos casillas: izquierda, derecha, abajo
                            if estado.valor_casilla(izquierda, j) == 1 and estado.valor_casilla(derecha, j) == 1 \
                                    and estado.valor_casilla(i, abajo) == 1:
                                huecosCerrados += 1

                        elif izquierda < 0:
                            # Comprobamos casillas: derecha, arriba, abajo
                            if estado.valor_casilla(derecha, j) == 1 and estado.valor_casilla(i, arriba) == 1 \
                                    and estado.valor_casilla(i, abajo) == 1:
                                huecosCerrados += 1

                        elif abajo > estado.tamaño_filas() - 1:
                            # Comprobamos casillas: arriba, izquierda, derecha
                            if estado.valor_casilla(i, arriba) == 1 and estado.valor_casilla(izquierda, j) == 1 \
                                    and estado.valor_casilla(derecha, j) == 1:
                                huecosCerrados += 1

                        elif derecha > estado.tamaño_columnas() - 1:
                            # Comprobamos casillas: izquierda, arriba, abajo
                            if estado.valor_casilla(izquierda, j) == 1 and estado.valor_casilla(i, arriba) == 1 \
                                    and estado.valor_casilla(i, abajo) == 1:
                                huecosCerrados += 1
                    # Si no se sale del rango, comprobamos casillas: arriba, abajo, derecha, izquierda
                    elif estado.valor_casilla(derecha, j) == 1 and estado.valor_casilla(izquierda, j) == 1 \
                            and estado.valor_casilla(i, arriba) == 1 and estado.valor_casilla(i, abajo) == 1:
                        huecosCerrados += 1

    return huecosCerrados

# BUSQUEDA A* (A ESTRELLA) (DETALLADO):
# b_a_estrella = busquee.BúsquedaAEstrella(h1)
# print(b_a_estrella.buscar(ProblemaPentominos))


# Creamos una instancia por cada búsqueda:
# BUSQUEDA EN PROFUNDIDAD (DETALLADO):
# b_profundidad = busquee.BúsquedaEnProfundidad(detallado=True)
# print(b_profundidad.buscar(ProblemaPentominos))

# BUSQUEDA EN ANCHURA (DETALLADO):
b_anchura = busquee.BúsquedaEnAnchura(detallado=True)
print(b_anchura.buscar(ProblemaPentominos))

# BUSQUEDA ÓPTIMA:
# b_optima = busquee.BúsquedaÓptima(detallado=True)
# print(b_optima.buscar(ProblemaPentominos))



# Dudas:
#  - ¿Debe continuar hasta recorrer todo el grafo? No, debe continuar hasta que
#                    encuentre una solución.
#  - ¿Qué posibles mejoras podríamos añadir?

# ¿Cuantas soluciones para un mismo tablero?
# Huecos aleatorios.
