def guardar_usuario(root, usuario):
    root.usuarios[usuario.id_usuario] = usuario


def guardar_entrenador(root, entrenador):
    root.entrenadores[entrenador.id_entrenador] = entrenador


def guardar_actividad(root, actividad):
    root.actividades[actividad.id_actividad] = actividad


def guardar_clase(root, clase):
    root.clases[clase.id_clase] = clase


def guardar_inscripcion(root, inscripcion):
    root.inscripciones[inscripcion.id_inscripcion] = inscripcion


def guardar_pago(root, pago):
    root.pagos[pago.id_pago] = pago


def guardar_horario(root, horario):
    root.horarios[horario.id_horario] = horario


def eliminar_usuario(root, id_usuario):
    if id_usuario in root.usuarios:
        del root.usuarios[id_usuario]
        return True
    return False


def eliminar_entrenador(root, id_entrenador):
    if id_entrenador in root.entrenadores:
        del root.entrenadores[id_entrenador]
        return True
    return False


def eliminar_actividad(root, id_actividad):
    if id_actividad in root.actividades:
        del root.actividades[id_actividad]
        return True
    return False


def eliminar_clase(root, id_clase):
    if id_clase in root.clases:
        del root.clases[id_clase]
        return True
    return False


def eliminar_inscripcion(root, id_inscripcion):
    if id_inscripcion in root.inscripciones:
        del root.inscripciones[id_inscripcion]
        return True
    return False


def eliminar_pago(root, id_pago):
    if id_pago in root.pagos:
        del root.pagos[id_pago]
        return True
    return False


def eliminar_horario(root, id_horario):
    if id_horario in root.horarios:
        del root.horarios[id_horario]
        return True
    return False