
import random

# Lista de palavras secretas
palavras = ["cabaco", "washiton", "pipoca", "playdooll", "pou"]

# Função para escolher uma palavra secreta aleatoriamente
def escolher_palavra():
    return random.choice(palavras)


# Função para exibir o estado atual da palavra a ser adivinhada
def exibir_palavra(palavra, letras_corretas):
    exibicao = ""
    for letra in palavra:
        if letra in letras_corretas:
            exibicao += letra + " "
        else:
            exibicao += "_ "
    return exibicao

# Função principal do jogo
def jogar_forca():
    palavra_secreta = escolher_palavra()
    vidas = 6
    letras_corretas = []
    letras_erradas = []

    print("Bem-vindo ao Jogo da Forca!")
    print("Adivinhe a palavra secreta.")

    while True:
        print("Palavra:", exibir_palavra(palavra_secreta, letras_corretas))
        print("Vidas restantes:", vidas)
        print("Letras erradas:", letras_erradas)

        letra = input("Digite uma letra: ").lower()

        if letra in letras_corretas or letra in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        if letra in palavra_secreta:
            letras_corretas.append(letra)
            if len(letras_corretas) == len(set(palavra_secreta)):
                print("Parabéns! Você venceu!")
                break
        else:
            letras_erradas.append(letra)
            vidas -= 1
            if vidas == 0:
                print("\nVocê perdeu! A palavra secreta era:", palavra_secreta)
                break

    jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
    if jogar_novamente == "s":
        jogar_forca()

# Iniciar o jogo
jogar_forca()


