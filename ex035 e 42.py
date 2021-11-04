a=int(input('lado do triangulo:'))
b=int(input('lado do triangulo:'))
c=int(input('lado do triangulo:'))
condicao=a+c>b and b+a>c and b+c>a
if condicao and a==b==c:
    print(f'esse triangulo de lados {a},{b} e {c} existe, é \033[1mequilatero.')
elif condicao and a==b or c==b or c==a:
    print(f'esse triangulo de lados {a},{b} e {c} existe, é \033[1misoceles.')
elif condicao and a!=b!=c:
    print(f'esse trianfulo de lados {a},{b} e {c} existe, é \033[1mescaleno.')
else:
    print(f'esse triangulo de lados {a},{b} e {c} não existe')
#if a+c>b and b+a>c and b+c>a and a==b or a==c or b==c:
    #print(f"esse triangulo de lados {a},{b} e {c} é isoceles")