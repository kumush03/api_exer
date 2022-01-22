from urllib import request
import requests

# url ="https://oc.kg/"

# res = requests.get(url)
# print(res)
# print(res.text)
# print(res.status_code)
# print(res.content)
# print(res.headers)

# print("Статуса кода:",res.status_code)
# print("Тип запроса:",res.request)
# print("Тип запроса:",res.request.method)
# print("URL сайта:",res.url)
# print("Тип кодировки(юнткод):",res.encoding)
# print("Контент сайта:",res.content)
# print(res.links)
# print(type(res.links))
# print(res.text)


# a=input("Вставьте ссылку сайта:")
# response=requests.get(a)
# a2=input("Введите название сайта:")+'.html'
# print(a2)
# my_file=open(a2,"x")
# print(my_file)

# my_file.write(response.text)
# print(response.status_code)






# a2=input("Введите название сайта:")
# a3=input("Введите название файла:")+'.html'
# print(a2)
# res=requests.get(a2)
# if res.status_code == 200:
    
#     my_file=open(a3,"x")
#     my_file2=open(a3,"a")
#     my_file2.write(res.text)
#     my_file2.close()
    
#     print("вы успешно создали файл")
# elif res.status_code == 404:
#     print('вы ввели неправильный путь')





b=str(input("Ведите название сайта"))
# print(b)

try:
    res=requests.get(b)
    b2=res.text
    b3=res.status_code
    if b3==404:
        print('вы ввели неправильный путь')
    elif b3==200:
        b4=b.split('.')[1]
        b5=open(f'{b4}.html',"x")
        b5.write(b2)
        b5=open(f'{b4}.html',"r")
        print(b5.read())
except FileExistsError:
    print('Такой файл уже  существует')       




# c=str(input("введите названия сайта"))
# print(c)
# try:
#     res=requests.get(c)
#     c2=res.text
#     c3=res.status_code
#     if c3==404:
#         print("это не правильно")
#     elif c3==200:
#         c4=c.split('.')
#         c5=open(f'{c4}.html',"x")
#         c5.write(f'{c2}.html',"r")
# except FileExistsError:
#     print('такой файл уже сущестует')

    




# import requests
# url="http://www.nurcinema.kg/"
# response=requests.get(url)
# print(response.text)

# html_name=input('Введите название файла:')+'.html'
html_name="html_file2.splitlines"
html_file=open(html_name,'x')
# html_file2=open(html_name,'w')
# html_file2.write(response.text)
# html_file2.close()
# html_file.close()

# lines=0
# for line in open(html_name):
#     lines += 1
# print(lines)


# lines=0
# for i in open(html_name):
#     if "<button"in i:
#         lines += 1
    

# print(lines)

btns=0
for i in open(html_name):
    if "<img" in i:
        btns += 1
    

print(btns)



