s=input('sexo:').upper()
while s not in 'MF':
    s=input('invalido, digite novamente:').upper()
if 'M' in s:print('\no sexo digitado foi masculino')
else:print('\nsexo feminino')