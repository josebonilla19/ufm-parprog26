# PARTE 1
import requests

nombre_pokemon = "pikachu"
url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon}"

# PARTE 2
respuesta = requests.get(url)

print("Status code:", respuesta.status_code)

if respuesta.status_code == 200:
    datos = respuesta.json()
    print("Nombre:", datos["name"])
    print("Altura:", datos["height"])
    print("Peso:", datos["weight"])
else:
    print("Algo salió mal al consultar la API")

