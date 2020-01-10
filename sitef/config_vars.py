from decouple import config

# pagamento pela loja sem juros
INTEREST_FREE = 4

# intervalo de cobranças, 1 para mensal
INTERVALO_MENSAL = 1

# intervalo de cobranças, 12 para anual
INTERVALO_ANUAL = 12

# intervalo de cobranças, 24 para bianual
INTERVALO_BIANUAL = 24

# Número de parcelas
NUMERO_PARCELAS = '1'

# Timeout do post, put e get
TIMEOUT_REQUEST = int(config('TIMEOUT_REQUEST_SITEF', default=25))
