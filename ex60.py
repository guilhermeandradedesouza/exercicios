a=input('for ou while? ')
n = [0, 0, 1]
n[0] = n[1] = int(input('numero para verificar o fatorial:'))
if a=="for":
    for a in range(0,n[1]-1):
        print(f'\033[32;1m{n[1]}x{n[2]}=\033[36;4m{n[0]}\033[m',end=' ')
        n[0]=n[0]*(n[1]-n[2])
        n[2]+=+1
    print(f'\033[4m\n{n[1]}!={n[0]}')
elif a=='while':
    while n[1]-n[2]!=0:
        print(f'\033[1;32m{n[1]}x{n[2]}=\033[4;36m{n[0]}\033[m',end=' ')
        n[0]=n[0]*(n[1]-n[2])
        n[2]+=1
    print(f'\033[4m\n{n[1]}!={n[0]}')