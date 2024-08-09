'''
Выберите веб-сайт с табличными данными, который вас интересует.
Напишите код Python, использующий библиотеку requests для отправки HTTP GET-запроса на сайт и получения HTML-содержимого страницы.
Выполните парсинг содержимого HTML с помощью библиотеки lxml, чтобы извлечь данные из таблицы.
Сохраните извлеченные данные в CSV-файл с помощью модуля csv.

Ваш код должен включать следующее:

Строку агента пользователя в заголовке HTTP-запроса, чтобы имитировать веб-браузер и избежать блокировки сервером.
Выражения XPath для выбора элементов данных таблицы и извлечения их содержимого.
Обработка ошибок для случаев, когда данные не имеют ожидаемого формата.
Комментарии для объяснения цели и логики кода.

Примечание: Пожалуйста, не забывайте соблюдать этические и юридические нормы при веб-скреппинге.
'''

import requests
from lxml import html
import pandas as pd
import time

#pd.set_option('display.max_columns', None)

url = 'https://finance.yahoo.com/trending-tickers/?guccounter=1'
response = requests.get(url, headers={
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/127.0.0.0 Safari/537.36'})

tree = html.fromstring(response.content)

table_rows = tree.xpath("//table[@class='W(100%)']/tbody/tr")
col_names = tree.xpath("//table[@class='W(100%)']/thead/tr/th/text()")

list_data = []

#print(tree.xpath('//*[@id="list-res-table"]/div[1]/table/tbody/tr/td/fin-streamer/text()'))
#//*[@id="list-res-table"]/div[1]/table/tbody/tr[1]/td[1]/a
#//*[@id="list-res-table"]/div[1]/table/tbody/tr[1]/td[2]
#//*[@id="list-res-table"]/div[1]/table/tbody/tr[1]/td[5]/fin-streamer/span
for row in table_rows:
    columns_0 = ''.join(row.xpath(".//td/a/text()"))
    columns_1 = ''.join(row.xpath(".//td/text()"))
    columns_2_3_6_7 = row.xpath(".//td/fin-streamer/text()")
    columns_4_5 = row.xpath(".//td/fin-streamer/span/text()")

    list_data.append({
        col_names[0]: columns_0.strip(),
        col_names[1]: columns_1.strip(),
        col_names[2]: ''.join(columns_2_3_6_7[0]).strip(),
        col_names[3]: ''.join(columns_2_3_6_7[1]).strip(),
        col_names[4]: ''.join(columns_4_5[0]).strip(),
        col_names[5]: ''.join(columns_4_5[1]).strip(),
        col_names[6]: ''.join(columns_2_3_6_7[2]).strip(),
        col_names[7]: ''.join(columns_2_3_6_7[3]).strip()
    })
    time.sleep(1)
df = pd.DataFrame(list_data)

print(df)

df.to_csv("trending_stickers.csv")