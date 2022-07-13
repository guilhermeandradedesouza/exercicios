def mult(string,valor,mostrar=False,letra=True):
    lista=list()
    for x in string:
       if x.isnumeric():lista.append(x)
    if letra:string=string.replace(''.join(lista),str(int(''.join(lista))*valor))
    else:string=str(int(''.join(lista))*valor)
    return string+'R$' if mostrar else string
def percentual(num,porcentagem,mostrar=True):
    num=int(num)
    return str(num+num*porcentagem/100)+'R$' if mostrar else str(num+num*porcentagem/100)
def resumo(num,*porcentagens):
    from random import randint
    print('\/._-^█'[randint(0,6)]*(19+len(str(num)))+f'\n{f"RESUMO DO NUMERO {num}":^{len(str(num))+21}}\n'+'\/._-^█'[randint(0,6)]*(len(str(num))+19)+f'\nPreço:{num:>20}\nDobro:{num:>20}\nMetade:{num:>20}')
    for valores in porcentagens:print(f'{valores}% de aumento:{percentual(num,valores,False):>20}')
    print('\/._-^█'[randint(0,6)]*(len(str(num))+19))