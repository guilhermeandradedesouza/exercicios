from random import randint
z=b=0
while b!=randint(0,10):
    b=int(input('um numero de 0 a 10:'))
    if randint(0,10)==b: print('\033[32mvoce chutou o numero certo :)')
    else:
        print('voce errou')
        z+=1
print(f'voce conseguiu com {z} tentativas.')