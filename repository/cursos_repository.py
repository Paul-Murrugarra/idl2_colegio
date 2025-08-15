# repository/cursos_repository.py
from dao.cursos_dao import CursosDAO

class CursosRepository:
    def __init__(self):
        self.dao = CursosDAO()

    def listar(self): return self.dao.listar()
    def obtener(self, id): return self.dao.obtener(id)
    def crear(self, nombre, descripcion): return self.dao.crear(nombre, descripcion)
    def actualizar(self, id, nombre, descripcion): return self.dao.actualizar(id, nombre, descripcion)
    def eliminar(self, id): return self.dao.eliminar(id)
