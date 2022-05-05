aluno={'nome':input('nome:'),'media':float(input('media:'))}
if aluno['media']<7:aluno['situação']='\033[31mReprovado'
else:aluno['situação']='\033[32mAprovado'
print(f'\n{aluno["nome"]} foi {aluno["situação"]}')