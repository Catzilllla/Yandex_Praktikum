import requests
from pprint import pprint

resp = requests.get('https://swapi.dev/api/planets/1/')
name_planet = resp.json().get('name')
diam_planet = resp.json().get('diameter')
print(f'Планета: {name_planet}')
print(f'Диаметр {name_planet}: {diam_planet}')
print('Общая информация о планете: ')
pprint(resp.json())
