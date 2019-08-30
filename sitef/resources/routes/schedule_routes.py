from .base_route import BASE_URL

SCHEDULE_URL = BASE_URL + '/e-sitef/api/v1/schedules/{0}'
PAYMENT_CONFIRM_URL = BASE_URL + '/e-sitef/api/v1/payments/{0}?confirm=true'
EDIT_SCHEDULE_URL = BASE_URL + '/e-sitef/api/v1/schedules/edits'
EDIT_SCHEDULE_URL_PARAM = BASE_URL + '/e-sitef/api/v1/schedules/edits/{0}'
