import requests


city_name ="Ташкент"

if  city_name =='Ош':
   
    print('Температура в оше')



API_key ='e4a9be217376696da220bd8bd54f4be8'
API_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={API_key}'
response=requests.get(API_url)
print(response)
json_data=response.json()
print(type(json_data))
print(json_data['weather'])
print(json_data['main'])
print(json_data['main']['temp'])
input('Температура в оше ощ-ся как')

print(' температура', json_data['main']['temp'])
print('min температура', json_data['main']['temp_min'])
print('Максимальная температура', json_data['main']['temp_max'])

status_sky=json_data['weather'][0]['main']
print(status_sky)
temp=json_data['clouds']
my_dict={'temp':'температура','rain':'дождь','wind':'ветер','snow':'снежное',
'clear':'чисьое'}


# if status_sky.lower() in my_dict:
#     print('Состояние:',my_dict[status_sky.lower()])
# else:
#     print('Состояние:',status_sky)
