import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import datetime
import os.path

URL_TEMPLATE = "https://lenta.ru/parts/news/"
FILE_NAME = "test.txt"


def parse(url=URL_TEMPLATE):
    r = requests.get(url)
    soup = bs(r.text, "html.parser")
    news_collections = soup.find_all('a', class_='card-full-news _parts-news')
    result_list = {'Новости и дата публикации': []}
    now = datetime.date.today()

    for element in news_collections:
        elem = element.h3
        div_elem = element.div
        time_news = div_elem.time.text
        if time_news.find(',') == -1:
            time_news = time_news + ' ' + str(now)
            news_str = elem.text + ' ' + time_news
            result_list['Новости и дата публикации'].append(news_str)

    return result_list

df = pd.DataFrame(data=parse(URL_TEMPLATE))
# if os.path.exists(FILE_NAME):
#     old_df = pd.read_csv(FILE_NAME)
#     new_df = pd.concat([old_df, df])
#     new_df.drop_duplicates(subset='', keep='first')
#     new_df.to_csv(FILE_NAME, mode='a', header=False)
#
# else:
df.to_csv(FILE_NAME, header=False)
# pd.read_csv('C:/Users/123/PycharmProjects/news_parser/test.txt', 'w', header=None, skiprows=[0])
# pd.read_csv(r'C:/Users/123/PycharmProjects/news_parser/test.csv', header=None, skiprows=[0])

# parse(URL_TEMPLATE)
