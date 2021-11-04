s=''
while s!='M' and s!='F':
    s=input('sexo:')
    if s not in "MF":
        print('digite novamente')
if s=='M':
    print('sexo masculino')
else:
    print('sexo feminino')