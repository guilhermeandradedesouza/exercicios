a=[0,0,0,0,0]
for v in range(4):a[v]=int(input('numero:'))
valores=(a[0],a[1],a[2],a[3])
print(f'Os valores digitados foram:{valores}.\nO 9 apereceu {valores.count(9)} vezes.' if valores.count(9)>1 or valores.count(9)==0 else 'O 9 so foi digitado 1 vez.')
if 3 not in valores:print('o valor 3 não apareceu.')
else:print(f'O valor 3 foi digitado pela primeira vez na {valores.index(3)+1}º posição.')
for g in range(len(valores)):
    if valores[g]%2==0:a[4]+=1
print(f'foram digitado {a[4]} valores pares.' if a[4]>1 or a[4]==0 else 'foi digitado 1 valor par.')