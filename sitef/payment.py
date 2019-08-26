from sitef.resources import handler_request
from sitef.resources.routes import payment_routes


def confirm(nit, dictionary={}):
    return handler_request.post(payment_routes.PAYMENT_URL.format(nit), dictionary)
