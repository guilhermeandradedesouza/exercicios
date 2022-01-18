from random import randint
n=['a',0]
repeticoes=int(input('quantas repetições antes de perguntar se voce quer parar? '))
while n[0][0].lower()!='n':
    for a in range(repeticoes):
        b=[randint(0,9),randint(0,9)]
        c=input(f'{b[0]}x{b[1]}:'if n[0]=='a' else f'\n{b[0]}x{b[1]}:')
        while c.isnumeric()!=True:input(f'digite novamente\n{b[0]}x{b[1]}:'if n[0]=='a' else f'\ndigite novamente\n{b[0]}x{b[1]}:')
        c=int(c)
        if c==b[0]*b[1]:
            print('\033[32mvoce acertou\033[m\n')
            n[1]+=1
        else:print(f'\033[31mvoce errou\033[m\nresposta:{b[0]*b[1]}\n')
    n[0]=input('deseja continuar?')
    if n[0].isalpha()==False:n[0]='g'