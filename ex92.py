from time import sleep
from datetime import date
infos={'nome':input('nome:'),'idade':date.today().year-int(input('ano de nascimento:')),'carteira':int(input('carteira de trabalho:'))}
if infos['carteira']!=0:
    for extra in ('ano de contratação','salario'):infos[extra]=int(input(f'{extra}:'))
    infos['aposentadoria']=35+infos['ano de contratação']-date.today().year
for info,valor in infos.items():
    print(f'{info} recebe {valor}')
    if info=='aposentadoria':
        if infos['aposentadoria'] <= 35: print(f'\nvoce vai se aposentar com {infos[info] + infos["idade"]} anos')
    sleep(1)