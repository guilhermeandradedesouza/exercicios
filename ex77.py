palavras=('felicidade','tristeza','amor','vida','familia','verdade','promessa','mentira')
vogais=('a','e','i','o','u')
for a,g in enumerate(palavras):
    print('\033[1m\n'+'_-'*40+f'\nNa palavra {g} temos as vogais ' if a>=1 else f'Na palavra {g} temos as vogais ',end='')
    for c in vogais:
        if c in palavras[a]:print(c,end=' ')