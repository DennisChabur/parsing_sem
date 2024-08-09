'''
- Установите пакет PyMongo и импортируйте MongoClient и json.
- Установите Compass MongoDB
- Подключитесь к серверу MongoDB по адресу 'mongodb://localhost:27017/'.
- Создайте базу данных 'town_cary' и коллекцию 'crashes'.
- Выполните чтение файла JSON 'crash-data.json'.
- Напишите функцию chunk_data, которая принимает два аргумента: список данных и размер фрагмента.
Функция должна разделить данные на более мелкие фрагменты указанного размера и вернуть генератор.
- Разделите данные JSON на фрагменты по 5000 записей в каждом.
- Переберите все фрагменты и вставьте каждый фрагмент в коллекцию MongoDB с помощью функции insert_many().
- Выведите финальное сообщение, указывающее на то, что данные были успешно вставлены.
'''

import json
from pymongo import MongoClient

# подключение к серверу MangoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['town_cary'] # выбор бзд

collection = db['crashes']

with open('crash-data.json', 'r') as file:
    data = json.load(file)

# извлечение данных из ключа features
data = data['features']

def changdata(data, changsize):
    for i in range(0, len(data), changsize):
        yield data[i:i + changsize]

changsize = 5000

data_chang = list(changdata(data, changsize))

for chang in data_chang:
    collection.insert_many(chang)