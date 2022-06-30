def voto(nascimento):
    from datetime import datetime as data
    idade=data.today().year-int(nascimento)
    return ''.join((f'Com {idade} anos seu voto é:','Negado!' if idade<16 else 'Opcional.' if idade>=65 or 18>idade>=16 else 'Obrigatório!'))
print(voto(2004))