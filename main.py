from persistencia.base_datos import BaseDatos


base = BaseDatos()

print("Base de datos abierta correctamente.")
print("Root:", base.root)

base.cerrar()

print("Base de datos cerrada correctamente.")
