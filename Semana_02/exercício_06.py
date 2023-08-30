def check_simmetric(matriz):
    n = len(matriz)
    for i in range(n):
            for j in range(n):
                if matriz[i][j] != matriz[j][i]:
                    print("A sua matriz quadrada não é simétrica!")
    print("A sua matriz quadrada é simétrica!")

def main():
    matriz = [
        [1, 2, 3],
        [2, 4, 5],
        [3, 5, 6]
    ]
    check_simmetric(matriz)
main()