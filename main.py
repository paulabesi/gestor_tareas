"""main"""
from db import crear_tabla, crear_tarea, marcar_completada, eliminar_tarea, obtener_tareas

crear_tabla()

while True:
    num_accion = input(
        "Escoja lo que quiere hacer:\n1. Crear tarea\n2. Listar tareas\n3. Marcar tarea como completada\n4. Eliminar tarea\n5. Salir\n")
    if num_accion == "1":
        titulo = input("Escriba el titulo de la tarea\n")
        descripcion = input("Escriba la descripcion\n")
        completada = (
            input("Escriba True si esta completa o False si no lo esta\n")) == "True"
        crear_tarea(titulo, descripcion, completada)
    elif num_accion == "2":
        for tarea in obtener_tareas():
            print(
                f"ID: {tarea[0]} | Titulo: {tarea[1]} | Descripcion: {tarea[2]} | Completada:  {'Sí' if tarea[3] else 'No'}")
    elif num_accion == "3":
        try:
            num_tarea_completada = int(
                input("Escriba la id de la tarea que desea marcar como completada \n"))
        except ValueError:
            print("Error debes escribir un numero")
            continue
        marcar_completada(num_tarea_completada)

    elif num_accion == "4":
        try:
            num_id_eliminar = int(
                input("Escriba el id de la tarea que quiere eliminar:\n"))
        except ValueError:
            print("Error debes ecribir un numero")
            continue
        eliminar_tarea(num_id_eliminar)
    elif num_accion == "5":
        break
    else:
        print("Error: orden no existente en el asistente")
