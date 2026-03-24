"""main"""
from storage import cargar_tareas, guardar_tareas
from models import Tarea, GestorTareas

gestor = GestorTareas()

try:
    for tarea in cargar_tareas():
        gestor.lista_tareas.append(tarea)
    if gestor.lista_tareas:
        gestor.contador = max(tarea.id for tarea in gestor.lista_tareas)
except FileNotFoundError:
    pass
while True:
    num_accion = input(
        "Escoja lo que quiere hacer:\n1. Crear tarea\n2. Listar tareas\n3. Marcar tarea como completada\n4. Eliminar tarea\n5. Salir\n")
    if num_accion == "1":
        titulo = input("Escriba el titulo de la tarea\n")
        descripcion = input("Escriba la descripcion\n")
        completada = (
            input("Escriba True si esta completa o False si no lo esta\n")) == "True"
        tarea_creada = Tarea(0, titulo, descripcion, completada)
        gestor.añadir_tarea(tarea_creada)
    elif num_accion == "2":
        gestor.imprime_lista()
    elif num_accion == "3":
        try:
            num_tarea_completada = int(
                input("Escriba la id de la tarea que desea marcar como completada \n"))
        except ValueError:
            print("Error debes escribir un numero")
            continue
        tarea = gestor.buscar_por_id(num_tarea_completada)
        if tarea:
            tarea.marcar_completada()
        else:
            print("Error:Tarea no existente")
    elif num_accion == "4":
        try:
            num_id_eliminar = int(
                input("Escriba el id de la tarea que quiere eliminar:\n"))
        except ValueError:
            print("Error debes ecribir un numero")
            continue
        gestor.eliminar_tarea(num_id_eliminar)
    elif num_accion == "5":
        guardar_tareas(gestor)
        break
    else:
        print("Error: orden no existente en el asistente")
