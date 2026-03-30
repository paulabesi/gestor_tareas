
"""gestor de tareas"""
from db import crear_tabla, crear_tarea, marcar_completada, eliminar_tarea, obtener_tareas, obtener_tareas_completadas, obtener_tareas_pendientes, obtener_tarea_por_id

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
        que_lista_quiere = input(
            "Que tipo de lista quiere?\na. Todas las tareas\nb. Solo las completadas\nc. Solo las pendientes\n")
        que_lista_quiere = que_lista_quiere.upper()
        if que_lista_quiere == "A":
            for tarea in obtener_tareas():
                print(
                    f"ID: {tarea[0]} | Titulo: {tarea[1]} | Descripcion: {tarea[2]} | Completada:  {'Sí' if tarea[3] else 'No'}")
        elif que_lista_quiere == "B":
            for tarea in obtener_tareas_completadas():
                print(
                    f"ID: {tarea[0]} | Titulo: {tarea[1]} | Descripcion: {tarea[2]} | Completada:  {'Sí' if tarea[3] else 'No'}")
        elif que_lista_quiere == "C":
            for tarea in obtener_tareas_pendientes():
                print(
                    f"ID: {tarea[0]} | Titulo: {tarea[1]} | Descripcion: {tarea[2]} | Completada:  {'Sí' if tarea[3] else 'No'}")
        else:
            print("Por favor escoja una letra de las que le hemos listado")
    elif num_accion == "3":
        try:
            num_tarea_completada = int(
                input("Escriba la id de la tarea que desea marcar como completada \n"))
        except ValueError:
            print("Error debes escribir un numero")
            continue
        tarea = obtener_tarea_por_id(num_tarea_completada)
        if tarea:
            marcar_completada(num_tarea_completada)
        else:
            print("Error tarea no encontrada")

    elif num_accion == "4":
        try:
            num_id_eliminar = int(
                input("Escriba el id de la tarea que quiere eliminar:\n"))
        except ValueError:
            print("Error debes ecribir un numero")
            continue
        tarea_a_eliminar = obtener_tarea_por_id(num_id_eliminar)
        if tarea_a_eliminar:
            eliminar_tarea(num_id_eliminar)
        else:
            print("Error tarea no encontrada")
    elif num_accion == "5":
        break
    else:
        print("Error: orden no existente en el asistente")
        # cambios para git
