nota1=float(input('sua primeira nota '))
nota2=float(input('sua segunda nota '))
media=(nota1+nota2)/2
if media<5:
    print(f'sua media é {media:.1f} e voce esta reprovado')
elif media==5 and media>=6.9:
    print(f'sua media é {media:.1f} e voce esta de recuperação')
else:
    print(f'voce foi aprovado,\033[1;32mparabens.{media}')