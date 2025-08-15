from dao.alumnos_dao import AlumnosDAO

class AlumnosRepository:
    def __init__(self):
        self.dao = AlumnosDAO()

    def listar(self):
        return self.dao.listar()

    def obtener(self, id):
        return self.dao.obtener(id)

    def crear(self, data):
        return self.dao.crear(data)

    def actualizar(self, id, data):
        return self.dao.actualizar(id, data)

    def eliminar(self, id):
        return self.dao.eliminar(id)
