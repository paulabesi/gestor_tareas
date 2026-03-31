"""API"""
import requests
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
