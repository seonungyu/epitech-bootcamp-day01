types = {"Electric": [], "Grass": [], "Fire": []}
pokemon_types = {
    "Pikachu": ["Electric"],
    "Bulbasaur": ["Grass"],
    "Charmander": ["Fire"],
    "Leafeon": ["Grass"],
    "Scovillain": ["Grass", "Fire"],
}
for pokemon in ["Pikachu", "Bulbasaur", "Charmander", "Leafeon", "Scovillain"]:
    for pokemon_type in pokemon_types[pokemon]:
        types[pokemon_type].append(pokemon)
print(types)
