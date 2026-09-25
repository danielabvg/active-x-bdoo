from persistent import Persistent
from persistent.list import PersistentList


class Clase(Persistent):

    def __init__(self, id_clase, actividad, entrenador,
                 fecha, hora, cupo, horario=None):
        self.id_clase = id_clase
        self.actividad = actividad
        self.entrenador = entrenador
        self.fecha = fecha
        self.hora = hora
        self.cupo = cupo
        self.horario = horario
        self.usuarios = PersistentList()

    def tiene_cupo(self):
        return len(self.usuarios) < self.cupo

    def agregar_usuario(self, usuario):
        if not self.tiene_cupo():
            return False

        if usuario not in self.usuarios:
            self.usuarios.append(usuario)
            self._p_changed = True
            return True

        return False

    def lugares_disponibles(self):
        return self.cupo - len(self.usuarios)

    def cancelar_usuario(self, usuario):
        if usuario in self.usuarios:
            self.usuarios.remove(usuario)
            self._p_changed = True
            return True

        return False

    def __str__(self):
        return f"{self.id_clase} - {self.actividad.nombre}"