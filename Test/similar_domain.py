import argparse
import threading
from abc import ABC, abstractmethod
import requests


"""

Подбор похожих доменов 

"""


parser = argparse.ArgumentParser()
parser.add_argument('-d', '--domain', type=str, help='Domain. Example:"yandex"', metavar='')
args = parser.parse_args()


class Strategy(ABC):

    def __init__(self, word):
        self.word = word

    @abstractmethod
    def get_list_change_domain(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class AddSymbol(Strategy):

    def get_list_change_domain(self):
        result = self.word
        list_symbol = [result + chr(letter) for letter in range(97, 123)]
        return list_symbol

    def __str__(self):
        return 'Добавление одного символа в конец строки'


class Replacement(Strategy):

    def get_list_change_domain(self):
        """
        Формируем список url со всеми возможными доменами

        """

        glyphs = ['o', 'i', 'z', ' ', ' ', 's', 'b', ' ', 's', 'g']

        result = [self.word]

        for index, letter in enumerate(glyphs):
            for r in result:
                if letter in r:
                    temporary = r.replace(letter, str(index), 1)
                    result.append(temporary)
        return result[1:]

    def __str__(self):
        return 'Подстановка символа, схожего по написанию (homoglyph)'


class AddPoint(Strategy):

    def get_list_change_domain(self):

        result = []

        for index, letter in enumerate(self.word, start=1):
            if letter.isdigit() or letter.isalpha():
                result.append(f'{self.word[:index]}.{self.word[index:]}')
            else:
                del result[-1]

        return result[:-1]

    def __str__(self):
        return 'Выделение поддомена, т. е. добавление точки'


class DeleteSymbol(Strategy):

    def get_list_change_domain(self):
        result = []
        for letter_index in range(len(self.word)):
            temporary = list(self.word)
            del temporary[letter_index]

            res = ''.join(temporary)
            result.append(res)

        return result

    def __str__(self):
        return 'Удалить 1 символ'


class SimilarDomain:
    list_strategy = [
        AddSymbol,
        Replacement,
        AddPoint,
        DeleteSymbol,
    ]
    result_list_url = []

    def __init__(self, domain):
        self.domain = domain

    def __choice_strategy(self):
        """

        Выбираем стратегию подбора доменов

        """
        [print(index, strategy(word=self.domain)) for index, strategy in enumerate(self.list_strategy)]
        print(f'{len(self.list_strategy)} Все перечисленные стратегии')

        input_choice = int(input('\nВыберите стратегию: '))

        if input_choice == len(self.list_strategy):
            return [strategy(word=self.domain) for strategy in self.list_strategy]
        return [self.list_strategy[input_choice](word=self.domain)]

    def __make_list_domain(self):
        """

        Формируем лист доменов

        """
        result = []
        strategies = self.__choice_strategy()
        for strategy in strategies:
            domain_test = strategy.get_list_change_domain()
            result += domain_test
        return result

    @staticmethod
    def __make_list_url(list_domain):
        """

        Формируем лист url из листа доменов принимаемого на входе функции

        """
        result = []
        domain_zone = ['com', 'ru', 'net', 'org', 'info', 'cn', 'es', 'top', 'au', 'pl', 'it', 'uk', 'tk', 'ml',
                       'ga', 'cf', 'us', 'xyz', 'top', 'site', 'win', 'bid']
        for dz in domain_zone:
            for domain in list_domain:
                res = f'https://{domain}.{dz}'
                result.append(res)
        return result

    def __try_connect(self,url):
        """

        Попытка соединения с предполагаемым url

        """
        try:
            r = requests.get(url, timeout=1)
            self.result_list_url.append(url)
        except:
            pass

    def pool_connect(self,list_url):
        """

        Формируем пул потоков-запросов, попутно очищаем его

        """
        list_thread = []

        for url in list_url:
            thread = threading.Thread(target=self.__try_connect, args=(url,))
            list_thread.append(thread)

        for thread in reversed(list_thread):
            thread.start()

        for thread in reversed(list_thread):
            thread.join()
            del list_thread[-1]
            print(f'Still have: {len(list_thread)} url')

    def run(self):
        """

        Основной метод

        """
        list_domain = self.__make_list_domain()
        check_list_url = self.__make_list_url(list_domain)
        print(f'Generate url :  {len(check_list_url)}')
        self.pool_connect(check_list_url)
        print(f'Check url :  {len(self.result_list_url)}')


if __name__ == '__main__':
    domain = args.domain
    connect_result = SimilarDomain(domain=domain)
    connect_result.run()

# python similar_domain.py -d ya