c=a=b=m=f=menordeidade=p=0
while True:
    while True:
        a=input('qual seu sexo? ' if a==0 else '\nqual seu sexo? ')
        if 'm' in a:m+=1
        if 'f' in a or 'm' in a:break
    p+=1
    while True:
        b=input('\nquantos anos voce tem? ')
        if b.isnumeric()==True:break
    b=int(b)
    if 'f' in a:
        f+=1
        if b<20:menordeidade+=1
    while True:
        c=input('\nquer continuar? ')
        if c=='sim' or c=='s' or c=='n' or c=='nao' or c=='não':break
    if c=='n' or c=='nao' or c=='não':break
print(f'\033[1m\npessoas:{p}\ntotal de mulheres:{f}\nmulheres menores de 18:{menordeidade}\nhomens:{m}'.upper())