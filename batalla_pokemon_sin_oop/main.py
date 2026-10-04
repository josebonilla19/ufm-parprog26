'''
Simulación de batalla pokemon
'''


from random import choice
from time import sleep
from poke import crear_pokemon, atacar


# Utils
def waiting():
    print('\n...')
    sleep(0.5)


# Crear 4 pokemon de inventario
pikachu = crear_pokemon('pikachu', 'electrico', 60, 15)
chikorita = crear_pokemon('chikorita', 'planta', 45, 10)
charmander = crear_pokemon('charmander', 'fuego', 40, 10)
froakie = crear_pokemon('froakie', 'agua', 40, 20)


# Seleccionar 2 pokemon para batalla
pokemon_es = [pikachu, chikorita, charmander, froakie]

poke_1 = choice(pokemon_es)
poke_2 = choice(pokemon_es)

print('\n ------ POKEMON SELECCIONADOS ------')

waiting()
print(f"\nPokemon 1: {poke_1['nombre']} (HP: {poke_1['hp']} | AD: {poke_1['ad']})")
print(f"Pokemon 2: {poke_2['nombre']} (HP: {poke_2['hp']} | AD: {poke_2['ad']})")

# Manejo de turnos (ciclo con ambos turnos hasta que uno pierda)
while True:

    # Turno poke_1
    waiting()
    atacar(poke_1, poke_2)

    # Verificar si poke_2 perdió
    if poke_2['hp'] <= 0:
        print(f"\nGAME OVER: {poke_1['nombre']} venció a {poke_2['nombre']}")
        break

    # Turno poke_2
    waiting()
    atacar(poke_2, poke_1)

    # Verificar si poke_1 perdió
    if poke_1['hp'] <= 0:
        print(f"\nGAME OVER: {poke_2['nombre']} venció a {poke_1['nombre']}")
        break

    # Imprimir vidas restantes
    waiting()
    print('\nHPs restantes')
    print(f"{poke_1['nombre']}: {poke_1['hp']}")
    print(f"{poke_2['nombre']}: {poke_2['hp']}")