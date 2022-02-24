inputs=[]
pesos=[]
pessoas=int(input('quantidade de pessoas:'))
max_peso=min_peso=0
pesos_max_min=[[],[]]
for a in range(pessoas):
    for c in range(2):inputs.append(int(input('peso:')) if c==1 else input('nome:'))
    if a==0 or inputs[1]>max_peso:
        max_peso=inputs[1]
        if a==0:min_peso=max_peso
    elif inputs[1]<min_peso:min_peso=inputs[1]
    pesos.append(inputs[:])
    inputs.clear()
for a in pesos:
    if a[1]==max_peso:pesos_max_min[0].append(a[0])
    elif a[1]==min_peso:pesos_max_min[1].append(a[0])
for c in range(2):print('foram cadastradas '+'\nO','maior' if c==0 else 'menor' ,f'peso foi de {pesos_max_min[0] if c==0 else pesos_max_min[1]}')