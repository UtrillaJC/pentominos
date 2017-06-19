# ----------------------------- MODULOS -----------------------------
import Modulos.Mapa as map
import Modulos.Fichas as fic
import Modulos.RellenarMapa as accion
import Modulos.problema_espacio_estados as probee
import Modulos.búsqueda_espacio_estados as busquee
import sys, timeit, functools

# --------------- CONSTANTES Y VARIABLES GLOBALES -------------------
menu_actions = {}                  # Diccionario de menus
fichas = fic.Fichas()              # Todas las fichas del problema
numFilas = None                    # Nº de filas del mapa
numColumnas = None                 # Nº de columnas del mapa

problemaPentominos = None          # Representa el problema
acciones = []                      # Representa las acciones del problema
estadoInicial = None

# ------------------------ MÉTODOS AUXILIARES -----------------------
# definicionProblema: método que define el Problema Pentonimos
def definicionProblema():
    # Necesitamos indicarle a Python que queremos utilizar una variable global
    global numFilas, numColumnas

    # Mientras filas no tenga un valor asignado...
    while not numFilas:
        try:
            numFilas = int(input("Elija el nº de filas: "))
        except ValueError:
            print("Los datos introducidos no son correctos")

    # Mientras columnas no tenga un valor asignado...
    while not numColumnas:
        try:
            numColumnas = int(input("Elija el nº de columnas: "))
        except ValueError:
            print("Los datos introducidos no son correctos")

    # Mejora: eliminamos aquellas acciones que ya sabemos con certeza
    #         que no se pueden aplicar. Nos referimos a aquellas accio-
    #         nes en las que partiendo de una coordenada (x,y), se sa-
    #         del mapa

    # De cada una de las fichas
    for keys, values in fichas.dicFichas.items():

        # Calculamos para cada una de las coordenadas (x,y)...
        for x in range(0, numFilas, 1):
            for y in range(0, numColumnas, 1):

                # ...Si la acción es aplicable
                fueraLimites = False

                for tupla in values.listaPosiciones:
                    if x + tupla[0] > numColumnas or y + tupla[1] > numFilas:
                        fueraLimites = True
                # Si la acción no está fuera de los límites...
                if not fueraLimites:
                    # ...creamos la acción
                    acciones.append(accion.RellenarMapa(x, y, values))

    # Necesitamos indicarle a Python que queremos utilizar una variable global
    global estadoInicial
    global problemaPentominos

    mapa = map.Mapa(numFilas, numColumnas)
    estadoInicial = mapa

    problemaPentominos = probee.ProblemaEspacioEstados(
        acciones, estadoInicial, []
    )

    for laaccion in problemaPentominos.acciones_aplicables(estadoInicial):
        print(laaccion.nombre)


