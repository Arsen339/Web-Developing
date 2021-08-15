# считаем с сайта нужную информацию
import requests
from bs4 import BeautifulSoup
# используем библиотеку для парсинга beautiful soup
response = requests.get("https://yandex.ru/")

# перепарсим курс валют
if response.status_code == 200:
    html_doc = BeautifulSoup(response.text, features="html.parser")
    list_of_values = html_doc.find_all('span', {"class": "inline-stocks__value_inner"})
    list_of_names = html_doc.find_all('a', {'class': 'home-link home-link_black_yes inline-stocks__link'})

    for names, values in zip(list_of_names, list_of_values):
        print(names.text, values.text)

if list_of_values:
    dollars_amount = input("Input the amount of dollars ")
    dollars_amount = float(dollars_amount)
    res = []

    for names, values in zip(list_of_names, list_of_values):
        if names.text == "USD":
            for sign in values.text:
                if sign == ",":
                    res.append('.')
                else:
                    res.append(sign)

    str_res = ''
    str_res = ''.join(res)
    print(f"You have {float(str_res) * dollars_amount} rubles ")
else:
    print("На сайте обновление, дождитесь заверщения")
