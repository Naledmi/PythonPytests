import requests
import pytest

url = 'https://api.pokemonbattle.ru/v2'
token = 'a35b1ff8ac6e9ae2622cb59410a8cbf9'
Header = {'Content-Type' : 'application/json', 'trainer_token' : token}
trainer_id = '33821'


def test_status_trainers():
    response = requests.get(url = f'{url}/trainers', headers = Header, params = {'trainer_id' : trainer_id})
    assert response.status_code == 200

def test_status_name():
    response_name = requests.get(url = f'{url}/trainers', headers = Header, params = {'trainer_id' : trainer_id})
    assert response_name.json()['data'][0]['trainer_name'] == 'Evavilina'
