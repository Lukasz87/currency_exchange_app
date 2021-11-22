import requests


class FreeCurrencyApi:

    def __init__(self):
        self.apikey = 'abbd9790-4b75-11ec-92e5-5ff22e45dd41'  # todo - DB config
        self.api_url = 'https://freecurrencyapi.net/api/v2/latest'

    def get(self, url):
        return requests.get(f'{self.api_url}&{self.apikey}&{url}')

    def get_rates(self, base_currency):
        base_currency = f'base_currency={base_currency}'
        return self.get(base_currency)
