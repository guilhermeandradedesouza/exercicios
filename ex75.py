a=[0,0,0,0,0]
for v in range(4):a[v]=int(input('numero:'))
valores=(a[0],a[1],a[2],a[3])
print(f'Os valores digitados foram:{valores}.\nO 9 apareceu {valores.count(9)} vezes.' if valores.count(9)>1 or valores.count(9)==0 else 'O 9 so foi digitado 1 vez.')
if 3 not in valores:print('o valor 3 não apareceu.')
else:print(f'O valor 3 foi digitado pela primeira vez na {valores.index(3)+1}º posição.')
print('os valores pares digitados foram:',end='')
for g in valores:
    if g%2==0:
        print(g,end=' ')
        a[4]+=1
if a[4]==0:print('\033[31;1mnão houveram valores pares')