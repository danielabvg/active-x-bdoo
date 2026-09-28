from persistent import Persistent


class Entrenador(Persistent):

    def __init__(self, id_entrenador, nombre, especialidad, telefono):
        self.id_entrenador = id_entrenador
        self.nombre = nombre
        self.especialidad = especialidad
        self.telefono = telefono

    def asignar_clase(self, clase):
        clase.entrenador = self
        clase._p_changed = True
        return clase

    def consultar_clases(self, clases):
        return [
            clase
            for clase in clases
            if clase.entrenador.id_entrenador == self.id_entrenador
        ]

    def __str__(self):
        return f"{self.id_entrenador} - {self.nombre}"