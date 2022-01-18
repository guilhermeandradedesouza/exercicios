palavras=('felicidade','tristeza','amor','vida','familia','verdade','promessa','mentira')
for a,g in enumerate(palavras):
    print(f'na palavra {g} temos as vogais ',end='')
    if 'a' in palavras[a]:print('a',end=' ')
    if 'o' in palavras[a]: print('o', end=' ')
    if 'i' in palavras[a]: print('i', end=' ')
    if 'e' in palavras[a]: print('e', end=' ')
    if 'u' in palavras[a]: print('u', end=' ')
    print('\n')