# repository/profesores_repository.py
from dao.profesores_dao import ProfesoresDAO

class ProfesoresRepository:
    def __init__(self):
        self.dao = ProfesoresDAO()

    def listar(self): return self.dao.listar()
    def obtener(self, id): return self.dao.obtener(id)
    def crear(self, nombre, especialidad): return self.dao.crear(nombre, especialidad)
    def actualizar(self, id, nombre, especialidad): return self.dao.actualizar(id, nombre, especialidad)
    def eliminar(self, id): return self.dao.eliminar(id)
