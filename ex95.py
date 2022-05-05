jogadores=[]
for partidas in range(int(input('quantidade de jogadores:'))):
    jogadores.append({partidas: {'nome': input('nome do jogador:'), 'partidas': int(input('quantidade de partidas:'))}})
    jogadores[partidas][partidas]['gols']=[int(input(f'gols na {pontos+1}º partida:')) for pontos in range(jogadores[partidas][partidas]['partidas'])]
    print('-_-'*30)
print('cod nome     gols        total','-=-'*30,sep='\n')
for cod,pessoa in enumerate(jogadores):print(f'{cod}  {pessoa[cod]["nome"]}      {pessoa[cod]["gols"]}        {sum(pessoa[cod]["gols"]):<{len(pessoa[cod]["gols"])*5}}')
if input('deseja procurar um jogador? ')[0].lower()=='s':
    selecionado=int(input('codigo do jogador:'))
    if selecionado!=999 and selecionado<len(jogadores):
        print()
        for num in range(len(jogadores)):
            if selecionado==num:
                for infos,x in jogadores[num][num].items():print(f'{infos}={x}')
    else:print('\nERRO JOGADOR NÃO EXISTE.')
else:print('\nOK')