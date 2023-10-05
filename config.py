TOKEN = 'Токен Вашего бота'
API_CURRENCYLAYER = 'Ваш API для https://currencylayer.com'
CREATOR_ID = 'Ваш ID'

text_values_command = 'Для просмотра списка валют используйте команду: /values'
text_info = f'''Чтобы начать работу введите команду боту в следующем формате:
<имя валюты, цену которой хотим узнать> <имя валюты, в которой надо узнать цену первой валюты> <количество переводимой валюты>
Пример №1: доллар евро 100
Пример №2: доллар рубль 1,99
Пример №3: евро рубль 1.99
{text_values_command}'''

db_values = {
    'рубль': 'RUB',
    'доллар': 'USD',
    'евро': 'EUR',
}

# Для общей информации. Что получаем после requests https://currencylayer.com по заданной валюте
db_request = {
    'рубль евро': {'success': True, 'terms': 'https://currencylayer.com/terms',
                   'privacy': 'https://currencylayer.com/privacy', 'timestamp': 1696517283, 'source': 'RUB',
                   'quotes': {'RUBEUR': 0.009574}},
    'рубль доллар': {'success': True, 'terms': 'https://currencylayer.com/terms',
                     'privacy': 'https://currencylayer.com/privacy', 'timestamp': 1696517283, 'source': 'RUB',
                     'quotes': {'RUBUSD': 0.010071}},
    'евро доллар': {'success': True, 'terms': 'https://currencylayer.com/terms',
                    'privacy': 'https://currencylayer.com/privacy', 'timestamp': 1696517283, 'source': 'EUR',
                    'quotes': {'EURUSD': 1.051884}},
    'евро рубль': {'success': True, 'terms': 'https://currencylayer.com/terms',
                   'privacy': 'https://currencylayer.com/privacy', 'timestamp': 1696517283, 'source': 'EUR',
                   'quotes': {'EURRUB': 104.444211}},
    'доллар евро': {'success': True, 'terms': 'https://currencylayer.com/terms',
                    'privacy': 'https://currencylayer.com/privacy', 'timestamp': 1696517343, 'source': 'USD',
                    'quotes': {'USDEUR': 0.95045}},
    'доллар рубль': {'success': True, 'terms': 'https://currencylayer.com/terms',
                     'privacy': 'https://currencylayer.com/privacy', 'timestamp': 1696517343, 'source': 'USD',
                     'quotes': {'USDRUB': 99.602571}},
}
