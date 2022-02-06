lista=[]
for a in range(5):
    b=int(input('numero:'))
    print('add ao final'if a==0 else '')
    if a>0:
        if max(lista)<b:lista.append(b)
        elif min(lista)<b:lista.insert(lista.index(min(lista))+1,b)
    else:lista.append(b)
print(lista)