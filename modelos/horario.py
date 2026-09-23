from persistent import Persistent


class Horario(Persistent):

    def __init__(self, id_horario, dia, hora_inicio, hora_fin):
        self.id_horario = id_horario
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin

    def actualizar_horario(self, dia, hora_inicio, hora_fin):
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self._p_changed = True

    def consultar_horario(self):
        return f"{self.dia} {self.hora_inicio} - {self.hora_fin}"

    def __str__(self):
        return self.consultar_horario()