from decouple import config

from .base_route import BASE_URL

SCHEDULE_URL = BASE_URL + config('SCHEDULE_URL_SITEF')  # '/api/v1/schedules/{0}'
EDIT_SCHEDULE_URL = BASE_URL + config('EDIT_SCHEDULE_URL_SITEF')  # '/api/v1/schedules/edits'
EDIT_SCHEDULE_URL_PARAM = BASE_URL + config('EDIT_SCHEDULE_URL_PARAM_SITEF')  # '/api/v1/schedules/edits/{0}'
