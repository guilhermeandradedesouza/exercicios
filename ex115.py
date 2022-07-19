from modularizacao.ex115 import *
from time import sleep as sp
from random import randint as rt
personalizacao=rt(0,3)
opcao=-3
def aleatorizar():return '-~─▬'[personalizacao]
while opcao!=3:
    while True:
        try:opcao=int(input(aleatorizar()*30+'\n1 - Ver cadastrados\n2 - Cadastrar pessoa.\n3 - Sair.\n'+aleatorizar()*30+'\nSua opção:'))
        except ValueError:print('\033[31mErro digite um numero.\033[m')
        except KeyboardInterrupt:print('\n\033[1mCaso queira sair digite o numero 3!\033[m\n')
        else:
            if 1<=opcao<=3:break
            else:print('\033[1;31mEntre 1 e 3!\033[m')
    sp(0.1)
    if opcao==3:
        print(f'\033[31;1m\nVocê escolheu sair.\n'+'saindo'.upper(),end='')
        for pontos in range(35):
            print('.',end='')
            sp(0.4)
    elif opcao==2:
        print()
        cadastrar()
    elif opcao==1:
        print('\n'+aleatorizar()*30+'\npessoas cadastradas\n'.upper()+aleatorizar()*30,end='')
        listar()