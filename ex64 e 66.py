a=[0,0,0]
while a[1]!=999:
    a[1]=int(input('programa de somas\n'+'<'+'='*30+'>'+'\n\033[33mdigite 999 para parar.'+'\n\033[mnumero:' if a[0]==0 else 'numero:'))
    if a[1]==999:break
    a[0]+=1
    a[2]+=a[1]
print(f'\nvoce digitou {a[0]} numeros e a soma dos números foi {a[2]}.\n'+'<'+'='*30+'>')