# dao/matriculas_dao.py
from db import get_connection

class MatriculasDAO:
    def listar(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM matriculas")
        rows = cursor.fetchall()
        cursor.close(); conn.close()
        return rows

    def obtener(self, id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM matriculas WHERE id=%s", (id,))
        row = cursor.fetchone()
        cursor.close(); conn.close()
        return row

    def crear(self, id_alumno, id_curso):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO matriculas (id_alumno, id_curso) VALUES (%s, %s)",
                       (id_alumno, id_curso))
        conn.commit()
        new_id = cursor.lastrowid
        cursor.close(); conn.close()
        return new_id

    def actualizar(self, id, id_alumno, id_curso):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE matriculas SET id_alumno=%s, id_curso=%s WHERE id=%s",
                       (id_alumno, id_curso, id))
        conn.commit()
        rc = cursor.rowcount
        cursor.close(); conn.close()
        return rc

    def eliminar(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM matriculas WHERE id=%s", (id,))
        conn.commit()
        rc = cursor.rowcount
        cursor.close(); conn.close()
        return rc
