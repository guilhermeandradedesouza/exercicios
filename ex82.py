lista=[]
listapar=[]
listaimpar=[]
for a in range(int(input('vezes:'))):lista.append(int(input('numero:')))
for i in lista:
    if i%2==0:listapar.append(i)
    else:listaimpar.append(i)
print(f'geral:{lista}\npar:{listapar}\nimpar:{listaimpar}')