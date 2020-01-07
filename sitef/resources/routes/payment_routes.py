from decouple import config

from .base_route import BASE_URL

PAYMENT_URL = BASE_URL + config('PAYMENT_URL_SITEF')  # '/api/v1/payments/{0}'
PAYMENT_CONFIRM_URL = BASE_URL + config('PAYMENT_CONFIRM_URL_SITEF')  # '/api/v1/payments/{0}?confirm=true'
