from random import randint
g=0
while True:
    n=int(input('jogo do impar ou par\nnumero:'.upper()))
    pm=input('impar ou par? ')
    if n>2:a=randint(0,n)+n
    else:a=randint(0,11)+n
    if pm=='p':pm='par'
    elif pm=='i':pm='impar'
    if a%2==0 and pm=='par':pass
    elif a%2!=0 and pm=='impar':pass
    else:break
    g+=1
    print(f'Voce venceu, {a-n}+{n}={a} é {pm}\n\033[33;1m{g+1} ROUND\033[m')
print(f'\033[31;1m\nVocê perdeu com o total de {g} vitorias' if g>0 else f'\n\033[31;1mVocê perdeu')