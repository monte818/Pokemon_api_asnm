import requests 

def get_pokemon_data(pokemon_name):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        abilities = [ability['ability']['name'] for ability in data['abilities']]
        weight = data['weight']

        return {'abilities': abilities, 'weight': weight}
    else:
        print(f"That Pokemon is not here :) {pokemon_name}")
        return None

def poke_dict(pokemon_names):
    pokemon_dict = {}

    for pokemon in pokemon_names:
        data = get_pokemon_data(pokemon)
        if data:
            pokemon_dict[pokemon.lower()] = data

    return pokemon_dict

def organizeType(pokemon_dict):
    organized_dict = {}

    for pokemon, data in pokemon_dict.items():
        types = pokemon_type(pokemon)
        for type_name in types:
            if type_name not in organized_dict:
                organized_dict[type_name] = {}
            organized_dict[type_name][pokemon] = data
        
    return organized_dict

def pokemon_type(pokemon_name):
    
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        types = [type['type']['name'] for type in data['types']]
        return types
    else:
        print(f"Couldnt find {pokemon_name}")
        return []
    
def printNeat(name_values):
    for pokemon_type, data in name_values.items():
        print(f"{pokemon_type}:")
        for pokemon, stats in data.items():
            print(f"  {pokemon}: {stats}")
        print()


if __name__ == "__main__":
    pokemon_names = ['Charizard', 'Pikachu', 'Squirtle', 'Bulbasaur', 'Jigglypuff',
                     'Gyarados', 'Dragonite', 'Snorlax', 'Mewtwo', 'Mew',
                     'Venusaur', 'Blastoise', 'Butterfree']
    
pokemon_data = poke_dict(pokemon_names)

organized_data = organizeType(pokemon_data)

print(printNeat(organized_data))