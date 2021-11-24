from random import randint
g=r=0
while True:
    n=''
    if r=='resposta infinita':pass
    else:r=0
    if g==0:print('jogo do impar ou par\n'.upper()+'\033[1;33m'+'1 Round'.upper()+'\033[m')
    while n.isnumeric()!=True:
        n=input('numero:'.upper())
        if 'resposta' in n:r=1
    n=int(n)
    if n>2:a=randint(0,n)+n
    else:a=randint(0,11)+n
    pm=input(f'impar ou par? a resposta é {a} ' if r==1 else 'impar ou par? ')
    if a%2!=0 and pm=='p' or pm=='par':break
    if a%2==0 and pm=='i' or pm=='impar':break
    g+=1
    print(f'\033[36mVoce venceu\ncomputador:{a-n}\njogador:{n}\n{a-n}+{n}={a} é par\n\033[33;1m{g+1} ROUND\033[m' if a%2==0 else f'\033[36mVoce venceu\ncomputador:{a-n}\njogador:{n}\n{a-n}+{n}={a} é impar\n\033[33;1m{g+1} ROUND\033[m')
print(f'\033[31;1m\nVocê perdeu com o total de {g} vitorias.' if g>0 and g!=1 else f'\n\033[31;1mVocê perdeu.', f'\033[31;1m\nVocê perdeu, teve uma vitoria.' if g==1 else '')