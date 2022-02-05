lista=[]
for a in range(int(input('quantos valores você deseja inserir? '))):lista.append(int(input('numero:')))
print(f'\033[1;34mforam digitados {len(lista)} numeros.\nlista em ordem decrescente:{sorted(lista,reverse=True)}\no valor cinco',f'está na lista e apareceu pela primeira vez na posição de numero {lista.index(5)+1}.' if 5 in lista else 'não está na lista.')