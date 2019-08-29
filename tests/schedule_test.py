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


def test_edit_scheduling():
    trx = transaction.create(transaction_dictionary.TRANSACTION_WITH_SCHEDULE)
    ctx = dict(card=card_dictionary.VALID_CARD)
    ret = schedule.confirm(trx['schedule']['sid'], ctx)
    sid = ret['schedule']['sid']
    ctx = transaction_dictionary.EDIT_SCHEDULE
    ret = schedule.edit(sid, ctx)  # não ta achando o SID pra editar, nao sei se da pra testar, mas metodo deve ta certo
    assert ret['code'] == '0'
    assert ret['schedule_edit']['status'] == 'CON'
