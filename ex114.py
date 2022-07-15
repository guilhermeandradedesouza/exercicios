def leiaint():
    try:
        ipt=input('Digite um número:')
        while True:
            try:ipt=int(ipt)
            except:ipt=input('\n\033[31mErro digite um numero inteiro!\033[m\nDigite um número inteiro:')
            else:break
        return ipt
    except KeyboardInterrupt:
        print('\nO usuário preferiu não digitar.')
        return 0
def leiafloat():
    try:
        floatnum = input('Digite um número:')
        while True:
            try:floatnum=float(floatnum.strip().replace(',','.'))
            except:floatnum=input('\n\033[31mErro digite um número racional!\033[m\nDigite um número:')
            else:break
        return floatnum
    except KeyboardInterrupt:
        print('\nO usuário preferiu não digitar.')
        return 0
print(f'\nO numero inteiro digitado foi {leiaint()}, o racional foi {leiafloat()}.')