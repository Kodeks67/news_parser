import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import datetime

URL_TEMPLATE = "https://lenta.ru/parts/news/"
FILE_NAME = "test.csv"


def parse(url=URL_TEMPLATE):
    r = requests.get(url)
    soup = bs(r.text, "html.parser")
    news_collections = soup.find_all('a', class_='card-full-news _parts-news')
    result_list = []
    now = datetime.date.today()

    for element in news_collections:
        elem = element.h3
        div_elem = element.div
        time_news = div_elem.time.text
        if time_news.find(',') == -1:
            time_news = time_news + ' ' + str(now)
            news_str = elem.text + ' ' + time_news
            result_list.append(news_str)

    print(result_list)

df = pd.DataFrame(data=parse())
df.to_csv(FILE_NAME)

parse(URL_TEMPLATE)
