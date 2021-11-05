g=input('com for ou com while:')
if g=='for':
    b=int(input('primeiro termo da p.a:'))
    a=int(input('razão da p.a:'))
    for c in range(b,a*9+b+1,a):
        print(c,end=' ')
elif g=='while':
    a=[0,0]
    a[1]=a[0]=int(input('primeiro termo da P.A:'))
    b=int(input('razão da P.A:'))
    while a[0]!=a[1]+b*11:
        print(a[0],end=' ')
        a[0]+=b