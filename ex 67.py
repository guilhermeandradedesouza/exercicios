while True:
    n=int(input('digite um numero para verificar sua tabuada:'))
    if n<0:break
    for a in range(1,11):print('<'+'-'*50+'>'+f'\n{n}x{a}={n*a}' if a==1 else f'{n}x{a}={n*a}','\n'+'<'+'-'*50+'>' if a==10 else '')