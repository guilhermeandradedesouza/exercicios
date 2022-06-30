def escreva(texto):print('\033[1m'+'~'*(len(texto)+3)+f'\n{texto:^{len(texto)+2}}\n'+'~'*(len(texto)+3))
escreva(input('mensagem:'))