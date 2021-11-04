numero=int(input('diga um numero:'))
a=input('deseja converter para binario,octal ou para hexadecimal:')
if a=='binario' or a=='bin':
    print(f'o numero {numero} em binario é {bin(numero)[2:]}')
elif a=='octal' or a=='oct':
    print(f'o numero {numero} em octal é {oct(numero)[2:]}')
elif a=='hexa' or a=='hexadecimal' or a=='hex':
    print(f'o numero {numero} em hexadecimal é {hex(numero)[2:]}')
else:
    print('\033[1;31minvalido')