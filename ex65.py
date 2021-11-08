c='sim'
b=[0,0,0,0,0]
a=int(input('quantos numeros voce quer? '))
while 'sim' in c:
    for g in range(0,a):
        if g==0:
            b[4]=b[0]=b[1]=int(input('numero:'))
        elif b[2]>b[0]:
            b[0]=b[2]
        elif b[2]<b[1]:
            b[1]=b[2]
        if g>0:
            b[2]=int(input('numero:'))
        if g==a-1:
            c=input('voce quer continuar? ')
            if 'sim' in c:
                a+=int(input('mais quantas? '))
        b[3]+=1
        b[4]+=b[2]
print(f'\n\033[1mO maior numero foi {b[0]} e o menor foi {b[1]}.\nA media entre esses numeros foi de {b[4]/b[3]:.0f}.')