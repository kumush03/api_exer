import requests
# from googletrans import Translator
country=input('название страны:')
url=f"https://covid-api.mmediagroup.fr/v1/cases?country={country}"
res=requests.get(url)
# print(res)
# print(res.text)
json_data=res.json()

# input('Название страна')
# print('Умерли:',json_data['All']['deaths'])
# print('Население:',json_data['All']['population'])
# print('Площадь;',json_data['All']['sq_km_area'])
# print('Продолжительность жизни:',json_data['All']['life_expectancy'])
# print('Потвеждено:',json_data['All']['confirmed'])

a=(input('Название города'))

print('Потверждено',json_data[f'{a}']['confirmed'])

print('Умерли:',json_data[f'{a}']['deaths'])
print('Выздоровели:',json_data[f'{a}']['recovered'])
