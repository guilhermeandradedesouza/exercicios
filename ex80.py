lista=[]
for a in range(5):
    numero=int(input('numero:'))
    if a==0:lista.append(numero)
    elif numero>max(lista):lista.append(numero)
    elif numero<min(lista):lista.insert(0,numero)
    elif a==2 and max(lista)>numero>min(lista):lista.insert(1,numero)
    elif a==3:lista.insert(1 if lista[1]>numero else 2,numero)
    elif a==4 and max(lista[1:-1])>numero>min(lista[1:-1]):lista.insert(2,numero)
    print(f'posição {lista.index(numero)}.')
print(lista)