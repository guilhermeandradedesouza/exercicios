def cadastrar():
    while True:
        try:idade=int(input('idade:'))
        except ValueError:print('\033[1mDigite sua idade.\033[m')
        except KeyboardInterrupt:print('Termine o cadastro primeiro!')
        else:break
    open('cadastrados.txt','a').write(input('nome:')+' '*10+str(idade)+' anos')
def listar():
    from time import sleep as sp
    try:print('\n'+open('cadastrados.txt','r').read())
    except FileNotFoundError:
        print('\nO arquivo não foi encontrado.')
        sp(2)
        print('gerando arquivo',end='')
    for pontos in range(5):
        print('.',end='\n' if pontos==4 else '')
        sp(0.5)
    open('cadastrados.txt','w')