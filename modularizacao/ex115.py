def cadastrar():
    nome=input('Nome:')
    while True:
        try:idade=int(input('Idade:'))
        except ValueError:print('\033[1mDigite sua idade.\033[m')
        except KeyboardInterrupt:print('Termine o cadastro primeiro!')
        else:break
    open('cadastrados.txt','a').write(nome+' '*10+str(idade)+' anos\n')
def listar():
    from time import sleep as sp
    try:
        print('\n'*2+open('cadastrados.txt','r').read())
        #for idadeEnome in open('cadastrados.txt','r').readlines():print(idadeEnome): incial
    except FileNotFoundError:
        print('\nO arquivo não foi encontrado.')
        sp(2)
        print('gerando arquivo',end='')
        open('cadastrados.txt','w')
    for pontos in range(5):
        print('.',end='\n' if pontos==4 else '')
        sp(0.5)