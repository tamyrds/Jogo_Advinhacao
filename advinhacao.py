import random

def jogar():
    
    print('*' * 50)
    print('Bem vindo no jogo de adivinhação')
    print('*' * 50)
    pontos = 1000

    numero_secreto = random.randrange(1,10)
    total_de_tentativas = 0

    print('Qual nível de dificuldade')
    print('(1) Facil (2) Medio (3) Dificil')

    nivel = int(input('Defina o nível: '))

    if(nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    for rodada in range(1,total_de_tentativas + 1):
        print('Tentativa', rodada, 'de', total_de_tentativas)
        chute_str = input('Digite um numero entre 1 e 100: ')
        print('Voce digitou ', chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute >100):
            print('Voce deve digitar um número entre 1 e 100!')
            continue


        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print(f'Voce acertou e fez {pontos} pontos!')
            break
        else:
            if (maior):
                print('Voce errou! O seu chute foi maior que o numero secreto')
            elif(menor):
                print('Voce errou! O seu chute foi menor que o numero secreto')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim de jogo")
    
if(__name__== "__main__"):
    jogar()