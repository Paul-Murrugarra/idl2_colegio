# service/matriculas_service.py
from repository.matriculas_repository import MatriculasRepository
from repository.alumnos_repository import AlumnosRepository
from repository.cursos_repository import CursosRepository

class MatriculasService:
    def __init__(self):
        self.repo = MatriculasRepository()
        self.alumnos_repo = AlumnosRepository()
        self.cursos_repo = CursosRepository()

    def listar(self): return self.repo.listar()

    def obtener(self, id):
        m = self.repo.obtener(id)
        if not m:
            return {"error": "Matrícula no encontrada"}, 404
        return m

    def crear(self, data):
        try:
            id_alumno = int(data.get("id_alumno"))
            id_curso = int(data.get("id_curso"))
        except Exception:
            return {"error": "id_alumno e id_curso deben ser enteros"}, 400

        if not self.alumnos_repo.obtener(id_alumno):
            return {"error": "Alumno no existe"}, 400
        if not self.cursos_repo.obtener(id_curso):
            return {"error": "Curso no existe"}, 400

        new_id = self.repo.crear(id_alumno, id_curso)
        return {"id": new_id, "mensaje": "Matrícula creada"}, 201

    def actualizar(self, id, data):
        if not self.repo.obtener(id):
            return {"error": "Matrícula no encontrada"}, 404

        try:
            id_alumno = int(data.get("id_alumno"))
            id_curso = int(data.get("id_curso"))
        except Exception:
            return {"error": "id_alumno e id_curso deben ser enteros"}, 400

        if not self.alumnos_repo.obtener(id_alumno):
            return {"error": "Alumno no existe"}, 400
        if not self.cursos_repo.obtener(id_curso):
            return {"error": "Curso no existe"}, 400

        rc = self.repo.actualizar(id, id_alumno, id_curso)
        if rc == 0:
            return {"error": "No se actualizó"}, 400
        return {"mensaje": "Matrícula actualizada"}

    def eliminar(self, id):
        rc = self.repo.eliminar(id)
        if rc == 0:
            return {"error": "Matrícula no encontrada"}, 404
        return {"mensaje": "Matrícula eliminada"}
