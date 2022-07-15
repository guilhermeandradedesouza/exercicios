from requests import get
try:get('http://pudim.com.br')
except:print('O site pudim não está acessível no momento.')
else:print('O site pode ser acessado.')