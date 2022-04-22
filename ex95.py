jogadores=[]
for partidas in range(int(input('quantidade de jogadores:'))):
    jogadores.append({'nome':input('nome do jogador:'),'partidas':int(input('quantidade de partidas:'))})
    jogadores[partidas]['gols']=[int(input(f'gols na {pontos+1}º partida:')) for pontos in range(jogadores[partidas]['partidas'])]
    print('-_-'*30)
print('cod nome     gols        total','-=-'*30,sep='\n')
for cod,pessoa in enumerate(jogadores):print(f'{cod}  {pessoa["nome"]}      {pessoa["gols"]}        {sum(pessoa["gols"]):<{len(pessoa["gols"])*5}}')