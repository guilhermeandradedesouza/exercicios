lista=[]
for a in range(int(input('quantos vezes voce quer repetir? '))):
    z=int(input('numero:'))
    if z not in lista:lista.append(z)
    else:print("esse valor ja existe em sua lista")
print(f'os valores na lista são {sorted(lista)}')