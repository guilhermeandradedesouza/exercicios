from random import randint
g=0
while True:
    n=int(input('jogo do impar ou par\nnumero:'.upper()))
    pm=input('impar ou par? ')
    if n>2:a=randint(0,n)+n
    else:a=randint(0,11)
    if pm=='p':pm='par'
    elif pm=='i':pm='impar'
    if a%2==0 and 'impar' in pm:break
    g+=1
    print(f'Voce venceu, {a-n}+{n}={a} é par\n\033[35m{g+1} ROUND\033[m' if pm=='par' and a%2==0 else f'Voce venceu, {a-n}+{n}={a} é {pm}\n\033[35m{g+1} ROUND\033[m')
print(f'\033[31m\nVoce perdeu com o total de {g} vitorias' if g>0 else '\nVoce perdeu')