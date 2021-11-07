a=[0,0,0]
while a[2]!=999:
    a[2]=int(input('numero:'))
    if a[2]!=999:
        print('\033[1;33merrado\033[m')
        a[1]+=1
        a[0]+=a[2]
print(f'\nForam necessarias {a[1]} tentivas e a soma dos números foi {a[0]}.')