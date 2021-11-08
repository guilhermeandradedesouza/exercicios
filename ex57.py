s=''
while s!='M' and s!='F':
    s=input('sexo:').upper
    if s not in "MF":
        print('digite novamente')
print(f'o sexo digitado {s}')
