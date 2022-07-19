def leiaint(msg):
    while True:
        try:ipt=int(input(msg).strip())
        except ValueError:ipt=input('\n\033[31mErro digite um numero inteiro!\033[m\nDigite um número inteiro:')
        except KeyboardInterrupt:
            print('\nO usuário preferiu não digitar.')
            return 0
        else:return ipt
def leiafloat(msg):
    while True:
        try:floatnum=float(input(msg).strip().replace(',','.'))
        except KeyboardInterrupt:
            print('\nO usuário preferiu não digitar.')
            return 0
        except ValueError:floatnum=input('\n\033[31mErro digite um número racional!\033[m\nDigite um número:')
        else:return floatnum
print(f'\nO numero inteiro digitado foi {leiaint("Digite um número:")}, o racional foi {leiafloat("Digite um número:")}.')