from datetime import date
b=0
c=0
for i in range(0,7):
    a=input('ano ou idade:')
    if a=='idade' or a=='i':
        g=int(input('quantos anos voce tem? '))
        if g>=18:
            b+=1
        elif g<18:
            c+=1
    elif a=='ano' or a=='a':
        g=date.today().year-int(input('quando voce nasceu? '))
        if g>=18:
            b+=1
        elif g<18:
            c+=1
    else:
        'nada'
print(f'\033[m\n{b} pessoas são maiores de idade e {c} são menores.')