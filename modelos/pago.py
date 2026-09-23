from persistent import Persistent


class Pago(Persistent):

    def __init__(self, id_pago, usuario, inscripcion,
                 monto, fecha_pago, estado="Pendiente"):
        self.id_pago = id_pago
        self.usuario = usuario
        self.inscripcion = inscripcion
        self.monto = monto
        self.fecha_pago = fecha_pago
        self.estado = estado

    def registrar_pago(self):
        self.estado = "Pagado"
        self._p_changed = True
        return True

    def esta_pagado(self):
        return self.estado == "Pagado"

    def __str__(self):
        return f"{self.id_pago} - {self.usuario.nombre} - {self.estado}"