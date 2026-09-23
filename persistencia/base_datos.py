import ZODB
import ZODB.FileStorage
import transaction
from persistent.mapping import PersistentMapping


class BaseDatos:

    def __init__(self, archivo="active_x.fs"):
        self.storage = ZODB.FileStorage.FileStorage(archivo)
        self.db = ZODB.DB(self.storage)
        self.connection = self.db.open()
        self.root = self.connection.root()

        self._crear_colecciones()

    def _crear_colecciones(self):

        colecciones = [
            "usuarios",
            "entrenadores",
            "actividades",
            "clases",
            "inscripciones",
            "pagos",
            "horarios"
        ]

        for nombre in colecciones:
            if not hasattr(self.root, nombre):
                setattr(self.root, nombre, PersistentMapping())

        transaction.commit()

    def guardar(self):
        transaction.commit()

    def cerrar(self):
        self.connection.close()
        self.db.close()
        self.storage.close()
