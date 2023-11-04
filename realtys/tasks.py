import requests
from realtys.models import Usd


def get_usd():
    data_from_bank = requests.get('https://www.cbr-xml-daily.ru/latest.js').json()
    rate_usr_rub = data_from_bank['rates']['USD']
    usd = Usd.objects.last()
    usd.usd_now = rate_usr_rub
    usd.save()

