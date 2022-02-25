quant=0
a=input('equação:')
for num,letras in enumerate(a):
    if letras==')':quant+=1
    if letras==')' and a[:num].count('(')==quant:print('falso'),exit()
if (a.count('(')+a.count(')'))%2==0:print('a expreção é verdadeira.')
else:print('falsa')