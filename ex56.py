from pygame import mixer
from time import sleep
t=''
l=m=0
g=d=['','','']
f=[0,0,0]
for a in range (0,4):
    n=input('nome:')
    i=int(input('idade:'))
    s=input('sexo:')
    l+=i
    if a==0:
       d=[i,n,s]
       g=[i,n,s]
    elif i>d[0]:
        d=[i,n,s]
    elif i<g[0]:
        g=[i,n,s]
    if s=='masculino' or s=='m':
        m+=1
    elif s=='feminino' or s=='f':
        f[0]+=1
        if i<20:
            f[1]+=1
    elif 'emo' in s and n=='sas' or n=='sasuke':
        print("\033[1mSASKEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE!!!")
        mixer.init()
        mixer.music.load('Naruto gritando Sasuke_160k.mp3')
        mixer.music.set_volume(0.18)
        mixer.music.play()
        sleep(1.5)
        exit()
    elif 'com' in s:
        mixer.init()
        mixer.music.load('HEHE BOI sound effect_160k.mp3')
        mixer.music.play()
        sleep(2)
        exit()
    elif 'todos' in s:
        mixer.init()
        mixer.music.load('C:\\Users\\Ricardo\\Desktop\\Gui\\PACK AUDIOS\\MEMES AUDIO\\13.wav')
        mixer.music.play()
        sleep(3.2)
        exit()
    else:
        f[2]+=1
        print('\033[31mSEXO NÃO DEFINIDO CORRETAMENTE.\n\033[1;33mpara masculino, masculino ou m\npara feminino, feminino ou f')
        t=f'\n\033[33;7m{f[2]} sexos não foram corretamente definidos\033[m'
    if a<3:
        print('\033[94;1mproximo\033[m')
    if d[2]=='m':
        d[2]='masculino'
    elif d[2]=='f':
        d[2]='feminino'
print(f'\033[36;1m\na media de idade entre as quatro pessoas é de {l/4:.1f} e o nome do mais velho é {d[1]} sua idade é {d[0]} e seu sexo é {d[2]}\no nome do mais novo é {g[1]} sua idade é {g[0]} e seu sexo é {g[2]},entre essas 4 pessoas {f[0]} são do sexo feminino e entre elas {f[1]} são menores de 20 anos. {m} pessoas são do sexo masculino.\nexistem {f[1]} mulheres com menos de vinte anos.{t}')