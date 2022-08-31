import requests
import json
from Crypto_config import keys


class ConvertiomException(Exception):
    error_text = f'Ошибка ввода'
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertiomException(f'Невозможно конвертировать валюту в себя {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertiomException(f'Не правильно указана валюта {quote}, для получения списка валют введите /values')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertiomException(f'Не правильно указана валюта {base}, для получения списка валют введите /values')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertiomException(f'Не правильно указано количество {amount}')


        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]
        total_base = total_base*amount

        return total_base


