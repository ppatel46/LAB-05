import sys
from pastebin_api import create_paste
from poke_api import get_pokemon_info

def get_pokemon_name():
    """
    Get the Pokémon name from the command line parameters.
    
    Returns:
        str: Pokémon name input as a command line parameter
    """
    if len(sys.argv) < 2:
        print("Error: No Pokémon name provided.")
        sys.exit(1)
    return sys.argv[1]

def construct_paste_content(pokemon_info):
    """
    Construct the title and body text for the new paste.
    
    Parameters:
        pokemon_info (dict): Dictionary of Pokémon information
    
    Returns:
        tuple: (title, body text) where title is the paste title and body text is the paste body
    """
    name = pokemon_info['name'].capitalize()
    abilities = [ability['ability']['name'] for ability in pokemon_info['abilities']]
    title = f"{name}'s Abilities"
    body = "\n".join(f"- {ability}" for ability in abilities)
    return title, body

def main():
    """
    Main function to fetch Pokémon information and create a new PasteBin paste.
    """
    pokemon_name = get_pokemon_name()
    print(f"Getting information for {pokemon_name}...", end="")
    pokemon_info = get_pokemon_info(pokemon_name)
    
    if pokemon_info:
        print("success")
        title, body = construct_paste_content(pokemon_info)
        print("Posting new paste to PasteBin...", end="")
        paste_url = create_paste(title, body, '1M', False)
        if paste_url:
            print("success")
            print(paste_url)
        else:
            print("failure")
    else:
        print("failure")

if __name__ == '__main__':
    main()
