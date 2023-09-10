def exibir_tabuleiro(tabuleiro):
    #essa função serve para mostrar o formato do tabuleiro e imprimi-lo
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * (4 * len(linha) - 2))

def verificar_vitoria(tabuleiro, jogador):
    #essa função é para verificar as linhas, colunas e diagonais do tabuleiro para ver se teve algum vencedor
    n = len(tabuleiro)

    #verica as linhas e colunas
    for i in range(n):
        if all(tabuleiro[i][j] == jogador for j in range(n)) or all(tabuleiro[j][i] == jogador for j in range(n)):
            return True

    #verifica as diagonais
    if all(tabuleiro[i][i] == jogador for i in range(n)) or all(tabuleiro[i][n - 1 - i] == jogador for i in range(n)):
        return True

    return False

def jogo_da_velha(n):
    #funcao de jogo, determina as jogadas e se o movimento ja foi feito, determina vitoria ou empate
    tabuleiro = [[" " for _ in range(n)] for _ in range(n)]
    jogadores = ["X", "O"]
    jogador_atual = 0
    jogadas = 0

    while True:
        exibir_tabuleiro(tabuleiro)
        print(f"Vez do jogador {jogadores[jogador_atual]}.")
        
        #obtem a posição da jogada do jogador que esta na vez
        while True:
            try:
                linha = int(input("Digite a linha (1 a {}): ".format(n))) - 1
                coluna = int(input("Digite a coluna (1 a {}): ".format(n))) - 1
                
                if 0 <= linha < n and 0 <= coluna < n and tabuleiro[linha][coluna] == " ":
                    break
                else:
                    print("Jogada inválida. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Tente novamente.")
        
        #computa a jogada
        tabuleiro[linha][coluna] = jogadores[jogador_atual]
        jogadas += 1

        #verifica se alguém ganhou
        if jogadas >= n:
            if verificar_vitoria(tabuleiro, jogadores[jogador_atual]):
                exibir_tabuleiro(tabuleiro)
                print(f"Jogador {jogadores[jogador_atual]} venceu!")
                break
        
        #verifica se empatou
        if jogadas == n**2:
            exibir_tabuleiro(tabuleiro)
            print("Empate!")
            break
        
        #troca para o próximo jogador
        jogador_atual = 1 - jogador_atual


#tabuleiro definido em 4X4
n = 4
jogo_da_velha(n)
