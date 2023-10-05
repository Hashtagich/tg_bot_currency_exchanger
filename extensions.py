import requests
import json

from config import *


class APIException(Exception):
    pass


class CriptoConvector:
    """Класс для конвертирования стоимости валюты из одной в другую и проверки корректности введённых данных."""

    @staticmethod
    def get_price(base: str, quote: str, amount: str) -> float:
        """Статический метод для конвертирования валюты из одной в другую.
        1) Проверяется корректность ввода(передачи) данных при некорректности возбуждается исключение APIException;
        2) После проверки данных происходит парсинг, чтобы получить коэффициент, если кол-во запросов будет больше 1000
         за месяц, то возбуждается исключение Exception;
        3) Функция возвращает результат конвертирования валюты в формате числа float."""

        if base not in db_values.keys() and quote not in db_values.keys():
            raise APIException(f'{base} и {quote} нет в списке валют.\n{text_values_command}')

        elif base not in db_values.keys():
            raise APIException(f'{base} нет в списке валют.\n{text_values_command}')

        elif quote not in db_values.keys():
            raise APIException(f'{quote} нет в списке валют.\n{text_values_command}')

        elif base in db_values.keys() and quote in db_values.keys() and base == quote:
            raise APIException(f'{base} и {quote} одинаковые валюты, результат будет {amount} {db_values[base]}. '
                               f'Конвертирование не имеет смысла.')

        try:
            new_amount = amount.replace(',', '.')
            new_amount = float(new_amount)
        except ValueError:
            raise APIException(f'При вводе {amount} допущена ошибка')

        try:
            base_en, quote_en = db_values[base], db_values[quote]
            url = f'http://apilayer.net/api/live?access_key={API_CURRENCYLAYER}&currencies={quote_en}&source={base_en}&format=1'
            request = requests.get(url=url)
            db = json.loads(request.content)
            course = db['quotes'][base_en + quote_en]

        except Exception:
            print('Прошу простить, но сервер с запросами курсов валют временно не доступен.')

        else:
            return new_amount * course

    @staticmethod
    def get_info(message) -> str:
        """Статический метод возвращает строку определённого формата с содержанием информации о написавшем."""
        return f"""\nВот информация: 
        ID: {message.from_user.id};
        FIRST_NAME: {message.from_user.first_name};
        LAST_NAME: {message.from_user.last_name};
        USERNAME: {message.from_user.username}."""
