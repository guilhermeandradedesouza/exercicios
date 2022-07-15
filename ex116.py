from modularizacao import ex116
while True:
    try:opcao=int(input('número entre 1 e 3:'))
    except ValueError:print('\033[31mErro digite um numero.\033[m')
    except KeyboardInterrupt:print('\n\033[1mCaso queira sair digite o numero 3!\033[m')
    else:
        if 1<=opcao<=3:break
        else:print('\033[1;31mEntre 1 e 3!\033[m')