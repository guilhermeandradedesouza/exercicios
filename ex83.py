'''a=input('equação:')
if (a.count('(')+a.count(')'))%2==0:print('a expreção é verdadeira.')
else:print('falsa')'''
a=input('equação:')
print(a.split(')'))
for c in a.split(')'):