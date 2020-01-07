from decouple import config

from .base_route import BASE_URL

TRANSACTION_URL = BASE_URL + config('TRANSACTION_URL_SITEF')  # '/api/v1/transactions'
CHECK_TRANSACTION_URL = BASE_URL + config('CHECK_TRANSACTION_URL_SITEF')  # '/api/v1/transactions/{0}'
