"""
Chat por terminal usando la API de Gemini.

Gemini requiere autenticacion (a diferencia de otras APIs abiertas como
PokeAPI). Para obtener una key gratuita (no pide tarjeta):

1. Entrar a https://aistudio.google.com
2. Iniciar sesion con una cuenta de Google
3. Click en "Get API key" y copiar la key generada

Docs oficiales: https://ai.google.dev/gemini-api/docs
"""

from api_key import API_KEY
import requests

MOSTRAR_DEBUG = False
NOMBRE_MODELO = "gemini-3.6-flash"
ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/{NOMBRE_MODELO}:generateContent"

if MOSTRAR_DEBUG:
    print("\n========================")
    print(f"Modelo en uso: {NOMBRE_MODELO}")
    print(f"Key cargada: {API_KEY}")
    print("========================")

# La key va en un header, no en la URL (Gemini no acepta credenciales
# como query param)
encabezados = {
    "Content-Type": "application/json",
    "x-goog-api-key": API_KEY,
}

# Ciclo principal: pide un prompt, lo manda a Gemini y muestra la respuesta,
# hasta que el usuario escriba "salir"
while True:
    print("\n=========== GEMINI AI =============")

    prompt_usuario = input("En que piensas? (escribe tu prompt o 'salir' para terminar): ")

    if prompt_usuario.strip().lower() == "salir":
        print("\nHasta luego!")
        break

    cuerpo_peticion = {
        "contents": [
            {
                "parts": [
                    {"text": prompt_usuario}
                ]
            }
        ]
    }

    respuesta = requests.post(ENDPOINT, headers=encabezados, json=cuerpo_peticion)

    if MOSTRAR_DEBUG:
        print("Status code:", respuesta.status_code)

    if respuesta.status_code != 200:
        print("Algo salio mal:")
        print(respuesta.text)
    else:
        datos = respuesta.json()
        # Estructura de la respuesta:
        # datos -> candidates -> [0] -> content -> parts -> [0] -> text
        texto_respuesta = datos["candidates"][0]["content"]["parts"][0]["text"]
        print("\nRespuesta de Gemini:\n")
        print(texto_respuesta)
