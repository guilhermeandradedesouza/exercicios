s=input('sexo:')
while s not in 'MF':
    s=input('invalido, digite novamente:').upper()
if 'M' in s:print('o sexo digitado foi masculino')
else:print('\nsexo feminino')