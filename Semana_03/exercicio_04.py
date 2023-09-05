def calculate(matriz):
    n = len(matriz)
    maior_produto = 0
    
    for i in range(n):
        for j in range(n):
            # Sequência na horizontal
            if j + 4 < n:
                produto = matriz[i][j] * matriz[i][j + 1] * matriz[i][j + 2] * matriz[i][j + 3] * matriz[i][j + 4]
                maior_produto = max(maior_produto, produto)

            if i + 4 < n:
                produto = matriz[i][j] * matriz[i + 1][j] * matriz[i + 2][j] * matriz[i + 3][j] * matriz[i + 4][j]
                maior_produto = max(maior_produto, produto)

            if i + 4 < n and j + 4 < n:
                produto1 = matriz[i][j] * matriz[i + 1][j + 1] * matriz[i + 2][j + 2] * matriz[i + 3][j + 3] * matriz[i + 4][j + 4]
                produto2 = matriz[i][j + 4] * matriz[i + 1][j + 3] * matriz[i + 2][j + 2] * matriz[i + 3][j + 1] * matriz[i + 4][j]
                maior_produto = max(maior_produto, produto1, produto2)
    return maior_produto

def main():
    matriz = [
        [2, 1, 1, 1, 1],
        [1, 2, 1, 1, 1],
        [1, 1, 2, 1, 1],
        [1, 1, 1, 2, 1],
        [1, 1, 1, 1, 2]
    ]
    maior_produto = calculate(matriz)
    print("O maior produto foi: ", maior_produto)
main()