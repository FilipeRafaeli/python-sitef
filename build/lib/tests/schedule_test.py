from sitef import transaction, schedule
from tests.resources.dictionaries import transaction_dictionary, card_dictionary


def test_confirm_scheduling():
    trx = transaction.create(transaction_dictionary.TRANSACTION_WITH_SCHEDULE)
    ctx = dict(card=card_dictionary.VALID_CARD)
    ret = schedule.confirm(trx['schedule']['sid'], ctx)
    te = ret.get('schedule')
    naote = te.get('sid')
    assert ret['code'] == '0'
    assert ret['schedule']['status'] == 'ATV'
