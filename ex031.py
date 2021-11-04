dis=float(input('distancia da viagem em kms '))
if dis<=200:
    print(f'vai custar {dis*0.5:.2f}R$')
else:
    print(f'a viagem vai custar {dis*0.45:.2f}R$')