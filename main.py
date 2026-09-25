from persistencia.base_datos import BaseDatos

from modelos.usuario import Usuario
from modelos.entrenador import Entrenador
from modelos.actividad import Actividad
from modelos.clase import Clase
from modelos.inscripcion import Inscripcion
from modelos.pago import Pago
from modelos.horario import Horario

from servicios.servicios import (
    guardar_usuario,
    guardar_entrenador,
    guardar_actividad,
    guardar_clase,
    guardar_inscripcion,
    guardar_pago,
    guardar_horario,
    eliminar_usuario
)

from consultas.consultas import (
    listar_usuarios,
    buscar_usuario,
    listar_entrenadores,
    listar_actividades,
    clases_disponibles,
    usuarios_de_clase,
    clases_de_usuario,
    clases_de_entrenador,
    actividades_mayor_demanda,
    usuarios_pagos_pendientes,
    ingresos_por_actividad,
    clases_llenas,
    consulta_compleja,
    historial_inscripciones
)


# ---------------------------------------
# ABRIR BASE DE DATOS
# ---------------------------------------

base = BaseDatos()
root = base.root

print("\n========== ACTIVE X BDOO ==========\n")


# ---------------------------------------
# CREATE
# ---------------------------------------

usuario1 = Usuario(
    "U001",
    "Daniela Bravo",
    "daniela@email.com",
    "2281234567",
    "2026-09-23"
)

usuario2 = Usuario(
    "U002",
    "Ana Lopez",
    "ana@email.com",
    "2289876543",
    "2026-09-23"
)

entrenador1 = Entrenador(
    "E001",
    "Carlos Perez",
    "Spinning",
    "2281111111"
)

actividad1 = Actividad(
    "A001",
    "Spinning",
    "Clase de spinning",
    150,
    2
)

actividad2 = Actividad(
    "A002",
    "Yoga",
    "Clase de yoga",
    120,
    3
)

horario1 = Horario(
    "H001",
    "Lunes",
    "08:00",
    "09:00"
)

clase1 = Clase(
    "C001",
    actividad1,
    entrenador1,
    "2026-09-28",
    "08:00",
    2,
    horario1
)

clase2 = Clase(
    "C002",
    actividad2,
    entrenador1,
    "2026-09-29",
    "10:00",
    3
)


guardar_usuario(root, usuario1)
guardar_usuario(root, usuario2)

guardar_entrenador(root, entrenador1)

guardar_actividad(root, actividad1)
guardar_actividad(root, actividad2)

guardar_horario(root, horario1)

guardar_clase(root, clase1)
guardar_clase(root, clase2)


# ---------------------------------------
# INSCRIPCIONES
# ---------------------------------------

inscripcion1 = Inscripcion(
    "I001",
    usuario1,
    clase1,
    "2026-09-23"
)

inscripcion2 = Inscripcion(
    "I002",
    usuario2,
    clase1,
    "2026-09-23"
)

inscripcion3 = Inscripcion(
    "I003",
    usuario1,
    clase2,
    "2026-09-23"
)

usuario1.inscribirse(inscripcion1)
usuario2.inscribirse(inscripcion2)
usuario1.inscribirse(inscripcion3)

guardar_inscripcion(root, inscripcion1)
guardar_inscripcion(root, inscripcion2)
guardar_inscripcion(root, inscripcion3)


# ---------------------------------------
# PAGOS
# ---------------------------------------

pago1 = Pago(
    "P001",
    usuario1,
    inscripcion1,
    150,
    "2026-09-23",
    "Pagado"
)

pago2 = Pago(
    "P002",
    usuario2,
    inscripcion2,
    150,
    "2026-09-23",
    "Pendiente"
)

pago3 = Pago(
    "P003",
    usuario1,
    inscripcion3,
    120,
    "2026-09-23",
    "Pagado"
)

guardar_pago(root, pago1)
guardar_pago(root, pago2)
guardar_pago(root, pago3)


base.guardar()


# ---------------------------------------
# READ
# ---------------------------------------

print("USUARIOS")
for usuario in listar_usuarios(root):
    print(usuario)


print("\nBUSCAR USUARIO POR IDENTIDAD")
usuario = buscar_usuario(root, "U001")
print(usuario)


print("\nENTRENADORES")
for entrenador in listar_entrenadores(root):
    print(entrenador)


print("\nACTIVIDADES")
for actividad in listar_actividades(root):
    print(actividad)


# ---------------------------------------
# UPDATE
# ---------------------------------------

usuario1.telefono = "2289999999"
usuario1._p_changed = True

base.guardar()

print("\nUSUARIO ACTUALIZADO")
print(usuario1.telefono)


# ---------------------------------------
# RELACIONES
# ---------------------------------------

print("\nUSUARIOS DE LA CLASE C001")

for usuario in usuarios_de_clase(root, "C001"):
    print(usuario)


print("\nCLASES DE U001")

for clase in clases_de_usuario(root, "U001"):
    print(clase)


print("\nCLASES DEL ENTRENADOR E001")

for clase in clases_de_entrenador(root, "E001"):
    print(clase)


# ---------------------------------------
# COMPORTAMIENTO
# ---------------------------------------

print("\nLUGARES DISPONIBLES EN C001:")
print(clase1.lugares_disponibles())

print("\n¿C001 TIENE CUPO?")
print(clase1.tiene_cupo())


# ---------------------------------------
# CONSULTAS
# ---------------------------------------

print("\nCLASES DISPONIBLES")

for clase in clases_disponibles(root):
    print(clase)


print("\nACTIVIDADES CON MAYOR DEMANDA")

for actividad, cantidad in actividades_mayor_demanda(root):
    print(actividad.nombre, "-", cantidad, "inscritos")


print("\nUSUARIOS CON PAGOS PENDIENTES")

for usuario in usuarios_pagos_pendientes(root):
    print(usuario)


print("\nINGRESOS POR ACTIVIDAD")

for actividad, ingresos in ingresos_por_actividad(root):
    print(actividad.nombre, "-", ingresos)


print("\nCLASES LLENAS")

for clase in clases_llenas(root):
    print(clase)


print("\nCONSULTA COMPLEJA")

for usuario in consulta_compleja(root):
    print(usuario)

print("\nHISTORIAL COMPLETO POR USUARIO")
for usuario in historial_inscripciones(root, "U001"):
    print(usuario)

# ---------------------------------------
# DELETE
# ---------------------------------------

usuario_prueba = Usuario(
    "U999",
    "Usuario Prueba",
    "prueba@email.com",
    "2280000000",
    "2026-09-23"
)

guardar_usuario(root, usuario_prueba)
base.guardar()

print("\nUSUARIO DE PRUEBA CREADO:")
print(buscar_usuario(root, "U999"))

eliminar_usuario(root, "U999")
base.guardar()

print("\nUSUARIO DE PRUEBA ELIMINADO:")
print(buscar_usuario(root, "U999"))


# ---------------------------------------
# CERRAR
# ---------------------------------------

base.cerrar()

print("\nBase de datos cerrada correctamente.")


# ---------------------------------------
# PRUEBA DE PERSISTENCIA
# ---------------------------------------

base = BaseDatos()
root = base.root

print("\n========== PRUEBA DE PERSISTENCIA ==========")

usuario = root.usuarios.get("U001")

print("Usuario recuperado después de reabrir:")
print(usuario)

base.cerrar()