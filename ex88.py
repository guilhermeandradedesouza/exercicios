from random import randint
from time import sleep
sorteio=randint(1,60)
print('\033[1m-==-'*8+f'\n{"jogo da mega sena":^32}\n'.upper()+'-==-'*8+'\033[m')
lista=[[] for c in range(int(input('quantidade de jogos:')))]
for a in range(len(lista)):
    for c in range(int(input(f'Quantidade de numeros para serem sorteados no jogo {a+1}:'))):
        while sorteio in lista[a]:sorteio=randint(1,60)
        lista[a].append(sorteio)
for num,c in enumerate(lista):
    print('\n' if num==0 else '',f'jogo {num+1}: {lista[num]}')
    sleep(1)