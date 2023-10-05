import telebot
from notifiers import get_notifier

from extensions import *

bot = telebot.TeleBot(TOKEN)
telegram = get_notifier('telegram')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: telebot.types.Message) -> None:
    """Функция для отправки ответным сообщением информации о том как пользоваться ботом
    при вводе команды /start или /help. Также отправляется сообщение разработчику о том, что бота начали использовать,
    в целях контроля, что нет злоупотребления API запросами т.к. они ограничены (1000 в месяц)."""
    bot.reply_to(message, text=text_info)

    message_to_me = f"Меня активировали. {CriptoConvector.get_info(message)}"
    telegram.notify(token=TOKEN, chat_id=CREATOR_ID, message=message_to_me)  # функция, чтобы отслеживать кто исп-л бота


@bot.message_handler(commands=['values'])
def values_info(message: telebot.types.Message) -> None:
    """Функция для вывода списка валют при вводе команды /values"""
    text = ('Список валют:',)
    res = '\n✦ '.join(text + tuple(db_values))

    bot.reply_to(message, text=res)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message) -> None:
    """Функция для активации конвертирования валюты (статический метод get_price класса CriptoConvector)
    в соответствии с введённым текстом, если будет ошибка ввода, то будет возбуждение исключений и вывод сообщения
    об конкретной ошибке. В случаи корректного ввода будет выведено сообщение с результатом конвертирования."""
    values = message.text.split(' ')
    try:
        if len(values) != 3:
            raise APIException('Вы ввели количество параметров неравное 3.')

        base, quote, amount = values
        sum_values = CriptoConvector.get_price(base, quote, amount)

    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')

    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду.\n{e}')

    else:
        text = f'Цена {amount} {db_values[base]} в {db_values[quote]} составляет {sum_values} {db_values[quote]}'
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
