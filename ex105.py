def notas(*tuple_notas,situacao=False):
    """
    :param tuple_notas: gera uma tupla que é analisada e usada no dicionário.
    :param situacao: recebe valor booleano caso verdadeiro avalia a média da turma e diz se é boa.
    :return: retorna um dicionário com informações sobre os dados."""
    dicionario={'Quantidade de notas':len(tuple_notas),'A maior nota':max(tuple_notas),'Menor nota':min(tuple_notas),'A media da turma':round(sum(tuple_notas)/len(tuple_notas),2)}
    if situacao:dicionario['Situação']='Ruim!' if sum(tuple_notas)/len(tuple_notas)<6 else 'Razoável!' if 7>=sum(tuple_notas)/len(tuple_notas)>=5 else 'Boa!'
    return dicionario
print(notas(8,7,10,9,6,6,7,6,7,situacao=1))