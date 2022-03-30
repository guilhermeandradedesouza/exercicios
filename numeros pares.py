from time import sleep
n=0
while True:
    if n%2==0:print(f'\033[32;1m{n}')
    else:print(f'\033[m{n}')
    n+=1
    sleep(0.4)