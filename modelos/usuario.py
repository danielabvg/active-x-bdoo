from persistent import Persistent


class Usuario(Persistent):

    def __init__(self, id_usuario, nombre, correo, telefono,
                 fecha_registro, estado="Activo"):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.fecha_registro = fecha_registro
        self.estado = estado

    def inscribirse(self, inscripcion):
        return inscripcion.registrar()

    def cancelar_inscripcion(self, inscripcion):
        return inscripcion.cancelar()

    def consultar_clases(self, inscripciones):
        return [
            inscripcion.clase
            for inscripcion in inscripciones
            if inscripcion.usuario.id_usuario == self.id_usuario
            and inscripcion.esta_activa()
        ]

    def consultar_pagos(self, pagos):
        return [
            pago
            for pago in pagos
            if pago.usuario.id_usuario == self.id_usuario
        ]

    def __str__(self):
        return f"{self.id_usuario} - {self.nombre}"