t=0
n=int(input('numero:'))
for c in range(1,n+1):
    if n%c==0:
        print('\033[32m',end='')
        t+=1
    else:
        print('\033[m',end='')
    print(c,end=' ')
if t==2:
        print('\n\033[messe numero é primo.')
else:
        print('\n\033[messe numero não é primo')