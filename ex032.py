from datetime import date
ano=input('digite 0 para verificar esse ano. ano:')
if ano.isnumeric()==False:
    ano=date.today().year
else:
    ano=int(ano)
if ano%4==0 and ano%100!=0 or ano%400==0:
    print(f"{ano} é um ano bissexto")
else:
    print(f"{ano} não é um ano bissexto")