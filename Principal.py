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

acciones = []

# DUDA: ¿Habría que hacer un filtrado de las acciones?
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

# print(ProblemaPentominos.es_estado_final(estadoInicial))
# Dime el nombre de todas las acciones que sean aplicables
for accion in ProblemaPentominos.acciones_aplicables(estadoInicial):
    print(accion.nombre)

# Creamos una instancia de búsqueda en anchura Y detallado
b_profundidad = busquee.BúsquedaEnProfundidad(detallado=True)
print(b_profundidad.buscar(ProblemaPentominos))

# Dudas:
#  - ¿Debe continuar hasta recorrer todo el grafo? No, debe continuar hasta que
#                    encuentre una solución.
#  - ¿Qué posibles mejoras podríamos añadir?