s=''
while s!='M' and s!='F':
    s=input('sexo:').upper
    if s not in "MF":
        print('digite novamente')
if s=='M':
    print('sexo masculino')
else:
    print('sexo feminino')
