import requests

def get_pokemon_info(name_or_id):
    """
    Fetch information for a specified Pokémon from the PokéAPI.
    
    Parameters:
        name_or_id (str/int): Name or PokéDex number of the Pokémon
    
    Returns:
        dict: Pokémon information if fetched successfully, None otherwise
    """
    pokeapi_url = f"https://pokeapi.co/api/v2/pokemon/{name_or_id}"
    response = requests.get(pokeapi_url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# Test function (you can remove or comment this part for final submission)
if __name__ == '__main__':
    pokemon = get_pokemon_info("pikachu")
    if pokemon:
        print(pokemon)
    else:
        print("Failed to fetch Pokémon info.")
