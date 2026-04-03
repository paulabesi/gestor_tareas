"""API"""
import requests
import os
try:
    respuesta = requests.get(
        "https://official-joke-api.appspot.com/random_joke")
    print(respuesta.status_code)
    print(respuesta.json())
    print(respuesta.json()["setup"])
    print(respuesta.json()["punchline"])
    respuesta_mala = requests.get(
        "https://official-joke-api.appspot.com/ruta_que_no_existe")
    print(respuesta_mala.status_code)
    respuesta_clima = requests.get(
        "https://wttr.in/Denia", params={"format": "j1"})
    datos = respuesta_clima.json()
    # print(datos)
    temperatura = datos["current_condition"][0]["temp_C"]
    desc_tiempo = datos["current_condition"][0]["weatherDesc"][0]["value"]
    humedad = datos["current_condition"][0]["humidity"]
    veloc_viento = datos["current_condition"][0]["windspeedKmph"]
    print(
        f"la temeperatura es de {temperatura} grados, el tiempo esta {desc_tiempo}, la humedad es de {humedad}, y el viento va a {veloc_viento}")
except requests.exceptions.RequestException:
    print("Error de conexion, comprueba tu internet")

with open("gestor_tareas/ejercicios/archivo.txt", "w") as archivo:
    archivo.write(
        f"la temperatura es de {temperatura} grados, el tiempo esta {desc_tiempo}, la humedad es de {humedad}, y el viento va a {veloc_viento}")
respuesta_post = requests.post(
    "https://httpbin.org/post",
    json={"nombre": "Paula", "ciudad": "Denia"}
)
print(respuesta_post.status_code)
print(respuesta_post.json())
headers = {"User-Agent": "MiApp/1.0", "Accept-Language": "es"}
respuesta_headers = requests.get(
    "https://httpbin.org/get",
    headers=headers
)
print(respuesta_headers.json()["headers"])


def hacer_peticion(url, params=None, headers=None):
    # aquí dentro haces la petición con try/except
    # y devuelves los datos o None si hay error
    try:
        respuesta = requests.get(url, params=params, headers=headers)
        return respuesta.json()
    except requests.exceptions.RequestException:
        print("error no se pudo conectar a la url")
        return None


datos = hacer_peticion("https://wttr.in/Denia", params={"format": "j1"})
if datos:
    print(datos["current_condition"][0]["temp_C"])
datos_perro = hacer_peticion("https://dog.ceo/api/breeds/image/random")
if datos_perro:
    print(datos_perro["message"])
