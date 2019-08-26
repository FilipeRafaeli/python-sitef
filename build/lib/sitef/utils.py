import datetime
import re

from sitef.config_vars import INTERVALO_ANUAL, INTERVALO_BIANUAL


def next_charge(prazo):
    date = datetime.date.today()
    day = 5
    month = (date.month + 1) % 12
    month = month if 1 <= month <= 12 else 1
    year = int(date.year + (month + 1) / 12)
    if prazo == INTERVALO_ANUAL:
        year += 1
        month = date.month
    elif prazo == INTERVALO_BIANUAL:
        year += 2
        month = date.month
    return datetime.date(year, month, day)


def retornar_codigo_bandeira_cartao(number):
    if re.search(
            "^(4011(78|79)|43(1274|8935)|45(1416|7393|763(1|2))|50(4175|6699|67[0-7][0-9]|9000)|627780|63(6297|6368)|650(03([^4])|04([0-9])|05(0|1)|4(0[5-9]|3[0-9]|8[5-9]|9[0-9])|5([0-2][0-9]|3[0-8])|9([2-6][0-9]|7[0-8])|541|700|720|901)|651652|655000|655021)",
            number):  # ELO
        return 41
    elif re.search("^4", number):  # VISA
        return 1
    elif re.search("^(5[1-5]|677189)|^(222[1-9]|2[3-6]\d{2}|27[0-1]\d|2720)", number):  # MASTER
        return 2
    elif re.search("^3[47]", number):  # AMEX
        return 3
