from persistent import Persistent


class Inscripcion(Persistent):

    def __init__(self, id_inscripcion, usuario, clase,
                 fecha_inscripcion, estado="Activa"):
        self.id_inscripcion = id_inscripcion
        self.usuario = usuario
        self.clase = clase
        self.fecha_inscripcion = fecha_inscripcion
        self.estado = estado

    def registrar(self):
        if self.clase.agregar_usuario(self.usuario):
            self.estado = "Activa"
            self._p_changed = True
            return True

        self.estado = "Cancelada"
        self._p_changed = True
        return False

    def cancelar(self):
        self.clase.cancelar_usuario(self.usuario)
        self.estado = "Cancelada"
        self._p_changed = True
        return True

    def esta_activa(self):
        return self.estado == "Activa"

    def __str__(self):
        return f"{self.id_inscripcion} - {self.usuario.nombre}"