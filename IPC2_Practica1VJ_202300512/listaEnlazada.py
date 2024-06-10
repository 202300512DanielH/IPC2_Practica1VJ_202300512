from nodo import Nodo
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.contador = 0

    def agregar_tarea(self, nombre, descripcion):
        self.contador += 1
        nueva_tarea = Nodo(self.contador, nombre, descripcion)
        if not self.cabeza:
            self.cabeza = nueva_tarea
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nueva_tarea
        print(f"Tarea '{nombre}' agregada con ID {self.contador}.")

    def marcar_en_progreso(self, id):
        actual = self.cabeza
        while actual:
            if actual.id == id:
                actual.estado = "En progreso"
                print(f"\nTarea con ID {id} marcada como 'En progreso'.")
                return
            actual = actual.siguiente
        print(f"\nTarea con ID {id} no encontrada.")

    def terminar_tarea(self, id):
        actual = self.cabeza
        anterior = None
        while actual:
            if actual.id == id:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                print(f"\nTarea con ID {id} eliminada.")
                return
            anterior = actual
            actual = actual.siguiente
        print(f"\nTarea con ID {id} no encontrada.")

    def imprimir_tareas(self):
        if not self.cabeza:
            print("\n=============No tienes actividades pendientes=============")
        else:
            print("=============Tareas=============")
            actual = self.cabeza
            while actual:
                print(f"\nID: {actual.id}")
                print(f"Nombre: {actual.nombre}")
                print(f"Descripción: {actual.descripcion}")
                print(f"Estado: {actual.estado}\n")
                actual = actual.siguiente

    def ver_lista(self):
        try:
            import graphviz
        except ImportError:
            print("Graphviz no está instalado.")
            return

        dot = graphviz.Digraph(comment='Lista de Tareas')
        dot.attr(rankdir='LR')  # Alinear horizontalmente
        dot.attr('node', shape='record', style='filled', fillcolor='lightblue2')

        actual = self.cabeza
        while actual:
            label = f"<f0> ID: {actual.id} | Nombre: {actual.nombre} | Descripción: {actual.descripcion} | Estado: {actual.estado} | <f1> siguiente"
            dot.node(f'nodo{actual.id}', label)
            if actual.siguiente:
                dot.edge(f'nodo{actual.id}:f1', f'nodo{actual.siguiente.id}:f0')
            actual = actual.siguiente

        dot.render('lista_tareas', view=True)

    def ver_informacion(self):
        print("\nDesarrollador: Daniel Andreé Hernandez Flores\nCarnet: 202300512")
