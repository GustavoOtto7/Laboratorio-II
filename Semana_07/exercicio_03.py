def calculate(matriz):
    for line in range(len(matriz)):
        for column in range(len(matriz[line])):
            min_line = line
            min_column = column
            for line_aux in range(line, len(matriz)):
                start = column if line == line_aux else 0
                for column_aux in range(column, len(matriz[line_aux])):
                    if matriz[line_aux][column_aux] < matriz[min_line][min_column]:
                        min_line = line_aux
                        min_column = column_aux
            # Armazena o menor valor
            min_value = matriz[min_line][min_column]
            # Armazena na posição de menor valor o atual
            matriz[min_line][min_column] = matriz[line][column]
            # Armazena no valor atual o menor valor
            matriz[line][column] = min_value
    return matriz
def main():
    matriz = [[30, 40, 50], 
              [60, 80, 70], 
              [100, 110, 90]]
    matriz = calculate(matriz)
    print(matriz)
main()