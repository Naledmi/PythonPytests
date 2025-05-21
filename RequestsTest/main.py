import requests 

url = 'https://api.pokemonbattle.ru/v2'
token = 'a35b1ff8ac6e9ae2622cb59410a8cbf9'
Header = {'Content-Type' : 'application/json', 'trainer_token' : token}

body_newPokemon = {
    "name": "Ропи",
    "photo_id": 39
}

body_reName = {
    "pokemon_id": "320168",
    "name": "Попи",
    "photo_id": 39
}

body_pokeball = {
    "pokemon_id": "320168"
}

response = requests.post(url = f'{url}/pokemons', headers = Header, json = body_newPokemon)
print(response.text) 

response_reName = requests.put(url = f'{url}/pokemons', headers = Header, json = body_reName)
print(response_reName.text)

response_addPokeball = requests.post(url = f'{url}/trainers/add_pokeball', headers = Header, json = body_pokeball)
print(response_addPokeball.text) 