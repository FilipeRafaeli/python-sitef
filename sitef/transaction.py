from sitef.resources import handler_request
from sitef.resources.routes import transaction_routes


def create(dictionary):
    return handler_request.post(transaction_routes.TRANSACTION_URL, dictionary)
