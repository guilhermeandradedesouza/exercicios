from modularizacao import ex107
num=int(input('Preço R$ >'))
for frases in (f'A metade do preço {num} é {ex107.mult(num,0.5)}R$.',f'O dobro de {num} é {ex107.mult(num,2)}R$',f'Aumentando em 10% o valor fica {ex107.percentual(num,10)}R$',f'Aumentando em 13% o valor fica {ex107.percentual(num,13)}R$'):print(frases,end='\n')