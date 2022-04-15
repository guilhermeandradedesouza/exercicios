from time import sleep
from datetime import date
infos={'nome':input('nome:'),'idade':date.today().year-int(input('ano de nascimento:')),'carteira':input('carteira de trabalho:')}
if infos!=0:
    for extra in ('ano de contratação','salario'):infos[extra]=int(input(f'{extra}:'))
    infos['aposentadoria']=35-date.today().year+infos['ano de contratação']
for info,valor in infos.items():
    print(f'{info} recebe {valor}')
    if info=='aposentadoria':
        if infos['aposentadoria'] <= 35: print(f'\nvoce vai se aposentar com {infos[info] + infos["idade"]} anos')
    sleep(1)