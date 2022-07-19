from requests import get
from requests.exceptions import ConnectionError
try:get('http://pudim.com.br')
except ConnectionError:print(f'O site pudim não está acessível no momento.')
else:print('O site pode ser acessado.')