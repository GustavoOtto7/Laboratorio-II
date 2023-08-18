def calculation(matriz):
    soma = []
    for line in range(len(matriz)):
        for column in range(len(matriz[line])):
            if matriz[line][column] >= matriz[line]:
                matriz[line][column].append(soma)
            return soma

def main():
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    soma = calculation(matriz)
    print(soma)
main()