# h1: heurística que cuenta el número de huecos vacíos
# ------------------------ SCRIPT PRINCIPAL ------------------------
def h1(nodo):
    estado = nodo.estado

    huecosCerrados = 0

    for i in range(0, estado.numeroFilas(), 1):
        for j in range(0, estado.numeroColumnas(), 1):
            # Si la casilla está desmarcada...
            if estado.valorCasilla(i, j) == 0:
                # Calculamos los índices...
                arriba = j - 1
                abajo = j + 1
                derecha = i + 1
                izquierda = i - 1

                # Comprobamos si nos salimos del rango...
                if (arriba < 0) or (izquierda < 0) or (abajo > estado.numeroFilas() - 1) or (
                    derecha > estado.numeroColumnas() - 1):
                    if (arriba < 0) and (izquierda < 0):
                        # Comprobamos casillas: derecha, abajo
                        if estado.valorCasilla(derecha, j) == 1 and estado.valorCasilla(i, abajo) == 1:
                            huecosCerrados += 1
                    elif izquierda < 0 and (abajo > estado.numeroFilas() - 1):
                        # Comprobamos casillas: derecha, arriba
                        if estado.valorCasilla(derecha, j) == 1 and estado.valorCasilla(i, arriba) == 1:
                            huecosCerrados += 1

                    elif (abajo > estado.numeroFilas() - 1) and (derecha > estado.numeroColumnas() - 1):
                        # Comprobamos casillas: arriba, izquierda
                        if estado.valorCasilla(i, arriba) == 1 and estado.valorCasilla(izquierda, j) == 1:
                            huecosCerrados += 1

                    elif arriba < 0 and (derecha > estado.numeroColumnas() - 1):
                        # Comprobamos casillas: abajo, izquierda
                        if estado.valorCasilla(i, abajo) == 1 and estado.valorCasilla(izquierda, j) == 1:
                            huecosCerrados += 1

                    elif arriba < 0:
                        # Comprobamos casillas: izquierda, derecha, abajo
                        if estado.valorCasilla(izquierda, j) == 1 and estado.valorCasilla(derecha, j) == 1 \
                                and estado.valorCasilla(i, abajo) == 1:
                            huecosCerrados += 1

                    elif izquierda < 0:
                        # Comprobamos casillas: derecha, arriba, abajo
                        if estado.valorCasilla(derecha, j) == 1 and estado.valorCasilla(i, arriba) == 1 \
                                and estado.valorCasilla(i, abajo) == 1:
                            huecosCerrados += 1

                    elif abajo > estado.numeroFilas() - 1:
                        # Comprobamos casillas: arriba, izquierda, derecha
                        if estado.valorCasilla(i, arriba) == 1 and estado.valorCasilla(izquierda, j) == 1 \
                                and estado.valorCasilla(derecha, j) == 1:
                            huecosCerrados += 1

                    elif derecha > estado.numeroColumnas() - 1:
                        # Comprobamos casillas: izquierda, arriba, abajo
                        if estado.valorCasilla(izquierda, j) == 1 and estado.valorCasilla(i, arriba) == 1 \
                                and estado.valorCasilla(i, abajo) == 1:
                            huecosCerrados += 1
                # Si no se sale del rango, comprobamos casillas: arriba, abajo, derecha, izquierda
                elif estado.valorCasilla(derecha, j) == 1 and estado.valorCasilla(izquierda, j) == 1 \
                     and estado.valorCasilla(i, arriba) == 1 and estado.valorCasilla(i, abajo) == 1:
                    huecosCerrados += 1

    return huecosCerrados

# menuPrincipal: método que representa al menú principal por pantalla.
def menuPrincipal():
    # Definimos el problema
    definicionProblema()

    # Ejecuta el comando clear (limpia la consola)
    print("\n" * 100)

    # Se muestran las opciones disponibles
    print("+----------------- Bienvenido ------------------+")
    print("| Por favor, elige el menu que quieres iniciar: |")
    print("|    1. Ejecutar búsqueda informada             |")
    print("|    2. Ejecutar búsqueda no informada          |")
    print("+-----------------------------------------------+")
    print("|    0. Quitar                                  |")
    print("+-----------------------------------------------+")

    opcion = input(" >>  ")
    ejecutarMenu(opcion)
    return

# ejecutarMenu: método que ejecuta cualquier menú de los disponibles
def ejecutarMenu(opcion):
    # Capturamos la elección
    eleccion = opcion.lower()          # Se pasa la opción a minúscula

    # Si no se ha elegido nada...
    if eleccion == '':
        menu_acciones['menuPrincipal']()   # Se vuelve al menú principal
    # En caso contrario...
    else:
        try:
            menu_acciones[eleccion]()  # Se carga el menú elegido
        except KeyError:    # Si hemos elegido una acción que no existe
            print ("Selección no valida, intentelo de nuevo.")
            menu_acciones['menuPrincipal']()
    return

