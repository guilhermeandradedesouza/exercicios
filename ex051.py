g=input('com for ou com while:')
if g=='for':
    b=int(input('primeiro termo da p.a:'))
    a=int(input('razão da p.a:'))
    for c in range(b,a*9+b+1,a):
        print(c,end=' ')
elif g=='while':
    a=int(input('primeiro termo da P.A:'))
    while