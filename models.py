"""clases"""


class Tarea():
    def __init__(self, id, titulo, descripcion, completada):
        self.id = id
        self.titulo = titulo
        self.descripcion = descripcion
        self.completada = bool(completada)

    def __str__(self):
        return (f"tarea {self.id},{self.titulo}, descripcion : {self.descripcion} , esta completada? {self.completada}")

    def marcar_completada(self):
        self.completada = True

    def to_dict(self):
        return {"id": self.id, "titulo": self.titulo, "descripcion": self.descripcion, "completada": self.completada}

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data["id"], data["titulo"], data["descripcion"], data["completada"])


class GestorTareas():
    def __init__(self):
        self.lista_tareas = []
        self.contador = 0

    def añadir_tarea(self, tarea):
        self.contador += 1
        tarea.id = self.contador
        self.lista_tareas.append(tarea)

    def eliminar_tarea(self, id):
        tarea = self.buscar_por_id(id)
        if tarea:
            self.lista_tareas.remove(tarea)
        else:
            print("No existe la tarea")

    def imprime_lista(self):
        if not self.lista_tareas:
            print("No hay nada en la lista de tareas")
            return
        for tarea in self.lista_tareas:
            print(
                f"tarea:{tarea.id}, titulo: {tarea.titulo}, descripcion: {tarea.descripcion}, completada? {tarea.completada}")

    def buscar_por_id(self, id):
        for tarea in self.lista_tareas:
            if tarea.id == id:
                return tarea
        return None
# cambio raro para git
