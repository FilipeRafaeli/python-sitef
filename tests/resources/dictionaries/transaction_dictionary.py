from tests.resources.sitef_test import next_charge

INTEREST_FREE = 4
MASTERCARD = 2

TRANSACTION = {
    'order_id': '1',
    'installments': '1',
    'installment_type': INTEREST_FREE,
    'authorizer_id': MASTERCARD,
    'amount': '100'
}

TRANSACTION_WITH_SCHEDULE = {
    'order_id': '1',
    'installments': '1',
    'installment_type': INTEREST_FREE,
    'authorizer_id': MASTERCARD,
    'amount': '100',
    'schedule': {
        'amount': '50',
        'initial_date': next_charge().strftime('%d/%m/%Y'),
        'interval': 1,
        'soft_descriptor': 'Assinatura',
        'do_payment_now': 'false',
        'installment_type': 4,
    },
    'additional_data': {
        'payer': {
            'store_identification': '98253053045'
        }
    }
}

EDIT_SCHEDULE_DEACTIVATE = {
    'status': 'INA'
}
