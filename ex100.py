from random import randint
from time import sleep
def sortear():
    aleatorio=[randint(1,10) for vezes in range(5)]
    print('sorteando valores:')
    for num in aleatorio:
        print(num,end=' ')
        sleep(0.5)
    return aleatorio
def somapar(lista):
    s=0
    for num in lista:
        if num%2==0:s+=num
    print(f'\nA soma dos numeros pares de {lista} é {s}.')
somapar(sortear())