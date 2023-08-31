palavras = ('ARVORE', 'TERRA', 'GRAMA', 'AREIA', 'PEDRA', 'FRUTA', 'FOLHA', 'GIRASSOL', 'CEU', 'TRONCO', 'FLOR'
            , 'NUVEM', 'AR', 'FOGO', 'GELO')
for p in palavras:
    print(f"\nPara a palavra {p}, temos: ", end='')
    for letra in p:
        if letra in 'AEIOU':
            print(letra, end=' ')
