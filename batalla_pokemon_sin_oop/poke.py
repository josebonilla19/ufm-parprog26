'''
Poke.py sin clasess
'''


# Crear un pokemon en vez del __init__
def crear_pokemon(nombre, tipo, hp, ad):
    pokemon = {
        'nombre': nombre.capitalize(),
        'tipo': tipo,
        'hp': hp,
        'ad': ad
    }
    return pokemon


# Restarle vida a un pokemon 
def recibir_dano(pokemon, hp_perdido):
    pokemon['hp'] = pokemon['hp'] - hp_perdido


# Un pokemon ataca a otro 
def atacar(atacante, rival):

    if atacante['tipo'] == 'electrico':
        ataque = 'Impactrueno'
    elif atacante['tipo'] == 'planta':
        ataque = 'Hoja navaja'
    elif atacante['tipo'] == 'fuego':
        ataque = 'Llamarada'
    else:
        ataque = 'Cañon de agua'

    recibir_dano(rival, atacante['ad'])

    print(f"\n({atacante['nombre']}) Ataca con {ataque} | -{atacante['ad']}")