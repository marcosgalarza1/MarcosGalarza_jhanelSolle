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
        self.contador = 0  # 👈 contador para size()

    # Operación 1: Encolar (enqueue)
    def enqueue(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.final is None:  
            self.frente = self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo
            self.contador += 1  # 👈 aumenta el contador
    # Operación 2: Desencolar (dequeue)
    def dequeue(self):
        if self.frente is None:
            return None  # Cola vacía
        dato = self.frente.dato
        self.frente = self.frente.siguiente
        if self.frente is None:  # Si la cola queda vacía
            self.final = None
        return dato
    
    # Operación 3: Ver el frente (peek)
    def peek(self):
        if self.frente is None:
           
            return None  # Cola vacía
        return self.frente.dato
    # operacion 4: IsEmpty
    def is_empty(self):
        return self.frente is None  # Retorna True si la cola está vacía, False en caso contrario

    

    # Operación 5: Tamaño (size)
    def size(self):
        return self.contador  # Retorna el tamaño de la cola
    #mostrar la cola
    def mostrar(self):
        if self.frente is None:
          
            return
        actual = self.frente
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")  # Indica el final de la cola


 # Mostrar la cola 
    def mostrar(self):
        actual = self.frente
        elementos = []
        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        print("Cola:", " -> ".join(elementos) if elementos else "vacía")
# Ejemplo de uso
# ----------------------
cola = Cola()
cola.enqueue(100)
cola.enqueue(200)
cola.enqueue(300)
cola.mostrar()               # Cola: 100 -> 200 -> 300 
    
    
    