import json
import requests
from .db import db
from . models import Currency, CurrencyRates
from flask_crontab import Crontab

crontab = Crontab()


class FreeCurrencyApi:

    def __init__(self):
        self.apikey = 'abbd9790-4b75-11ec-92e5-5ff22e45dd41'  # todo - DB config
        self.api_url = 'https://freecurrencyapi.net/api/v2/latest'  # todo - DB config

    def get(self, extra_data):
        """
        :param extra_data: Add extra params to request
        :return: GET request
        """
        data = {
            'apikey': self.apikey,
        }
        data.update(extra_data)
        get_data = requests.get(self.api_url, params=data)
        return get_data

    def get_rates(self, base_currency):
        base_currency = {'base_currency': base_currency}
        return self.get(base_currency)

    def add_rates_to_db(self, currency_rate, currency, currency_id_dict):
        if currency_rate and currency in currency_id_dict:
            rates_obj = [CurrencyRates(currency_id_dict[currency], currency_id_dict[code], currency_rate[code])
                         for code in currency_rate if code in currency_id_dict.keys()]
            db.session.add_all(rates_obj)
            db.session.commit()

    @crontab.job(day="1")   # run once a day
    def update_rates(self):
        currencies = Currency.query.all()
        currency_id_dict = {currency.code: currency.id for currency in currencies}
        unique_currencies_symbol = []
        [unique_currencies_symbol.append(currency.code) for currency in currencies
         if currency.code not in unique_currencies_symbol]
        for currency in unique_currencies_symbol:
            rates = self.get_rates(currency)
            try:
                rates_data = json.loads(rates.content) if rates.content else False
            except json.decoder.JSONDecodeError:
                rates_data = False
            if rates.ok and rates_data:
                currency_rate = rates_data.get('data')
                self.add_rates_to_db(currency_rate, currency, currency_id_dict)

