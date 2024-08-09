'''
Задание 1
Напишите сценарий на языке Python, который выполняет следующие задачи:

- отправляет HTTP GET-запрос на целевой URL и получает содержимое веб-страницы.
- выполняет парсинг HTML-содержимого ответа с помощью библиотеки lxml.
- используя выражения XPath, извлеките данные из первой строки таблицы.
- выведите извлеченные данные из первой строки таблицы в консоль.
'''

import requests
from lxml import html
import pandas as pd

url = 'https://worldathletics.org/records/toplists/sprints/60-metres/indoor/women/senior/2023?page=1'

response = requests.get(url, headers={
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/108.0.0.0 Safari/537.36'})

# https://pypi.org/project/fake-useragent/ -- библиотека для разных user-agents

tree = html.fromstring(response.content)

#print(tree)

table_rows = tree.xpath("//table[@class='records-table']/tbody/tr")
#columns = table_rows[0].xpath(".//td/text()")
col_names = tree.xpath("//table[@class='records-table']/thead/tr/th/text()")
list_data = []
for row in table_rows:
    columns = row.xpath(".//td/text()")
    print(columns)
    # list_data.append({
    #     'rank': columns[0].strip(),
    #     'mark': columns[1].strip(),
    #     'wind': columns[2].strip(),
    #     'competitor': row.xpath(".//td[4]/a/text()")[0].strip(),
    #     'dob': columns[5].strip(),
    #     'nat': columns[7].strip(),
    #     'pos': columns[8].strip(),
    #     'venue': columns[9].strip(),
    #     'date': columns[10].strip(),
    #     'result_score': columns[11].strip()
    # })
#print(list_data)

# df = pd.DataFrame(list_data)

# print(df)