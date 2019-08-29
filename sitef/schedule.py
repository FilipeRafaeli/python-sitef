from sitef.resources import handler_request
from sitef.resources.routes import schedule_routes


def confirm(sid, dictionary={}):
    return handler_request.post(schedule_routes.SCHEDULE_URL.format(sid), dictionary)


def edit(sid, dictionary={}):
    return handler_request.put(schedule_routes.EDIT_SCHEDULE_URL.format(sid), dictionary)
