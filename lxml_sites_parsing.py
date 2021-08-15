import lxml.html
import requests
# XPath - мощный интсрумент по навигации по HTML страницам
# получаем html-документ
time_response = requests.get('https://www.utctime.net/')
# преобразуем его в дерево
html_tree = lxml.html.document_fromstring(time_response.text)
# вытаскиваем нужное по шаблону
list_of_matches = html_tree.xpath("//*[@id='time']")
print(f"Время по UTC: {list_of_matches[0].text}")
