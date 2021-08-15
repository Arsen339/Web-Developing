import requests
from bs4 import BeautifulSoup

response = requests.get("https://yandex.ru/pogoda/54?utm_source=serp&utm_campaign=wizard&utm_medium=desktop&utm_content=wizard_desktop_main&utm_term=url")

if response.status_code == 200:
    html_doc = BeautifulSoup(response.text, features="html.parser")
    # list_of_values = html_doc.find_all('div', {"class": "js_meas_container temperature"})
    list_of_values = html_doc.find_all('span', {"class": "temp__value temp__value_with-unit"})
    list_of_pressures = html_doc.find_all('div', {"class": "term__value"})


print(f"Текущая температура: {list_of_values[1].text}")
print(f"Текущее давление {list_of_pressures[4].text}")