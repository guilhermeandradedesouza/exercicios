def mult(string,valor,mostrar=False,letra=True):
    lista=list()
    for x in string:
       if x.isnumeric():lista.append(x)
    if letra:string=string.replace(''.join(lista),str(int(''.join(lista))*valor))
    else:string=str(int(''.join(lista))*valor)
    return string+'R$' if mostrar else string
def percentual(num,porcentagem,mostrar=True):
    num=int(num)
    return str(num+num*porcentagem/100)+'R$' if mostrar else ''