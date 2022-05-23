def maior(*numeros):print(f'Foram passados {len(numeros)} valores o maior foi:',str(max(numeros)) if len(numeros)>0 else '0',sep='')
maior(1,3)