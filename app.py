import telebot

from config import *
from extensions import *

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, text=text_info)


@bot.message_handler(commands=['values'])
def values_info(message: telebot.types.Message):
    text = ('Список валют:',)
    res = '\n✦ '.join(text + tuple(db_values.keys()))

    bot.reply_to(message, text=res)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    values = message.text.split(' ')
    try:
        if len(values) != 3:
            raise ConversionException('Вы ввели количество параметров неравное 3.')

        base, quote, amount = values
        sum_values = CriptoConvector.get_price(base, quote, amount)

        res = f'Вы ввели первая валюта = {base} вторая валюта = {quote} число = {amount}'  # это потом удалить

    except ConversionException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')

    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду.\n{e}')

    else:
        text = f'Цена {db_values[base]} {db_values[quote]} {amount} - {sum_values}'
        bot.send_message(message.chat.id, res)  # это потом удалить
        bot.send_message(message.chat.id, text)  # это финальный вывод !!!верный!!!


bot.polling(none_stop=True)
