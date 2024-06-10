class Nodo:
    def __init__(self, id, nombre, descripcion):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = "pendiente"
        self.siguiente = None
