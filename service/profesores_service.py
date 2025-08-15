# service/profesores_service.py
from repository.profesores_repository import ProfesoresRepository

class ProfesoresService:
    def __init__(self):
        self.repo = ProfesoresRepository()

    def listar(self): return self.repo.listar()

    def obtener(self, id):
        p = self.repo.obtener(id)
        if not p:
            return {"error": "Profesor no encontrado"}, 404
        return p

    def crear(self, data):
        nombre = (data.get("nombre") or "").strip()
        especialidad = (data.get("especialidad") or "").strip()
        if not nombre or not especialidad:
            return {"error": "nombre y especialidad son obligatorios"}, 400
        new_id = self.repo.crear(nombre, especialidad)
        return {"id": new_id, "mensaje": "Profesor creado"}, 201

    def actualizar(self, id, data):
        if not self.repo.obtener(id):
            return {"error": "Profesor no encontrado"}, 404
        nombre = (data.get("nombre") or "").strip()
        especialidad = (data.get("especialidad") or "").strip()
        if not nombre or not especialidad:
            return {"error": "nombre y especialidad son obligatorios"}, 400
        rc = self.repo.actualizar(id, nombre, especialidad)
        if rc == 0:
            return {"error": "No se actualizó"}, 400
        return {"mensaje": "Profesor actualizado"}

    def eliminar(self, id):
        rc = self.repo.eliminar(id)
        if rc == 0:
            return {"error": "Profesor no encontrado"}, 404
        return {"mensaje": "Profesor eliminado"}
