valor=float(input('valor da casa:'))
salario=float(input('salario:'))
anos=int(input('em quantos anos voce quer pagar? '))
prestaçao=valor/(anos*12)
if prestaçao<=salario*0.3:
    print(f'voce não pode financiar essa casa a prestação sera de {prestaçao:.2f}R$')
else:
    print(f'a prestação mensal sera de {prestaçao:.2f}R$ durante o periodo de {anos} anos')