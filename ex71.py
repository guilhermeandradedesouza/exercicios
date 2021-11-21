c50=c20=c10=c1=0
n=int(input('valor a ser sacado:'))
while n>=50:
    n-=50
    c50+=1
if c50>=1:print(f'{c50} cédulas de 50 reais.')
while n>=20:
    n-=20
    c20+=1
if c20>=1:print(f'{c20} cédulas de 20 reais.')
while n>=10:
    n-=10
    c10+=1
if c10>=1:print(f'{c10} cédulas de 10 reais.')
while n>=1:
    n-=1
    c1+=1
if c1>=1:print(f'{c1} cédulas de 1 real.')