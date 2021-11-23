import requests


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
        return requests.get(self.api_url, data=data)

    def get_rates(self, base_currency):
        base_currency = {'base_currency': base_currency}
        return self.get(base_currency)

