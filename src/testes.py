import jogovelha
import sys

erro inicializar= False
jogo = jogovelha.inicializar()

if len(jogo) != 3:
    erro inicializar= True
else:
    for linha in jogo:
        if len(linha) != 3:
                erro inicializar= True
        else:
            for elemento in linha:
                if elemento != '.':
                    erro inicializar= True
if erro inicializar:
    sys.exit(1)
else:
    sys.exit(0)
