c=a=b=m=f=idademenorque20=maiorque18=p=0
while c!='n' and c!='nao' and c!='não':
    while True:
        a=input('qual seu sexo? ' if a==0 else '\nqual seu sexo? ')[0].upper()
        if a=='M':m+=1
        if a=='F' or a=='M':break
    p+=1
    while True:
        b=input('\nquantos anos voce tem? ')
        if b.isnumeric()==True:break
    b=int(b)
    if a=='F':
        f+=1
        if b<20:idademenorque20+=1
    if b>18:maiorque18+=1
    c = input('\nquer continuar? ').strip().lower()
    while c[0]!='s' and c[0]!='n':c=input('\nquer continuar? ').strip().lower()
print(f'\033[1m\npessoas:{p}\ntotal de mulheres:{f}\nmulheres menores de 20:{idademenorque20}\nhomens:{m}\nmaiores de 18 anos:{maiorque18}'.upper())