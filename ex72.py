numex=('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
repitir='s'
while repitir!='n':
    while True:
        inteiro=input('numero entre 0 e 20:')
        if inteiro.isnumeric() and 0<=int(inteiro)<=20:break
    print(f'\n{numex[int(inteiro)]}.\n')
    repitir=input('deseja repitir? ')