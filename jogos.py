import forca
import advinhacao

def escolha_jogo():
    print('*' * 50)
    print('Escolha o seu jogos')
    print('*' * 50)

    print('(1) Forca (2) Adivinhação')

    jogo = int(input('Qual jogo ? '))

    if(jogo ==1):
        print('Jogar o jogo da Foca')
        forca.jogar()
    elif(jogo ==2):
        print('Jogar o jogo da Advinhação')
        advinhacao.jogar()

if (__name__=="__main__"):
    escolha_jogo()