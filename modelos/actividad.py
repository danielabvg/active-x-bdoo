from persistent import Persistent


class Actividad(Persistent):

    def __init__(self, id_actividad, nombre, descripcion,
                 costo, cupo_maximo):
        self.id_actividad = id_actividad
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo
        self.cupo_maximo = cupo_maximo

    def consultar_clases(self, clases):
        return [
            clase
            for clase in clases
            if clase.actividad.id_actividad == self.id_actividad
        ]

    def calcular_ingresos(self, pagos):
        return sum(
            pago.monto
            for pago in pagos
            if pago.esta_pagado()
            and pago.inscripcion.clase.actividad.id_actividad == self.id_actividad
        )

    def __str__(self):
        return f"{self.id_actividad} - {self.nombre}"