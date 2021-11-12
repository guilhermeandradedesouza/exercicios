n=[0,0]
s=''
while 'sair' not in s:
    n[0]=int(input('numero:'))
    n[1]=int(input('numero:'))
    s=input('\033[1;34mO QUE VOCE QUER?\n\nSOMAR\nMULTIPLICAR\nVERIFICAR QUEM É MAIOR\nNOVOS NUMEROS\nSAIR\n\033[m')
    if 'somar' in s: print(f'a soma equivale a {n[0]+n[1]}\n')
    elif 'multiplicar' in s: print(f'o produto desses valores equivale a {n[0]*n[1]}\n')
    elif 'verificar' in s:
        if n[0]>n[1]: print(f'{n[0]}>{n[1]}\n')
        elif n[0]==n[1]: print(f'{n[0]}={n[1]}, são iguais\n')
        else: print(f'{n[1]}>{n[0]}\n')
    else:
        if 'novos' in s:print('insira os numeros novamente.\n')
        elif 'sair' not in s:print('\n\033[1;31mopção invalida digite os numeros novamente.\033[m\n')