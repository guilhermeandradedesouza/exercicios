idade=int(input('sua idade:'))
if idade<=9:
    print('voce é um nadador mirim')
elif idade>9 and idade<=14:
    print('voce é um nadador infantil')
elif idade>14 and idade<=19:
    print('voce é um nadador junior')
elif idade==20:
    print('voce é um nadador sênior')
else:
    print('voce é um nadador master')
print('\033[1;34mFIM')