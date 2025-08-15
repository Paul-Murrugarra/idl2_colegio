# dao/cursos_dao.py
from db import get_connection

class CursosDAO:
    def listar(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM cursos")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows

    def obtener(self, id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM cursos WHERE id = %s", (id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return row

    def crear(self, nombre, duracion):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO cursos (nombre, duracion) VALUES (%s, %s)",
            (nombre, duracion)
        )
        conn.commit()
        new_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return new_id

    def actualizar(self, id, nombre, duracion):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE cursos SET nombre=%s, duracion=%s WHERE id=%s",
            (nombre, duracion, id)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return id

    def eliminar(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM cursos WHERE id=%s", (id,))
        conn.commit()
        cursor.close()
        conn.close()
        return id
