def soma(matriz):
    media_linha = []
    media_matriz = 0
    for line in matriz:
        soma1 = 0
        for column in line:
            media_matriz += column
            soma1 += column
        media_linha.append(soma1 / 3)
    return media_linha, media_matriz
    
def main():
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    media_linha, media_matriz = soma(matriz)
    print("A média de cada linha é: ", media_linha)
    print("A média dos números da matriz é: ", media_matriz / 9)
main()