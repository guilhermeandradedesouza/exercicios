for vezes in range(int(input('vezes:'))):
    a=int(input('numero:'))
    lista=[]
    while a>0:
        lista.append(a%2)
        a=a//2
    for num,c in enumerate(reversed(lista)):print(c,end=f'\n' if num==len(lista)-1 else '')