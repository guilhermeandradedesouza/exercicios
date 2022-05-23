from time import sleep
def contador(inicio,fim,passo):
    print(f'contagem de {inicio} ate {fim} de {passo if passo!=0 else 1} em {passo if passo!=0 else 1}.')
    if passo<0 and fim>inicio:print('\033[1;31mErro!'),exit()
    for num in range(inicio,fim+(1,-1)[0 if fim>inicio else 1],(passo*(1,-1)[0 if fim>inicio or passo<0 else 1],1 if fim>inicio else -1)[0 if passo!=0 else 1]):
        print(num,end=' ')
        sleep(0.5)
    print()
for valores in ((1,10,1),(10,0,2)):
    contador(valores[0],valores[1],valores[2])
    print('-='*30)
contador(int(input('Agora é sua vez:\n\nInicio:')),int(input('\nFim:')),int(input('\nPasso:')))