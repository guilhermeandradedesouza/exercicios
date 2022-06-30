def leiaint(ipt=input('Digite um numero:')):
    while not ipt.isnumeric():ipt=input('\n\033[31mErro digite um numero inteiro!\033[m\nDigite um numero:')
    return int(ipt)
print(f'\nO numero digitado foi {leiaint()}.')