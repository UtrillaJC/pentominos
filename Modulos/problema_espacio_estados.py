# Clase Acción: para cada una de las acciones que se definan en un problema
#               utilizaremos esta clase
class Acción:

    # Constructor

    def __init__(self, nombre='', aplicabilidad=None, aplicación=None,
                 coste=None):
        self.nombre = nombre                                # Identificador de la acción
        self.aplicabilidad = aplicabilidad                  # Método de aplicabilidad de la acción
        self.aplicación = aplicación                        # Método de aplicacion de la acción
        self.coste = coste                                  # Método de coste (optativo)

    # Condición de aplicabilidad: evalua si una acción es aplicable o no
    def es_aplicable(self, estado):
        if self.aplicabilidad is None:                      # Si no se define el método aplicabilidad...
            raise NotImplementedError(                      # ...devuelve un error (NotImplementedError)
                'Aplicabilidad de la acción no implementada')
        else:                                               # En caso contrario...
            return self.aplicabilidad(estado)               # ...aplica el método y devuelve: True (se puede aplicar
                                                            # la acción) o False (no se puede aplicar la acción)

    # Aplicación: aplica la acción correspondiente a un estado
    def aplicar(self, estado):
        if self.aplicar is None:                            # Si no se define el método aplicar...
            raise NotImplementedError(                      # ...devuelve un error (NotImplementedError)
                'Aplicación de la acción no implementada')
        else:                                               # En caso contrario...
            return self.aplicación(estado)                  # ...aplica la acción y devuelve el nuevoEstado

    # Si el problema lo requiere, se calculará el coste de aplicar la acción
    def coste_de_aplicar(self, estado):
        if self.coste is None:                      # Si no se define el método coste...
            return 1                                # ...devuelve 1
        else:                                       # En caso contrario...
            return self.coste(estado)               # ...devuelve el coste asociado a dicho estado

    # Representación como cadena de una instancia de la clase Acción
    def __str__(self):
        return 'Acción: {}'.format(self.nombre)

# Clase ProblemaEspacioEstados: con esta clase definiremos el problema a tratar.

class ProblemaEspacioEstados:

    # Constructor

    def __init__(self, acciones, estado_inicial=None, estados_finales=None):
        if not isinstance(acciones, list):                                  # Si acciones no es de tipo list
            raise TypeError('Debe proporcionarse una lista de acciones')    # ...devuelve un error (TypeError)
        self.acciones = acciones                                            # Acciones (todas)
        self.estado_inicial = estado_inicial                                # Estado inicial
        self.estados_finales = estados_finales                              # Lista de estados finales


    # ¿es estado un estado final?
    def es_estado_final(self, estado):              # Devuelve si dicho estado es igual a alguno de los
        return estado in self.estados_finales       # estados finales

    # ¿Cuáles son las acciones que podemos aplicar a un estado concreto?
    def acciones_aplicables(self, estado):
        return (acción                              # Devuelve aquellas acciones
            for acción in self.acciones             # de todas las acciones disponibles
                if acción.es_aplicable(estado))     # que se puedan aplicar a un estado
