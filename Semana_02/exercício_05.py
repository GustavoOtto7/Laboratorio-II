def calculation(matriz_1, matriz_2):
    lines = len(matriz_1)
    columns = len(matriz_1)

    new_matriz = []
    for line in range(lines):
        new_line = []
        for column in range(columns):
            soma = (matriz_1[line][column] + matriz_2[line][column])
            new_line.append(soma)
        new_matriz.append(new_line)
    return new_matriz

def main():
    matriz_1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    matriz_2 = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]
    new_matriz = calculation(matriz_1, matriz_2)
    print(new_matriz)
main()