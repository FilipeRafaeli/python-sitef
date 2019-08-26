from sitef.resources import handler_request
from tests.resources.sitef_test import AUTH_TEST


def test_authentication_id():
    auth = handler_request.authentication_key(AUTH_TEST['merchant_id'])
    assert auth['merchant_id'] == AUTH_TEST['merchant_id']


def test_authentication_key():
    auth = handler_request.authentication_key(AUTH_TEST['merchant_key'])
    assert auth['merchant_key'] == AUTH_TEST['merchant_key']
