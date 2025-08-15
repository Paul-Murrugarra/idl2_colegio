# repository/matriculas_repository.py
from dao.matriculas_dao import MatriculasDAO

class MatriculasRepository:
    def __init__(self):
        self.dao = MatriculasDAO()

    def listar(self): return self.dao.listar()
    def obtener(self, id): return self.dao.obtener(id)
    def crear(self, id_alumno, id_curso): return self.dao.crear(id_alumno, id_curso)
    def actualizar(self, id, id_alumno, id_curso): return self.dao.actualizar(id, id_alumno, id_curso)
    def eliminar(self, id): return self.dao.eliminar(id)
