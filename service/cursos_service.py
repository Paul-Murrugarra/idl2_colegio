# service/cursos_service.py
from repository.cursos_repository import CursosRepository

class CursosService:
    def __init__(self):
        self.repo = CursosRepository()

    def listar(self): return self.repo.listar()

    def obtener(self, id):
        c = self.repo.obtener(id)
        if not c:
            return {"error": "Curso no encontrado"}, 404
        return c

    def crear(self, data):
        nombre = data.get("nombre")
        duracion = data.get("duracion")
        if not nombre or duracion is None:
            return {"error": "Nombre y duración son requeridos"}, 400
        new_id = self.repo.crear(nombre, duracion)
        return {"id": new_id, "nombre": nombre, "duracion": duracion}


    def actualizar(self, id, data):
        if not self.repo.obtener(id):
            return {"error": "Curso no encontrado"}, 404
        nombre = (data.get("nombre") or "").strip()
        descripcion = (data.get("descripcion") or "").strip()
        if not nombre or not descripcion:
            return {"error": "nombre y duración son obligatorios"}, 400
        rc = self.repo.actualizar(id, nombre, descripcion)
        if rc == 0:
            return {"error": "No se actualizó"}, 400
        return {"mensaje": "Curso actualizado"}

    def eliminar(self, id):
        rc = self.repo.eliminar(id)
        if rc == 0:
            return {"error": "Curso no encontrado"}, 404
        return {"mensaje": "Curso eliminado"}
