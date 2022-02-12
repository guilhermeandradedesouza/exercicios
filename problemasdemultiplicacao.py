from random import randint
erradas=[]
n=['a',0,0,'n',6]
while n[0][0].lower()!='n':
    for a in range(int(input('quantas repetições antes de perguntar se voce quer parar? '))):
        if n[3][0]!='s':b=[randint(1,9),randint(1,9)]
        c=input(f'{b[0]}x{b[1]}:'if n[0]=='a' else f'\n{b[0]}x{b[1]}:')
        while c.isnumeric()!=True:input(f'digite novamente\n{b[0]}x{b[1]}:'if n[0]=='a' else f'\ndigite novamente\n{b[0]}x{b[1]}:')
        c=int(c)
        n[2]+=1
        if c==b[0]*b[1]:
            print('\033[32mvoce acertou\033[m\n')
            n[1]+=1
        else:
            print(f'\033[31mvoce errou\033[m\nresposta:{b[0]*b[1]}\n')
            erradas.append(f'{b[0]}x{b[1]}')
        if a!=0 and a%9==0:
            n[3]=(input('deseja algo mais dificil? '))
            n[4]+=5 if a==9 else 10
            if n[3][0].lower()=='s':b=[randint(n[4],n[4]+randint(1,3)),randint(n[4],n[4]+randint(1,7))]
    n[0]=input('deseja continuar?')
    if n[0].isalpha()==False:n[0]='s'
print(f'\n\033[94mVoce acertou {n[1]} questões de {n[2]} ou seja %{n[1]*100/n[2]:.0f}.\n\033[31mAs questoes erradas foram:'if n[1]*100/n[2]>50 else f'\n\033[94mVoce acertou {n[1]} questões de {n[2]} ou seja \033[93m%{n[1]*100/n[2]}.\n\033[31mAs questoes erradas foram: ',end='')
for abc in erradas:print(f'{abc}',end=' ')