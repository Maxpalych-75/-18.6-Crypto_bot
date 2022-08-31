import telebot
from Crypto_config import keys, TOKEN
from Crypto_classes import CryptoConverter, ConvertiomException

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в следующем формате: ' \
           '\n<название валюты> ' \
           '<в какую валюту перевести> ' \
           '<количество переводимой валюты> '\
           '\n'\
           '\nУвидеть список всех доступных валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные вапюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'],)
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertiomException('Неизвестная команда, для получения списка команд введите /help')

        quote, base, amount = values
        total_base = CryptoConverter.convert(quote, base, amount)
    except ConvertiomException as e:
        bot.reply_to(message, f'Ошибка ввода.\n{e}')
    except Exception:
        bot.reply_to(message, f'Неизвестная команда\n{e}, для получения списка команд введите /help')
    else:

        text = f'Цена {amount} {quote} в {base} составляет {total_base}'
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True, interval=0)



