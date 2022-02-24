matriz=[]
localizacao=[0,0]
for a in range(9):
    matriz.append(int(input(f'digite um valor para {localizacao}:')))
    localizacao[1]+=1
    if localizacao[1]==3:
        localizacao[0]+=1
        localizacao[1]=0
print()
for linhas in range(9):print(f'[ {matriz[linhas]} ]',end='\n' if (linhas+1)%3==0 else ' ')

'''matriz = []
localizacao = [0,0]
for a in range(9):
    matriz.append(int(input(f'digite um valor para {localizacao}:')))
    localizacao[1] += 1
    if localizacao[1] == 3:
        localizacao[0] += 1
        localizacao[1] = 0
print()
for linhas,matrix_2kkk in enumerate(matriz):print(f'[ {matrix_2kkk} ]',end='\n' if (linhas+1)%3==0 else ' ')'''

'''matriz = []
localizacao = [0,0]
for a in range(9):
    matriz.append(int(input(f'digite um valor para {localizacao}:')))
    localizacao[1] += 1
    if localizacao[1] == 3:
        localizacao[0] += 1
        localizacao[1] = 0
print()
for linhas,matriz_2kkk in enumerate(matriz):
    print(f'[ {matriz_2kkk} ]',end=' ')
    if (linhas+1)%3==0:print()'''