matriz=[]
somadospares=0
for a in range(3):
    for b in range(3):
        matriz.append(int(input(f'digite um valor para a posição {a},{b}:')))
        if matriz[-1]%2==0:somadospares+=matriz[-1]
print()
for linhas in range(9):print(f'[ {matriz[linhas]} ]',end='\n' if (linhas+1)%3==0 else ' ')
print(f'\nA soma da terceira coluna é {matriz[6]+matriz[7]+matriz[8]}.\nA soma dos valores pares é {somadospares}.\nO maior valor da segunda linha foi {max(matriz[3:6])}.')

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