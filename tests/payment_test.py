import pytest

from sitef import transaction, payment
from tests.resources.dictionaries import transaction_dictionary, card_dictionary


def test_confirm_payment():
    trx = transaction.create(transaction_dictionary.TRANSACTION)
    ctx = dict(card=card_dictionary.VALID_CARD)
    pay = payment.confirm(trx['payment']['nit'], ctx)
    assert pay['code'] == '0'
    assert pay['payment']['authorizer_code'] == '000'


def test_invalid_card_number_payment():
    trx = transaction.create(transaction_dictionary.TRANSACTION)
    ctx = dict(card=card_dictionary.INVALID_CARD_NUMBER)
    with pytest.raises(Exception) as e:
        payment.confirm(trx['payment']['nit'], ctx)
    assert str(e.value) == 'invalid cardNumber value'


