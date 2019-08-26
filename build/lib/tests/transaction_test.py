from sitef import transaction
from tests.resources.dictionaries import transaction_dictionary


def test_create_transaction_without_scheduling():
    amount = transaction_dictionary.TRANSACTION['amount']
    trx = transaction.create(transaction_dictionary.TRANSACTION)
    assert trx['code'] == '0'
    assert trx['payment']['status'] == 'NOV'
    assert trx['payment']['amount'] == amount
    assert trx['payment']['nit']


def test_create_transaction_with_scheduling():
    amount = transaction_dictionary.TRANSACTION_WITH_SCHEDULE['schedule']['amount']

    trx = transaction.create(transaction_dictionary.TRANSACTION_WITH_SCHEDULE)
    assert trx['code'] == '0'
    assert trx['schedule']['status'] == 'NOV'
    assert trx['schedule']['amount'] == amount
    assert trx['schedule']['sid']
