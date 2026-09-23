# 1. Listar usuarios

def listar_usuarios(root):
    return list(root.usuarios.values())


# 2. Buscar usuario por identidad

def buscar_usuario(root, id_usuario):
    return root.usuarios.get(id_usuario)


# 3. Listar entrenadores

def listar_entrenadores(root):
    return list(root.entrenadores.values())


# 4. Listar actividades

def listar_actividades(root):
    return list(root.actividades.values())


# 5. Mostrar clases disponibles

def clases_disponibles(root):
    return [
        clase
        for clase in root.clases.values()
        if clase.tiene_cupo()
    ]


# 6. Mostrar usuarios inscritos en una clase

def usuarios_de_clase(root, id_clase):
    clase = root.clases.get(id_clase)

    if clase is None:
        return []

    return list(clase.usuarios)


# 7. Mostrar clases de un usuario

def clases_de_usuario(root, id_usuario):
    usuario = root.usuarios.get(id_usuario)

    if usuario is None:
        return []

    return usuario.consultar_clases(root.inscripciones.values())


# 8. Mostrar clases impartidas por un entrenador

def clases_de_entrenador(root, id_entrenador):
    entrenador = root.entrenadores.get(id_entrenador)

    if entrenador is None:
        return []

    return entrenador.consultar_clases(root.clases.values())


# 9. Actividades con mayor número de inscritos

def actividades_mayor_demanda(root):
    resultados = []

    for actividad in root.actividades.values():

        clases = actividad.consultar_clases(root.clases.values())

        inscritos = sum(
            len(clase.usuarios)
            for clase in clases
        )

        resultados.append((actividad, inscritos))

    return sorted(
        resultados,
        key=lambda x: x[1],
        reverse=True
    )


# 10. Usuarios con pagos pendientes

def usuarios_pagos_pendientes(root):
    usuarios = []

    for pago in root.pagos.values():

        if not pago.esta_pagado():
            if pago.usuario not in usuarios:
                usuarios.append(pago.usuario)

    return usuarios


# 11. Calcular ingresos por actividad

def ingresos_por_actividad(root):

    resultados = []

    for actividad in root.actividades.values():

        ingresos = actividad.calcular_ingresos(
            root.pagos.values()
        )

        resultados.append((actividad, ingresos))

    return resultados


# 12. Clases que alcanzaron su cupo

def clases_llenas(root):
    return [
        clase
        for clase in root.clases.values()
        if not clase.tiene_cupo()
    ]


# 13. Consulta compleja
#
# Usuarios activos que tienen una inscripción activa
# en una clase llena y además cuentan con un pago pendiente.

def consulta_compleja(root):

    resultados = []

    for usuario in root.usuarios.values():

        if usuario.estado != "Activo":
            continue

        tiene_clase_llena = False
        tiene_pago_pendiente = False

        for inscripcion in root.inscripciones.values():

            if (
                inscripcion.usuario.id_usuario == usuario.id_usuario
                and inscripcion.esta_activa()
                and not inscripcion.clase.tiene_cupo()
            ):
                tiene_clase_llena = True

        for pago in root.pagos.values():

            if (
                pago.usuario.id_usuario == usuario.id_usuario
                and not pago.esta_pagado()
            ):
                tiene_pago_pendiente = True

        if tiene_clase_llena and tiene_pago_pendiente:
            resultados.append(usuario)

    return resultados