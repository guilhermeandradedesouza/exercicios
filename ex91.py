from random import randint
from time import sleep
from operator import itemgetter
lugar=1
jogadores={f'jogador {num}':randint(1,6) for num in range(1,5)}
print('\033[1mValores:\033[m')
for jogador,valor in jogadores.items():
    print(f'{jogador} tirou {valor}')
    sleep(1)
print('\n\033[1m'+'ranking dos jogadores:'.upper()+'\033[m')
for num,infos in enumerate(reversed(sorted(jogadores.items(),key=itemgetter(1)))):
    print(f'{num+1}º lugar:{infos[0]} com {infos[1]} pontos.')
    sleep(1)