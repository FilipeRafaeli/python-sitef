import datetime

from decouple import config

from sitef.resources import handler_request

MERCHANT_ID = config('MERCHANT_ID')
MERCHANT_KEY = config('MERCHANT_KEY', None)

AUTH_TEST = handler_request.authentication_key(MERCHANT_ID, MERCHANT_KEY)


def next_charge():
    date = datetime.date.today()
    day = 5
    month = (date.month + 1) % 12
    month = month if 1 <= month <= 12 else 1
    year = int(date.year + (month + 1) / 12)
    return datetime.date(year, month, day)
