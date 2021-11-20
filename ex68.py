from random import randint
g=0
while True:
    n=int(input('jogo do impar ou par\nnumero:'.upper()))
    pm=input('impar ou par? ')
    if n>2:a=randint(0,n)+n
    else:a=randint(0,11)+n
    if 'par' in pm:pm='par'
    elif 'impar':pm='impar'
    if a%2==0 and pm=='par':pass
    elif a%2!=0 and pm=='impar':pass
    else:break
    g+=1
    print(f'Voce venceu, {a-n}+{n}={a} é {pm}\n\033[33m{g+1} ROUND\033[m')
print(f'\033[31m\nVoce perdeu com o total de {g} vitorias {a}' if g>0 else f'\nVoce perdeu {a}')