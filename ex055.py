c=0
b=0
for l in range(0,5):
    a=float(input('qual seu peso:'))
    if l==0:
        c=a
    if a>b:
        b=a
    if a<c:
        c=a
print(f'o maior peso foi {b}kg e o menor foi {c}kg')