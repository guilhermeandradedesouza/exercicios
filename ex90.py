aluno={'nome':input('nome:'),'media':float(input('media:'))}
if aluno['media']<7:aluno['situação']='\033[31mReprovado'
else:aluno['situação']='\033[32mAprovado'
for a,b in aluno.items():print(f'{a} é {b}')