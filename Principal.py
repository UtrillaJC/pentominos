# ----------------------------- MODULOS -----------------------------
import Modulos.Mapa as map
import Modulos.Fichas as fic
import Modulos.problema_espacio_estados as probee
import Modulos.búsqueda_espacio_estados as busquee
import copy

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
#mapa = map.Mapa(filas, columnas)

# Paso 1: definición de los estados del problema.
#estadoInicial = (None, None, 0,0)

# Paso 2: definición de las funciones aplicabilidad y aplicación
#    - Método ponerFicha:
#         · Aplicabilidad: el mapa tiene los huecos vacíos de la ficha a
#                          partir de las coordenadas x, y.


#    - Método quitarFicha:
#         · Aplicabilidad: la ficha de la posición x, y coincide con la
#                          ficha que quiero eliminar.



# ------------------------ PRUEBAS DE LAS CLASES ------------------------
# Atributos
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

# Líneas de prueba
mapa_prueba = map.Mapa(filas, columnas)
# mapa_prueba.marcarCasilla(1, 2)
# mapa_prueba.marcarCasilla(1, 1)
mapa_prueba.mostrarMapa()

# Probando la clase fichas
ficha = fic.Fichas()
# ficha.listadoFichas()
ficha.dibujarFichas('V')
miFicha1 = ficha.cogerFicha('Z', 3)
print("Añadimos la ficha: ")
mapa_prueba.anadirFicha(0, 0, miFicha1)
print("Volvemos a añadir la misma ficha: ")
mapa_prueba.anadirFicha(0, 0, miFicha1)
print("Añadimos la ficha V:")

print("Coger ficha: " + str(ficha.cogerFicha('V', 3)))
mapa_prueba.anadirFicha(1,1, ficha.cogerFicha("V", 3))


mapa_prueba.mostrarMapa()
mapa_prueba.quitarFicha(0, 0, miFicha1)
mapa_prueba.mostrarMapa()
print("El nº de casillas marcadas es: " + str(mapa_prueba.numCasillasMarcadas()))
print("El nº de casillas desmarcadas es: " + str(mapa_prueba.numCasillasDesmarcadas()))