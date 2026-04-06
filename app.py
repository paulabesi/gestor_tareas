"""flask"""
from flask import Flask, jsonify, request
from db import crear_tabla, crear_tarea, obtener_tareas, marcar_completada, eliminar_tarea, obtener_tarea_por_id, actualizar_tarea
crear_tabla()
app = Flask(__name__)


@app.route("/")
def inicio():
    return "Hola mundo desde mi API"


@app.route("/tareas", methods=["GET"])
def funcion_tareas():
    tareas = obtener_tareas()
    resultado = []
    for cosas in tareas:
        resultado.append(
            {"id": cosas[0], "titulo": cosas[1], "descripcion": cosas[2], "completada": bool(cosas[3])})
    return jsonify(resultado)


@app.route("/tareas", methods=["POST"])
def cosas():
    datos = request.get_json()
    crear_tarea(datos["titulo"], datos["descripcion"], datos["completada"])
    return jsonify({"mensaje": "Tarea creada correctamente"})


@app.route("/tareas/<id>", methods=["DELETE"])
def borrar_cosas(id):
    eliminar_tarea(id)
    return jsonify({"mensaje": "Tarea borrada correctamente"})


@app.route("/tareas/<id>", methods=["PUT"])
def editar_tarea(id):
    tarea = request.get_json()
    actualizar_tarea(
        id, tarea["titulo"], tarea["descripcion"], tarea["completada"])
    tarea_final = obtener_tarea_por_id(id)
    final = {"id": tarea_final[0], "titulo": tarea_final[1],
             "descripcion": tarea_final[2], "completada": bool(tarea_final[3])}
    return jsonify(final)


if __name__ == "__main__":
    app.run(debug=True)
