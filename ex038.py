a=int(input('primeiro valor:'))
b=int(input('segundo valor:'))
if a>b:
    print(f'o primeiro numero é maior,\033[1m{a}>{b}.')
elif a<b:
    print(f'o segundo valor é maior,\033[1m{b}>{a}.')
else:
    print(f'os dois valores são iguais,\033[1m{a}={b}.')