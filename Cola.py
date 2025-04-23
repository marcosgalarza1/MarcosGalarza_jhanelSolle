# Clase Nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

# Clase Cola
class Cola:
    def __init__(self):
        self.frente = None
        self.final = None

    # Operación 1: Encolar (enqueue)
    def enqueue(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.final is None:  
            self.frente = self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo

  
