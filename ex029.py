km=float(input("quantidade de km/h:"))
if km>80: print(f'\033[31msua multa foi de {(km-80)*7:.2f}R$')
else: print("\033[32mtudo ok")