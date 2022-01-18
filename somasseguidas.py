from random import randint
while True:
    numeros=[randint(1,9),randint(1,9)]
    resposta=input(f'{numeros[0]}+{numeros[1]}')
    if resposta==numeros[0]+numeros[1]:print('acertou')
    else:print('\033[31merrou\033[m')