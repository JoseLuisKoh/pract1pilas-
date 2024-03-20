
class Pila:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.elementos = []
        self.tope = 0

    def insertar(self, elemento):
        if self.tope < self.capacidad:
            self.elementos.append(elemento)
            self.tope += 1
            print(f"Insertado {elemento}. TOPE = {self.tope}")
        else:
            print("Error: desbordamiento")

    def eliminar(self):
        if self.tope > 0:
            elemento = self.elementos.pop()
            self.tope -= 1
            print(f"Eliminado {elemento}. TOPE = {self.tope}")
        else:
            print("Error: subdesbordamiento")


# Crear una pila con capacidad máxima para 8 elementos
pila = Pila(8)

# Operaciones
pila.insertar("X")
pila.insertar("Y")
pila.eliminar()
pila.eliminar()
pila.eliminar()
pila.insertar("V")
pila.insertar("W")
pila.eliminar()
pila.insertar("R")
