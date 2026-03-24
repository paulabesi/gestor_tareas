"""json"""
import json
from models import Tarea, GestorTareas


def guardar_tareas(gestor):
    lista = []
    for tarea in gestor.lista_tareas:
        lista.append(tarea.to_dict())
    with open("tareas.json", "w") as archivo:
        json.dump(lista, archivo)


def cargar_tareas():
    with open("tareas.json", "r") as archivo:
        lista_diccionarios = json.load(archivo)
    # lista_tareas = []
    return [Tarea.from_dict(diccionario) for diccionario in lista_diccionarios]
    """for diccionario in lista_diccionarios:
        lista_tareas.append(Tarea.from_dict(diccionario)) + este y el de arriba hacen lo mismo, el primero es mas
    return lista_tareas"""
# no se que pasa
