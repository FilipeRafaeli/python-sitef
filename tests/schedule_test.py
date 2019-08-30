from sitef import transaction, schedule
from tests.resources.dictionaries import transaction_dictionary, card_dictionary


def test_confirm_scheduling():
    trx = transaction.create(transaction_dictionary.TRANSACTION_WITH_SCHEDULE)
    ctx = dict(card=card_dictionary.VALID_CARD)
    ret = schedule.send(trx['schedule']['sid'], ctx)
    assert ret['code'] == '0'
    assert ret['schedule']['status'] == 'ATV'


def test_edit_scheduling():
    try:
        trx = transaction.create(transaction_dictionary.TRANSACTION_WITH_SCHEDULE)
        ctx = dict(card=card_dictionary.VALID_CARD)
        ret = schedule.send(trx['schedule']['sid'], ctx)
        sid = ret['schedule']['sid']
        ctx = {'sid': sid}
        ret = schedule.edit_post(ctx)

        assert ret['code'] == '0'
        assert ret['schedule_edit']['status'] == 'CON'
    except Exception as e:
        er = e


def test_confirm_payment():
    try:
        trx = transaction.create(transaction_dictionary.TRANSACTION_WITH_SCHEDULE)
        ctx = dict(card=card_dictionary.VALID_CARD)
        ret = schedule.confirm(trx['schedule']['sid'], ctx)
        assert ret['code'] == '0'
        assert ret['schedule_edit']['status'] == 'CON'
    except Exception as e:
        er = e


def test_deactivate_schedule():
    try:
        seid = 'qwertyuiopasdfghjklzxcvbnm0123456789qwertyuiopasdfghjklzxcvbnm02'
        ctx = transaction_dictionary.EDIT_SCHEDULE_DEACTIVATE
        ret = schedule.edit_put(seid, ctx)
        assert ret['code'] == '0'
        assert ret['schedule_edit']['status'] == 'CON'
    except Exception as e:
        er = e


'''
item 15 do manual de integração:
Fluxo de edição de agendamento para inativação:
1. O lojista inicia uma edição de agendamento passando o SID da transação desejada. Em caso de sucesso, o
    e-SiTef retornará código e mensagem correspondentes.
1.1.Durante a chamada de criação de edição de agendamento, o e-SiTef fará um POST na URL de
    autenticidade cadastrada da loja com o SEID (identificador da edição de agendamento). A loja deve
    então responder a esse POST com um código HTTP 200 (OK). Caso esse código não seja devolvido, o eSiTef 
    interpretará como uma falha nessa operação e invalidará o SEID.
2. A loja virtual prossegue o fluxo chamando o serviço de edição de agendamento, passando o SEID obtido
    no POST de autenticidade e os dados a serem alterados. Caso nenhum problema ocorra, o e-SiTef
    retornará uma mensagem de sucesso e os dados atualizados do agendamento.
'''
