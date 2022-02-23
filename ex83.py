a=input('equação:')
if a[:a.index(')')+1].count('(')==0:print('falso'),exit()
if (a.count('(')+a.count(')'))%2==0:print('a expreção é verdadeira.')
else:print('falsa')