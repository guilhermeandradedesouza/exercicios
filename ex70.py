n=p=mp=c=ptotal=maior1000=nmp=g=0
while True:
    n=input('nome do produto:' if g==0 else '\nnome do produto:')
    if g==0:nmp=n
    while True:
        p=input('preço do produto:')
        if p.isnumeric()==True:break
    p=int(p)
    if p>1000:maior1000+=1
    if g==0:mp=p
    elif p<mp:
        mp=p
        nmp=n
    ptotal+=p
    g+=1
    while c!='nao' and c!='não' and c!='n' and c!='sim' and c!='s':c=input('quer continuar? ')
    if c=='não' or c=='n' or c=='nao':break
    c=''
print(f'\ntotal gasto:{ptotal:.2f}R$\nmenor preço:{mp:.2f}R$\nnome do produto de menor preço:{nmp}\nprodutos acima de 1000$:{maior1000}')