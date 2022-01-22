import requests
from googletrans import Translator

city_name =input('Ведите страна:')

API_key ='e4a9be217376696da220bd8bd54f4be8'
API_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={API_key}'
res=requests.get(API_url)
json_data=res.json()

transletor=Translator()
# a=transletor.translate(status_sky,dest='ky').text
# print(status_sky)
# print(a,'аба ырайы')
# city_name=input('введите город')

# text=input('выберите язык:')

# if text=='ky':
    # print(tra/nsletor.translate(status_sky,dest='ky').text)
# elif text=='ru':
#     print(transletor.translate(status_sky,dest='ru').text)
# elif text=='en':
#     print(transletor.translate(status_sky,dest='en').text)
# elif text=='korean':
#     print(transletor.translate(status_sky,dest='korean').text)

weat=input('1.Кыргызча\n2.Русский\n3.English\n4.Казакша\n5.Turkish\n6.korean \nВыберите язык:')
if weat=='ky':
    print(transletor.translate(f"\nтемпература ,{json_data['main']['temp']}\nмин температура', {json_data['main']['temp_min']},\nОщущается как',{json_data['main']['feels_like']}, \nПогода: {json_data['weather'][0]['main']}", dest='ky').text)
elif weat=='ru':
      print(transletor.translate(f"\nтемпература ,{json_data['main']['temp']}\nмин температура', {json_data['main']['temp_min']},\nОщущается как',{json_data['main']['feels_like']}, \nПогода: {json_data['weather'][0]['main']}", dest='ru').text)

elif weat=='turkish':
     print(transletor.translate(f"\nтемпература ,{json_data['main']['temp']}\nмин температура', {json_data['main']['temp_min']},\nОщущается как',{json_data['main']['feels_like']}, \nПогода: {json_data['weather'][0]['main']}", dest='turkish').text)

elif weat=='kazakh':
    print(transletor.translate(f"\nтемпература ,{json_data['main']['temp']}\nмин температура', {json_data['main']['temp_min']},\nОщущается как',{json_data['main']['feels_like']}, \nПогода: {json_data['weather'][0]['main']}", dest='kazakh').text)

elif weat=='en':
    
 print(transletor.translate(f"\nтемпература ,{json_data['main']['temp']}\nмин температура', {json_data['main']['temp_min']},\nОщущается как',{json_data['main']['feels_like']}, \nПогода: {json_data['weather'][0]['main']}", dest='en').text)


elif weat=='korean':
    
 print(transletor.translate(f"\nтемпература ,{json_data['main']['temp']}\nмин температура', {json_data['main']['temp_min']},\nОщущается как',{json_data['main']['feels_like']}, \nПогода: {json_data['weather'][0]['main']}", dest='korean').text)