from modularizacao import ex109
num=input('Preço R$ >')
for frases in (f'A metade do preço {num} é {ex109.mult(num,0.5,1,False)}!',f'O dobro de {num} é {ex109.mult(num,2,1,False)}.',f'Aumentando em 10% o valor fica {ex109.percentual(num,10)}',f'Aumentando em 13% o valor fica {ex109.percentual(num,13)}'):print(frases,end='\n'*2)