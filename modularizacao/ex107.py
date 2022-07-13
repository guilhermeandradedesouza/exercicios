def mult(string,valor):
    lista=list()
    if type(string)=='str':
        for x in string:
            if x.isnumeric():lista.append(x)
        for quant in range(string.count(''.join(lista))):string.replace(''.join(lista), str(int(''.join(lista)) * valor))
        return string
    else:return string*valor
def percentual(num,porcentagem):return num+num*porcentagem//100 if type(num)==type(porcentagem)=='int' else num+num*porcentagem/100