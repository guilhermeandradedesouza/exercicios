from time import sleep
jogador={'nome':input('nome do jogador:'),'partidas':int(input('quantidade de partidas:'))}
lista=[int(input(f'Quantidade de gols na {f+1}º partida:')) for f in range(jogador['partidas'])]
jogador['gols']=lista[:]
print(20*'-=')
for campo,info in jogador.items():
    print(f'O campo partidas possui {campo} tem valor {info}.')
    sleep(1)
print(20*'-=',f'Joelson jogou {jogador["partidas"]} partidas.',sep='\n')
for partida,gol in enumerate(jogador['gols']):
    print(f'O {jogador["nome"]} fez {gol} gols na {partida+1}º partida.')
    sleep(1.2)
print(f'foi um total de {sum(lista)} gols.')