import argparse
import json
from bs4 import BeautifulSoup
import requests
import threading

"""

Парсинг приложений Google Play Market по ключевому слову 

"""

parser = argparse.ArgumentParser()
parser.add_argument('-k', '--keyword', type=str, help='Keyword. Example:"Сбер"', metavar='')
args = parser.parse_args()


class GooglePlayMarketParser:
    list_url_app = []
    dict_all_app = {}
    json_all_app = None

    def __init__(self, keyword_app):
        self.keyword = keyword_app

    @staticmethod
    def get_full_search_url(keyword):
        """

        Получаем url на приложение

        """
        search_url = ['https://play.google.com/store/search?q=', None, '&c=apps']
        low_keyword = keyword.lower()
        search_url[1] = low_keyword
        return search_url

    @staticmethod
    def get_html_obj(url):
        """

        Получаем объект html страницы

        """
        search_url = ''.join(url)
        response = requests.get(search_url)
        if response.status_code == 200:
            return BeautifulSoup(response.text, features='html.parser')

    @staticmethod
    def make_list_url_app(html_obj, list_url):
        """

        Наполняем список url из поиска

        """
        div_all = html_obj.find_all('div', {'class': 'mpg5gc'})
        for div in div_all:
            url = div.find('div', class_='wXUyZd').find('a', class_='poRVub').get('href')
            list_url.append(f'https://play.google.com{url}')

    def valid_app_name(self,app_name):
        """

        Проверка по названию

        """
        return self.keyword.lower() in app_name.lower()

    def get_app_detail(self, url_app):

        """
        Собираем всю необходимую информацию о приложении и пакуем в словарь

        """
        html_obj = self.get_html_obj(url=url_app)
        clear_name_app = html_obj.find('h1', class_='AHFaub').find('span').text
        if not self.valid_app_name(clear_name_app):
            return
        raw_author_category = html_obj.find_all('span', {'class': 'T32cc UAO9ie'})
        clear_author = raw_author_category[0].find('a').text
        clear_category = raw_author_category[1].find('a').text
        clear_description = html_obj.find('div', {'jsname': 'sngebd'}).text

        try:
            clear_rating = html_obj.find('div', class_='BHMmbe').text
            num_rating = html_obj.find('span', class_='AYi5wd TBRnV').text
            clear_num_rating = num_rating.replace(',', '')
        except AttributeError as exc:
            clear_num_rating = 'empty'
            clear_rating = 'empty'

        date_update = html_obj.find('span', class_='htlgb').text
        clear_date_update = date_update.replace(',', '')

        dict_all_descriprion = {
            "name_app": clear_name_app,
            "author": clear_author,
            "category": clear_category,
            "description": clear_description,
            "rating": clear_rating,
            "num_rating": clear_num_rating,
            "date_update": clear_date_update,
        }

        self.dict_all_app.update({clear_name_app: dict_all_descriprion})

    def run_scan(self):
        """
        Запускаем потоки по парсингу url

        """
        list_thread = []

        for url in self.list_url_app:
            thread = threading.Thread(target=self.get_app_detail, args=(url,))
            list_thread.append(thread)

        for thread in list_thread:
            thread.start()

        for thread in list_thread:
            thread.join()

    def make_json_report(self):
        """

        Преобразуем словарь в json

        """
        encode_json = json.dumps(self.dict_all_app)
        self.json_all_app = encode_json

    def get_report(self):
        """

        Формируем отчет

        """
        full_search_url = self.get_full_search_url(self.keyword)
        html_obj = self.get_html_obj(full_search_url)
        self.make_list_url_app(html_obj, self.list_url_app)
        self.run_scan()
        self.make_json_report()


if __name__ == '__main__':
    parser_result = GooglePlayMarketParser(keyword_app=args.keyword)
    parser_result.get_report()
    print(parser_result.json_all_app)
    print(parser_result.dict_all_app)

# python gpm_parser.py -k Сбер

