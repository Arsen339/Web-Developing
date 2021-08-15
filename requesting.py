# команда ping "url" проверяет подключение к интернету
import requests

# пройдем идентификацию на сайте
response = requests.get('https://httpbin.org/basic-auth/user/password', auth=('user', 'password'))
print(f"Тело ответа {response.content}")
print(f"Код состояния {response.status_code}")

print(f"Тело ответа в байтах {response.content}")
print(f"Тело ответа в str    {response.text}")
print(f"Тело ответа в json    {response.json()}")

print("Отправим заголовок")
headers = {'Skillbox': '16 module'}
response_with_headers = requests.get('http://httpbin.org/get', headers=headers)
print(f"Ответ сервера, включающий и передающий нам заголовки{response_with_headers.text}")
print("Пост-запрос(запрос, содержащий тело, возвращена форма")

payload = {"key1": "value1", "key2": "value2"}
response_with_data = requests.post("http://httpbin.org/post", data=payload)
print(f"Ответ сервера, включающий наши данные: {response_with_data.text}")
print(f"Заголовки ответа: {response_with_data.headers}")

# редиректы
response_with_redirect = requests.get("https://gitlab.skillbox.ru/learning_materials?python_base", allow_redirects=True)
print(f"В результате мы оказались на {response_with_redirect.url}")
print(f"Итоговый код состояния {response_with_redirect.status_code}")
print(f"история редиректов: {response_with_redirect.history}")

# таймаут
try:
    response_with_time = requests.get("https://gitlab.skillbox.ru", timeout=1)
except requests.exceptions.Timeout:
    print("Out of time")

print(response.request.headers)