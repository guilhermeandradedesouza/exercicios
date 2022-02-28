from random import randint
from time import sleep
print('\033[1m-==-'*8+'\njogo da mega sena\n'.upper()+'-==-'*8+'\033[m')
lista=[[] for c in range(int(input('quantidade de jogos:')))]
for a in range(len(lista)):
    for c in range(int(input(f'Quantidade de numeros para serem sorteados no jogo {a+1}:'))):lista[a].append(randint(1,60))
for num,c in enumerate(lista):
    print('\n' if num==0 else '',f'jogo {num+1}: {lista[num]}')
    if num<len(lista):sleep(1)