# Menu 1: BUSQUEDA INFORMADA
def menuBusquedaNoInformada():
    print("\n" * 100)
    # Se muestran las opciones disponibles
    print("+----------- BUSQUEDA NO INFORMADA -------------+")
    print("| Elija el algoritmo que quieres ejecutar:      |")
    print("|    1. B. no Informada en profundidad          |")
    print("|    2. B. no Informada en anchura              |")
    print("+-----------------------------------------------+")
    print("|    9. Volver al menú principal                |")
    print("|    0. Salir del programa                      |")
    print("+-----------------------------------------------+")

    eleccion = input(" >>  ")

    # Ejecutamos el algoritmo correspondiente
    if eleccion.lower() == '1':
        bProfundidad = busquee.BúsquedaEnProfundidad(detallado=True)
        # print("Tiempo de ejecución: %f" % timeit.timeit(functools.partial(bProfundidad.buscar, problemaPentominos),
        #                                                number=1))
        print(bProfundidad.buscar(problemaPentominos))
        # print("Tiempo de ejecución: %f" % timeit.repeat(functools.partial(bProfundidad.buscar, problemaPentominos),
        #                                               repeat=4, number=1))
        input("Pulse una tecla para volver al menú principal")
    elif eleccion.lower() == '2':
        bAnchura = busquee.BúsquedaEnAnchura(detallado=True)
        print("Tiempo de ejecución: %f" % timeit.timeit(functools.partial(bAnchura.buscar, problemaPentominos),
                                                        number=1))
        # print(bAnchura.buscar(problemaPentominos))
        # print("Tiempo de ejecución: %f" % timeit.repeat(functools.partial(bAnchura.buscar, problemaPentominos),
        #                                               repeat=2, number=1))
        input("Pulse una tecla para volver al menú principal")
    elif eleccion.lower() == '9':
        volver()
    elif eleccion.lower() == '0':
        salir()
    else:
        menu_acciones['2']()
    volver()
    return

# Menu 2: BUSQUEDA NO INFORMADA
def menuBusquedaInformada():
    print("\n" * 100)
    print("+------------- BUSQUEDA INFORMADA --------------+")
    print("| Elija el algoritmo que quieres ejecutar:      |")
    print("|    1. B. Informada primero el mejor           |")
    print("|    2. B. Informada A estrella (A*)            |")
    print("|    3. B. Informada Óptima                     |")
    print("+-----------------------------------------------+")
    print("|    9. Volver al menú principal                |")
    print("|    0. Quitar                                  |")
    print("+-----------------------------------------------+")

    eleccion = input(" >>  ")

    # Ejecutamos el algoritmo correspondiente
    if eleccion.lower() == '1':         # BUSQUEDA PRIMERO EL MEJOR
        bPrimeroElMejor = busquee.BúsquedaPrimeroElMejor(h1, detallado=True)
        print("Tiempo de ejecución: %f" % timeit.timeit(functools.partial(bPrimeroElMejor.buscar, problemaPentominos),
                                                        number=1))

        # print("Tiempo de ejecución: %f" % timeit.repeat(functools.partial(bPrimeroElMejor.buscar, problemaPentominos),
        #                                               repeat=2, number=1))
        input("Pulse una tecla para volver al menú principal")
    elif eleccion.lower() == '2':       # BUSQUEDA A ESTRELLA (A*)
        bAEstrella = busquee.BúsquedaAEstrella(h1, detallado=True)
        print("Tiempo de ejecución: %f" % timeit.timeit(functools.partial(bAEstrella.buscar, problemaPentominos),
                                                        number=1))
        # print(timeit.repeat("Tiempo de ejecución: %f" % functools.partial(bAEstrella.buscar, problemaPentominos),
        #                                               repeat=2, number=1))

        input("Pulse una tecla para volver al menú principal")
    elif eleccion.lower() == '3':       # BUSUQEDA OPTIMA
        bOptima = busquee.BúsquedaÓptima(detallado=True)
        print("Tiempo de ejecución: %f" % timeit.timeit(functools.partial(bOptima.buscar, problemaPentominos),
                                                        number=1))
        # print(timeit.repeat("Tiempo de ejecución: %f" % functools.partial(bOptima.buscar, problemaPentominos),
        #                                               repeat=2, number=1))
        input("Pulse una tecla para volver al menú principal")
    elif eleccion.lower() == '9':
        volver()
    elif eleccion.lower() == '0':
        salir()
    else:
        menu_acciones['1']()

    return

# volver: método que vuelve al menu principal
def volver():
    menu_acciones['menuPrincipal']()

# salir: método que finaliza la ejecución del programa
def salir():
    print("Desarrolladores:"
          "\n\t· Juan Carlos Utrilla - https://www.linkedin.com/in/juancarlosutrilla/"
          "\n\t· Carmen Rosal Malvar - https://www.linkedin.com/in/carmen-rosal-malvar-7a91b7130/")
    sys.exit()

# ==========================
#    DEFINICIONES DE MENU
# ==========================

menu_acciones = {
    'menuPrincipal': menuPrincipal,
    '1': menuBusquedaInformada,
    '2': menuBusquedaNoInformada,
    '9': volver,
    '0': salir,
}

menuPrincipal()