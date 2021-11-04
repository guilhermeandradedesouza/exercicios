preco=int(input('quanto o produto custa:'))
pay=input('qual vai ser a forma de pagamento, dinheiro/cheque ou cartão? ')
texto=f'com \033[4m10%\033[m de desconto o produto vai passar a custar {preco-preco/10:.2f}R$'
textocartao=f'o valor do produto em duas vezes é {preco}R$ cada parcela de {preco/2:.2f}R$'
if pay=='cartão' or pay=='card' or pay=='cartao':
    cartao=input('a vista ou em duas vezes ou em tres ou para mais digite o numero:')
    if cartao=='a vista' or cartao=='1':
        print(texto[:61].replace('10%','5%'),f'{preco-preco/20}')
    elif cartao=='2' or cartao=='duas' or cartao=='duas vezes':
        print(textocartao)
    else:
        print(textocartao[:26].replace('duas',cartao),f'vezes custa {preco+preco/5:.2f}R$ cada parcela de {(preco+preco/5)/int(cartao):.2f}R$')
elif pay=='dinheiro' or pay=='cheque' or pay=='din':
    print(texto)
else:
    print('\033[31mopção invalida.')