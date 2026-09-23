import ZODB
import ZODB.FileStorage


class BaseDatos:

    def __init__(self, archivo="active_x.fs"):
        self.storage = ZODB.FileStorage.FileStorage(archivo)
        self.db = ZODB.DB(self.storage)
        self.connection = self.db.open()
        self.root = self.connection.root()

    def cerrar(self):
        self.connection.close()
        self.db.close()
        self.storage.close()
