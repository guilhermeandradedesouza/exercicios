a=[]
for b in range(5):a.append(int(input(f'valor {b+1}:')))
print('os valores digitados foram:',end='')
for z in sorted(a):print(z,end=' ')
print(f'\no maior valor foi {max(a)} na posição {a.index(max(a))+1}\no valor minimo foi {min(a)} e esta na posição {a.index(min(a))+1}')