cor={'vermelho':101,'azul':44,'ciano':46,'branco':107}
def formatacao(color,mensagem,extra):return f'\033[m\033[1;{cor[color]}m'+(len(mensagem)+extra*2)*'~'+f'\n{mensagem.upper():^{len(mensagem)+extra*2}}\n'+(len(mensagem)+extra*2)*'~'
def pyhelp(pesquisa=0):
    from time import sleep as sp
    while True:
        pesquisa=input(formatacao('azul','sistema de ajuda PyHelp!!!',4)+'\n\033[mFunção ou biblioteca >')
        if pesquisa=='fim' or pesquisa=='sair':break
        print(formatacao('ciano',f'Acessando manual do comando \'{pesquisa}\'.',3))
        sp(3)
        print(f"\033[1;{cor['branco']};30m")
        help(pesquisa)
    print(formatacao('vermelho','até logo!',2))
pyhelp()