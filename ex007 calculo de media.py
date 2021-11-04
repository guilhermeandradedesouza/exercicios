from time import sleep
z=input('qual media voce quer anual ou normal? ')
if z=='anual':
    h=float(input('sua media do primeiro bimestre:'))
    f=float(input('sua media do segundo bimestre:'))
    g=float(input('sua media do terçeiro bimestre:'))
    v=float(input('sua nota do quarto bimestre:'))
    print(f'sua media anual foi de {(h+f+g+v)/4}')
else:
    p1=float(input('sua nota:'))
    p2=float(input('sua segunda nota:'))
    v1=float(input('nota da v1:'))
    simulado=float(input('nota do simulado:'))
    m=(p1+p2)*0.4+v1+simulado
    pf=(6-m)*1.0
    if m<=6:
        pergunta=input('quer saber sua nota? ')
        if pergunta=='sim' or pergunta=='s':
            print('\033[31m:(')
            sleep(1.5)
            print(f'sua media é {m:.1f} e voce precisa de {pf / 0.4:.1f} pontos.')
        else:
            print('\033[1mOk')
    else:
        print(':)')
        sleep(1.5)
        print(f'\033[32mSua media é {m:.1f}')