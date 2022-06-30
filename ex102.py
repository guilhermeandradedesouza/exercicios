def fatorial(num,show=False,f=1):
    """
    :param num: É o número que vai sofrer o processo de multiplicação pelos seus antecessores naturais não nulos.
    :param show: recebe valor booleano e decide se o processo de multiplicação do fatorial estará a mostra.
    :return: retorna o fatorial do número."""
    for fator in range(2,num+1):f*=fator
    return '.'.join([str(x) for x in reversed(range(2,num+1))])+f'={f}' if show else f
print(fatorial(6,1))