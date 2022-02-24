valores=[[],[]]
for c in range(7):
    numero=int(input('numero:'))
    if numero%2==0:valores[0].append(numero)
    else:valores[1].append(numero)
for c in range(2):print('\nvalores','impares:' if c==1 else 'pares:' ,f'{valores[0 if c==0 else 1]}')