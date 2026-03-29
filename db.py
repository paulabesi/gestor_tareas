"""SQL"""
import sqlite3


def obtener_conexion():
    return sqlite3.connect("gestor_tareas/tareas.db")


def crear_tabla():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tareas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        descripcion TEXT,
        completada INTEGER DEFAULT 0
    )
""")
    conexion.commit()
    conexion.close()


def obtener_tareas():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM tareas")
    tareas = cursor.fetchall()
    conexion.close()
    return tareas


def crear_tarea(titulo, descripcion, completada):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("""INSERT INTO tareas(titulo, descripcion, completada)
                   VALUES(?,?,?)""", (titulo, descripcion, completada))
    conexion.commit()
    conexion.close()


def marcar_completada(id):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("""UPDATE tareas SET completada = 1 WHERE id = ?""", (id,))
    conexion.commit()
    conexion.close()


def eliminar_tarea(id):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("""DELETE FROM tareas WHERE id = ?""", (id,))
    conexion.commit()
    conexion.close()


def obtener_tareas_pendientes():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("""SELECT * FROM tareas WHERE completada = ?""", (0,))
    tareas = cursor.fetchall()
    conexion.close()
    return tareas


def obtener_tareas_completadas():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("""SELECT * FROM tareas WHERE completada = ?""", (1,))
    tareas = cursor.fetchall()
    conexion.close()
    return tareas


def obtener_tarea_por_id(id):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM tareas WHERE id = ?", (id,))
    tareas = cursor.fetchone()
    conexion.close()
    return tareas
