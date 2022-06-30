def maior(*numeros):print(f'Foram passados {len(numeros[0]) if type(numeros[0])==list else len(numeros)} valores o maior foi:',str(max(numeros) if type(numeros[0])!=list else str(max(numeros[0]))) if len(numeros)>0 else '0',sep='')
maior(0,3)
maior([int(input('numero:')) for vezes in range(int(input('\nTente você:\n\nquantidade de numeros:')))])