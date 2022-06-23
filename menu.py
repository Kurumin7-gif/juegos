import advinhacao
import forca


def escolhe_jogo():
    print()
    print()
    print("***********************************")
    print("***Escolha seu jogo agora mesmo!***")
    print("***********************************")
    print()
    print()
    print("(1) Advinhação | (2) Forca")
    jogo = int(input("Escolha o jogo: "))

    if jogo == 1:
        print("Jogando Advinhação")
        advinhacao.jogar()
    elif jogo == 2:
        print("Jogando Forca")
        advinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()