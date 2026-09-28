types = {
    "Electric": ["Pikachu"],
    "Grass": ["Bulbasaur", "Leafeon", "Scovillain"],
    "Fire": ["Charmander", "Scovillain"],
}

# Way 1: a loop over each key/value pair
for pokemon_type, pokemons in types.items():
    if "Pikachu" in pokemons:
        print(pokemon_type)

# Way 2: a list comprehension
print([pokemon_type for pokemon_type in types if "Pikachu" in types[pokemon_type]])
