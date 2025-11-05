import requests

# Список первых 20 покемонов
response = requests.get("https://pokeapi.co/api/v2/pokemon")
data = response.json()
pokemons = [p['name'] for p in data['results']]

print("Список первых 20 покемонов:")
print(pokemons[:21])

# Получаем имя покемона через input()
pokemon_name = input("Имя покемона: ").lower()

# Получаем информацию об этом покемоне
url_detail = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
response_detail = requests.get(url_detail)
if response_detail.status_code == 200:
    pokemon_response = response_detail.json()
    # Имя
    name = pokemon_response['name']
    # Типы
    types = [i['type']['name'] for i in pokemon_response['types']]
    # Вес
    weight = pokemon_response['weight']
    # Рост
    height = pokemon_response['height']
    # Cпособности
    abilities = [a['ability']['name'] for a in pokemon_response['abilities']]

    print("Имя:", name)
    print("Тип:", ", ".join(types))
    print("Вес:", weight)
    print("Рост:", height)
    print("Способности:", ", ".join(abilities))
else:
    print("Ошибка")
