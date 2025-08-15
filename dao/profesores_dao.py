# dao/profesores_dao.py
from db import get_connection

class ProfesoresDAO:
    def listar(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM profesores")
        rows = cursor.fetchall()
        cursor.close(); conn.close()
        return rows

    def obtener(self, id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM profesores WHERE id=%s", (id,))
        row = cursor.fetchone()
        cursor.close(); conn.close()
        return row

    def crear(self, nombre, especialidad):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO profesores (nombre, especialidad) VALUES (%s, %s)",
                       (nombre, especialidad))
        conn.commit()
        new_id = cursor.lastrowid
        cursor.close(); conn.close()
        return new_id

    def actualizar(self, id, nombre, especialidad):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE profesores SET nombre=%s, especialidad=%s WHERE id=%s",
                       (nombre, especialidad, id))
        conn.commit()
        rc = cursor.rowcount
        cursor.close(); conn.close()
        return rc

    def eliminar(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM profesores WHERE id=%s", (id,))
        conn.commit()
        rc = cursor.rowcount
        cursor.close(); conn.close()
        return rc
