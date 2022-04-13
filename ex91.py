from random import randint
from time import sleep
lugar=1
jogadores={f'jogador {num}':randint(1,6) for num in range(1,5)}
print(sorted(jogadores.values()))
print('\033[1mValores:\033[m')
for jogador,valor in jogadores.items():
    print(f'{jogador} tirou {valor}')
    sleep(1)
print('\n\033[1m'+'ranking dos jogadores:'.upper()+'\033[m')
for ordem,num in enumerate(sorted(jogadores.values(),reverse=True)):
    for jogador in jogadores.keys():
        if jogadores[jogador]==num:
           print(f'{lugar}º:{jogador} com {num}')
           lugar += 1
           sleep(1)
           break