def check_simmetric(matriz):
    n = len(matriz)
    for i in range(n):
            for j in range(n):
                if matriz[i][j] != matriz[j][i] and matriz[j][i] != matriz[i][j]:
                    print("A sua matriz quadrada não é simétrica!")
                    break
    print("A sua matriz quadrada é simétrica!")
def main():
    matriz = [
        [1, 2],
        [2, 2]
    ]
    check_simmetric(matriz)
main()