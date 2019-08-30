from sitef.resources import handler_request
from sitef.resources.routes import schedule_routes


def send(sid, dictionary={}):
    return handler_request.post(schedule_routes.SCHEDULE_URL.format(sid), dictionary)


def confirm(nit, dictionary={}):
    return handler_request.post(schedule_routes.PAYMENT_CONFIRM_URL.format(nit), dictionary)


def edit_post(dictionary={}):
    return handler_request.post(schedule_routes.EDIT_SCHEDULE_URL, dictionary)


def edit_put(seid, dictionary={}):
    return handler_request.put(schedule_routes.EDIT_SCHEDULE_URL_PARAM.format(seid), dictionary)
