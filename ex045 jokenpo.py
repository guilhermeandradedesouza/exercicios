from random import choice,shuffle
a=['pedra','papel','tesoura']
shuffle(a)
b=choice(a)
c=input('pedra,papel ou tesoura:')
d=f'voce ganhou, {c} e {b}'
if b=='pedra' and c=='papel':
    print(d)
elif b=='papel' and c=='tesoura':
    print(d)
elif b=='tesoura' and c=='pedra':
    print(d)
elif b==c:
    print(f'empate, {c} e {b}')
else:
    print(f'voce perdeu, {c} e {b}')