from random import randint
while True:
    numeros=[randint(1,9),randint(1,9)]
    resposta=int(input(f'{numeros[0]}+{numeros[1]}:'))
    if resposta==numeros[0]+numeros[1]:print('acertou')
    else:print(f'\033[31merrou\033[m\na resposta era{numeros[0]+numeros[1]}')