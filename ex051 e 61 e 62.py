g=input('com for ou com while:')
if g=='for':
    b=int(input('primeiro termo da p.a:'))
    a=int(input('razão da p.a:'))
    for c in range(b,a*9+b+1,a):
        print(c,end=' ')
elif g=='while':
    a=[0,0,0,'sim',1]
    a[1]=a[0]=int(input('\nprimeiro termo da P.A:'))
    b=int(input('razão da P.A:'))
    while a[0]!=a[1]+b*(11+a[2]) and a[3]=='sim' and a[4]!=0:
        print(a[0],end=' ')
        a[0]+=b
        if a[0]==a[1]+b*(11+a[2]):
            a[3]=input('\nquer mais? ')
            if 'sim' in a[3]:
                a[0]=a[1]
                a[4]=a[2]=int(input(f'\033[1;33mobs:É em relação ao numero {a[1]+b*10}\033[m\nmais quantos? '))