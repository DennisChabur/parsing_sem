'''
Выполнить скрейпинг данных в веб-сайта http://books.toscrape.com/ и извлечь информацию о всех книгах на сайте
во всех категориях: название, цену, количество товара в наличии (In stock (19 available)) в формате integer, описание.

Затем сохранить эту информацию в JSON-файле.
'''

import requests
from bs4 import BeautifulSoup
import urllib.parse
from datetime import datetime, time, timedelta
import time
import re
import json


# Запрос веб-страницы
url = 'https://books.toscrape.com/'
response = requests.get(url)#, headers={
#    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)
#    Chrome/110.0.0.0 Safari/537.36'})

# Парсинг HTML-содержимого веб-страницы с помощью Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

try_ = soup.find_all('li')

# print(try_)

# Get links for each book
release_links = []
for link in soup.find_all('li', ('class', 'col-xs-6 col-sm-4 col-md-3 col-lg-3')):
    release_links.append(url + link.find('a').get('href'))

print(len(release_links))
print(release_links)

try:
    book_info = {}
    book_info_list = []
    for link in release_links:
        response = requests.get(link)
        time.sleep(1)
        soup = BeautifulSoup(response.text, "html.parser")
        data = soup.find("div", class_="content")
        book_name = data.find("h1").text
        price = float(soup.find("p", class_="price_color").text[2:])
        description = soup.find("meta", attrs={"name": "description"})["content"].strip()
        stock = int(soup.find("p", class_="instock availability").text.split()[2][1:])
        book_url_img = "https://books.toscrape.com/" + data.find("img").get("src").replace("../", "")
        book_info = {"book_name": book_name, "price": price, "description": description, "stock": stock,
                 "book_url": link}
        book_info_list.append(book_info)
        print(book_info)
except Exception:
    print(f"Error: {str(Exception)}")


    # data.append(row_data)
    # time.sleep(10)

# сохранение данных в JSON-файл
with open('books_data.json', 'w') as f:
    json.dump(book_info_list, f)

