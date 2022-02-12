lista=[]
for a in range(int(input('vezes:'))+1):
    b=int(input('numero:'))
    if a==0:
        lista.append(b)
        print('add ao final')
    else:
        if b>max(lista):
            lista.append(b)
            print('add ao final')
        elif b<min(lista):
            lista.insert(0,b)
            print('add casa 0')
        else:
            if len(lista)>2:
                for g in lista[1:-1]:
                    if b>g:
                        lista.insert(lista.index(g)+1,b)
                        print(f'add na casa {lista.index(b)}')
                        break
            else:
                lista.insert(1,b)
                print('add casa 1')
print(lista)