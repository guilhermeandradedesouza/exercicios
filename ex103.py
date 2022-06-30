def ficha(nome,quant):print(f'\nO jogador {"<desconhecido>" if nome=="" else nome} fez {"x" if quant=="" or quant.isalpha() else quant} gols.')
ficha(input('nome:'),input('quantidade de gols:'))