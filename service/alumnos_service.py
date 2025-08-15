from repository.alumnos_repository import AlumnosRepository

class AlumnosService:
    def __init__(self):
        self.repo = AlumnosRepository()

    def listar(self):
        return self.repo.listar()

    def obtener(self, id):
        alumno = self.repo.obtener(id)
        if not alumno:
            return {"error": "Alumno no encontrado"}, 404
        return alumno

    def crear(self, data):
        if not data.get("nombre") or not data.get("edad"):
            return {"error": "Datos incompletos"}, 400
        new_id = self.repo.crear(data)
        return {"id": new_id, "mensaje": "Alumno creado"}

    def actualizar(self, id, data):
        if not self.repo.obtener(id):
            return {"error": "Alumno no encontrado"}, 404
        self.repo.actualizar(id, data)
        return {"mensaje": "Alumno actualizado"}

    def eliminar(self, id):
        if not self.repo.obtener(id):
            return {"error": "Alumno no encontrado"}, 404
        self.repo.eliminar(id)
        return {"mensaje": "Alumno eliminado"}
