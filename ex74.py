from random import randint
a=(randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print(f'Os falores sorteados foram:{a}\no menor valor foi {sorted(a)[-1]}\nO maior foi {sorted(a)[0]}')