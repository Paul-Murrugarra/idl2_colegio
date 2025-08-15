from db import get_connection

class AlumnosDAO:
    def listar(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM alumnos")
        data = cursor.fetchall()
        conn.close()
        return data

    def obtener(self, id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM alumnos WHERE id=%s", (id,))
        data = cursor.fetchone()
        conn.close()
        return data

    def crear(self, data):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO alumnos (nombre, edad) VALUES (%s, %s)", 
                       (data["nombre"], data["edad"]))
        conn.commit()
        conn.close()
        return cursor.lastrowid

    def actualizar(self, id, data):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE alumnos SET nombre=%s, edad=%s WHERE id=%s", 
                       (data["nombre"], data["edad"], id))
        conn.commit()
        conn.close()
        return cursor.rowcount

    def eliminar(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM alumnos WHERE id=%s", (id,))
        conn.commit()
        conn.close()
        return cursor.rowcount
