a=0
for c in range (1,7):
    b=int(input(f'{c} numero:'))
    if b%2==0:
        a+=b
print(a)