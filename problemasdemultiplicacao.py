from random import randint
erradas=[]
n=['a',0,0]
repeticoes=int(input('quantas repetições antes de perguntar se voce quer parar? '))
while n[0][0].lower()!='n':
    for a in range(repeticoes):
        b=[randint(1,9),randint(1,9)]
        c=input(f'{b[0]}x{b[1]}:'if n[0]=='a' else f'\n{b[0]}x{b[1]}:')
        while c.isnumeric()!=True:input(f'digite novamente\n{b[0]}x{b[1]}:'if n[0]=='a' else f'\ndigite novamente\n{b[0]}x{b[1]}:')
        c=int(c)
        n[2]+=1
        if c==b[0]*b[1]:
            print('\033[32mvoce acertou\033[m\n')
            n[1]+=1
        else:
            print(f'\033[31mvoce errou\033[m\nresposta:{b[0]*b[1]}\n')
            erradas.insert(a,f'{b[0]}x{b[1]}')
    n[0]=input('deseja continuar?')
    if n[0].isalpha()==False:n[0]='g'
print(f'\n\033[94mVoce acertou {n[1]} questões de {n[2]} ou seja %{n[1]*100/n[2]:.0f}.\n\033[31mAs questoes erradas foram:'if n[1]*100/n[2]>50 else f'\n\033[94mVoce acertou {n[1]} questões de {n[2]} ou seja \033[93m%{n[1]*100/n[2]}.\n\033[31mAs questoes erradas foram: ',end='')
for abc in erradas:print(f'{abc}',end=' ')