from time import sleep
nomes_lista=[]
notas_nomes=[]
nota=[]
naoemnomes=[]
for a in range(int(input('quantidade de alunos:'))):
    g=input('nome:')
    notas_nomes.append([g])
    nomes_lista.append(g)
    for vezes in range(2):nota.append(int(input(f'Nota {vezes+1}:')))
    notas_nomes[a].append(nota[:])
    nota.clear()
print('\033[1m'+'='*15+'\nmedias\n'.upper())
for dados in notas_nomes:print(f'Media do {dados[0]}: {(dados[1][0]+dados[1][1])/2}\n',('='*15+'\033[m\n') if notas_nomes[len(notas_nomes)-1]==dados else '')
sleep(1)
if input('deseja procurar alguem? ')[0]=='s':
    procurar=[input('nome da pessoa:') for pessoa in range(int(input('quantidade de pessoas para procurar:')))]
    for pessoas in procurar:
        if pessoas not in nomes_lista:
            naoemnomes.append(pessoas)
            print(f'\033[31mpessoa {pessoas} não encontrada.\033[m\n')
    for tirar in naoemnomes:procurar.remove(tirar)
    for num in range(len(procurar)):print(f'As notas de {notas_nomes[num]} são respectivamente, {notas_nomes[num][1][0]} e {notas_nomes[num][1][1]}')
else:print('OK!')
