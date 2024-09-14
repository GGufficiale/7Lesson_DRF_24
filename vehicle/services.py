import requests
from django.conf import settings
from rest_framework import status


def convert_currencies(rub_price):
    """Метод запроса курса доллара к рублю"""
    usd_price = 0
    response = requests.get(
        f'{settings.CURRENCY_API_URL}v3/latest?apikey={settings.CURRENCY_API_KEY}&currencies=RUB'
    )
    if response.status_code == status.HTTP_200_OK:
        usd_rate = response.json()['data']['RUB']['value']
        usd_price = rub_price * usd_rate
    return usd_price
