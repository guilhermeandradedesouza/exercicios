from datetime import date
ano=int(input('em que ano voce nasceu? '))
idade=date.today().year-ano
if idade==18:
    print(f'voce pode se alistar esse ano,{date.today().year}')
elif idade<18 and idade>=0:
    print(f'faltam {18-idade} anos para voce poder se alistar, voce podera se alistar em {ano+18}')
elif idade<0:
    print(f'O ano de \033[1;4;31m{ano}\033[m ainda não existe.')
else:
    print(f'ja passou o tempo para voce se alistar em {idade-18} anos, voce poderia se alistar em {date.today().year-(idade-18)}')