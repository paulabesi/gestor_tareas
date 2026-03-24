"""SQL"""
import sqlite3
conexion = sqlite3.connect("tareas.db")
cursor = conexion.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tareas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        descripcion TEXT,
        completada INTEGER DEFAULT 0
    )
""")
cursor.execute("""
    INSERT INTO tareas (titulo, descripcion, completada)
    VALUES (?, ?, ?)
""", ("Guitarra", "practicar 1 hora", 0))

conexion.commit()
cursor.execute("SELECT * FROM tareas")
print(cursor.fetchall())
