from random import randint
b=[0,0,randint(0,10)]
b[0]=int(input('numero de 0 a 10:'))
while b[0]!=b[2]:
    if b[2]>b[0]:
        print('é maior')
        b[1]+=1
    else:
        print('é menor')
        b[1]+=1
    b[0]=int(input('numero de 0 a 10:'))
print(f'\nvoce conseguiu com {b[1]} tentativas.')