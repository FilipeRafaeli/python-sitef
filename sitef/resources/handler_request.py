import requests

from sitef.config_vars import TIMEOUT_REQUEST

KEYS = {}


def validate_response(sitef_response):
    if 200 <= sitef_response.status_code < 300:
        return sitef_response.json()
    elif sitef_response.status_code == 502:
        raise requests.exceptions.Timeout('timed-out')  # gambiarra sitef
    else:
        return error(sitef_response)


def authentication_key(merchant_id=None, merchant_key=None):
    global KEYS
    KEYS['merchant_id'] = merchant_id
    KEYS['merchant_key'] = merchant_key
    return KEYS


def post(end_point, data={}):
    sitef_response = requests.post(end_point, json=data, headers=headers(), timeout=TIMEOUT_REQUEST)
    return validate_response(sitef_response)


def get(end_point, data={}):
    sitef_response = requests.get(end_point, json=data, headers=headers(), timeout=TIMEOUT_REQUEST)
    return validate_response(sitef_response)


def put(end_point, data={}):
    sitef_response = requests.put(end_point, json=data, headers=headers(), timeout=TIMEOUT_REQUEST)
    return validate_response(sitef_response)


def headers():
    _headers = {
        'content-type': 'application/json',
        'merchant_id': KEYS['merchant_id'],
    }
    if KEYS['merchant_key']:
        _headers['merchant_key'] = KEYS['merchant_key']
    return _headers


def error(data):
    try:
        data = data.json()
        message = data['message']
    except:
        message = str(data)
    raise Exception(message)
