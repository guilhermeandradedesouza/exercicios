from random import randint
z=b=0
a=randint(0,10)
while b!=a:
    b=int(input('um numero de 0 a 10:'))
    if a==b: print('\033[32mvoce chutou o numero certo :)')
    else:
        print('voce errou')
        z+=1
print(f'voce conseguiu com {z} tentativas.')