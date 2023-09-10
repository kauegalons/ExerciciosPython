import random

def escolher_palavra():
    #abrir o arquivo para pegar uma palavra aleatória
    with open("Palavras.txt", "r") as arquivo:
        palavras = arquivo.read().splitlines()
    return random.choice(palavras)

def mostrar_palavra(palavra, letras_certas):
    #mostra as letras certas ou erradas da palavra atual escolhida como desafio
    resultado = ""
    for i in range(len(palavra)):
        if letras_certas[i]:
            resultado += palavra[i]
        else:
            resultado += "_"
    return resultado

def jogo_termo():
    #todas as regras do jogo, tentativa, mostra as letras certas e erradas, mostra se ganhou ou perdeu o jogo
    palavra_secreta = escolher_palavra()
    letras_certas = [False] * len(palavra_secreta)
    tentativas_restantes = 6

    print("Bem-vindo ao jogo TERMO!")
    print(f"A palavra que você precisa adivinhar tem {len(palavra_secreta)} letras.")
    
    while tentativas_restantes > 0:
        palavra_atual = mostrar_palavra(palavra_secreta, letras_certas)
        print("\nPalavra atual: ", palavra_atual)
        tentativa = input(f"Tentativas restantes: {tentativas_restantes}\nDigite uma palavra de {len(palavra_secreta)} letras: ").lower()

        if len(tentativa) != len(palavra_secreta):
            print("A palavra deve ter o mesmo tamanho da palavra secreta.")
            continue

        if tentativa == palavra_secreta:
            print("Parabéns! Você adivinhou a palavra corretamente.")
            break

        if tentativa in letras_certas:
            print("Você já tentou essa palavra.")
            continue

        acertos = [letra == palavra_secreta[i] for i, letra in enumerate(tentativa)]
        
        for i in range(len(tentativa)):
            if not acertos[i]:
                letras_erradas = [letra for letra in tentativa if letra in palavra_secreta and letra != tentativa[i]]
                break
        else:
            letras_erradas = []

        for i in range(len(tentativa)):
            if acertos[i]:
                if not letras_certas[i] and tentativa[i] == palavra_secreta[i]:
                    letras_certas[i] = True

        if letras_erradas:
            print("Letras certas: ", ' '.join(letras_erradas))
        elif not any(acertos):
            print("Todas as letras estão erradas.")

        tentativas_restantes -= 1

    else:
        print(f"\nVocê perdeu! A palavra correta era '{palavra_secreta}'.")


jogo_termo()
