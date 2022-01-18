palavras=('felicidade','tristeza','amor','vida','familia','verdade','promessa','mentira')
for a,g in enumerate(palavras):
    print(f'na palavra {g} temos as vogais {palavras[a].index("a"),palavras[a].index("e"),palavras[a].index("i"),palavras[a].index("o"),palavras[a].index("u")}')