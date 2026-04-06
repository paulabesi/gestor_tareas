"""flask"""
from flask import Flask, jsonify
app = Flask(__name__)


@app.route("/")
def inicio():
    return "Hola mundo desde mi API"


@app.route("/tareas")
def obtener_tareas():
    tareas = [
        {"id": 1, "titulo": "Guitarra", "completada": False},
        {"id": 2, "titulo": "Estudiar", "completada": True},
    ]
    return jsonify(tareas)


if __name__ == "__main__":
    app.run(debug=True)
