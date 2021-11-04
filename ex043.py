peso=float(input('seu peso em KG:'))
alturaquadrada=(float(input('sua altura em metros:')))**2
imc=peso/alturaquadrada
if imc<18.5:
    print(f'seu imc é de {imc:.2f} e voce esta \033[1;31mabaixo do peso.')
elif imc>=18.5 and imc<25:
    print(f'seu imc é de {imc:.2f} e voce esta no \033[1;32mpeso ideal.')
elif imc>=25 and imc<30:
    print(f'seu imc é de {imc:.2f} e voce esta com \033[1;33msobrepeso.')
elif imc>=30 and imc<40:
    print(f'seu imc é de {imc:.2f} e voce esta com \033[1;31mobesidade.')
else:
    print(f'seu imc é de {imc:.2f} e voce esta com \033[1;31obesidade morbida.')
print('\033[m\033[1;4mFIM')