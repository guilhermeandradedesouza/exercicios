from time import sleep
pessoas=[{'nome': input('nome:'), 'idade': int(input('idade:')), 'sexo': input('[masculino/feminino] sexo:')} for pessoa in range(int(input('quantidade de pessoas:')))]
m_idade=0
mulheres=[]
idade_acima=[]
print(f'foram cadastradas {len(pessoas)} pessoas.')
for pessoa in pessoas:
    m_idade+=pessoa['idade']/len(pessoas)
    if pessoa['sexo'][0].lower()=='f':mulheres.append(pessoa['nome'])
for pessoa in pessoas:
    if pessoa['idade']>m_idade:idade_acima.append(pessoa['nome'])
print(f'A media de idades foi de {m_idade}\nAs mulheres cadastradas foram:{mulheres}\nPessoas com a idade acima da media:{idade_acima}\nTodas as pessoas:\n')
for pessoa in pessoas:
    for info_k,info_v in pessoa.items():print(f'{info_k}:{info_v}')
    sleep(1),print()