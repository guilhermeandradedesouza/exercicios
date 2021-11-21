c50=c20=c10=c1=0
n=int(input('valor a ser sacado:'))
while True:
    if n>=50:
        n-=50
        c50+=1
    elif n>=20:
        n-=20
        c20+=1
    elif n>=10:
        n-=10
        c10+=1
    elif n>=1:
        n-=1
        c1+=1
    else:break
print(f'cedulas de 50:{c50}\ncedulas de 20:{c20}\ncedulas de 10:{c10}\ncedulas de 1:{c1}')