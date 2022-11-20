import requests
import json
from config import keys

class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Валюта {quote} отсутствует в списке доступных, что-бы узнать список доступных валют наберите /values.')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Валюта {base} отсутствует в списке доступных, что-бы узнать список доступных валют наберите /values.')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Для получения результата вместо "{amount}"введите количество валюты в числовом формате.')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        final_base = json.loads(r.content)[keys[base]]
        total_base = final_base * amount
        return total_base
