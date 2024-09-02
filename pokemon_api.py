import requests

def get_all_pokemon():
    response = requests.get('https://pokeapi.co/api/v2/pokemon')
    return response.json()

def get_pokemon(name):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro {response.status_code}: {response.text}")
        return None

all_pokemon = get_all_pokemon()
print("Todos os Pokémon (primeiros 5):")
print(all_pokemon['results'][:5])  

pokemon = get_pokemon('pikachu')
if pokemon:
    print("\nInformações sobre Pikachu:")
    print(pokemon)
