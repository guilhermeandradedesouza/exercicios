numex=('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    inteiro=input('numero entre 0 e 20:')
    if inteiro.isnumeric()==True and 0<=int(inteiro)<=20:break
print(f'\n{numex[int(inteiro)]}.')