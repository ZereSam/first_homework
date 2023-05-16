import requests
import json


response = requests.get("https://jsonplaceholder.typicode.com/todos")

if response.status_code == 200:
    data = response.json()

    with open("data.json", "w") as file:
        json.dump(data, file)

    # Или сохранение данных в переменную
    # data_variable = json.dumps(data)

    print("Данные успешно сохранены в JSON-файл.")
else:
    print("Ошибка при выполнении запроса.")
