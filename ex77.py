palavras=('felicidade','tristeza','amor','vida','familia','verdade','promessa','mentira')
vogais=('a','e','i','o','u')
for a,g in enumerate(palavras):
    print(f'na palavra {g} temos as vogais ',end='')
    for c in vogais:
        if c in palavras[a]:print(c,end=' ')
    print('\n')