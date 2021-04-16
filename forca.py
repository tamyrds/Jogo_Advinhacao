def jogar():
        print('*' * 50)
        print('Bem vindo no jogo de Forca')
        print('*' * 50)

        palavra_secreta = "banana"

        enforcou = False
        acertou = False

        #enquanto True e True
        while(not enforcou and not acertou):
            chute = input("Qual letra? ")
            chute = chute.strip()

            index = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    print(f"Encontrei a letra {letra} na posição {index}")
                index = index +1

            print("Jogando....")
                


        print('FIM DO JOGO')

if(__name__ == "__main__"):
    jogar()