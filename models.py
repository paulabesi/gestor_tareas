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
