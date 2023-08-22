def check_simmetric(matriz):
    n = len(matriz)
    for i in range(n):
            for j in range(n):
                if i != j and matriz[i][j] != matriz[j][i]:
                    print("A sua matriz quadrada não é simétrica!")
                    return
    print("A sua matriz quadrada é simétrica!")
def main():
    matriz = [
        [1, 2],
        [2, 2]
    ]
    check_simmetric(matriz)
main()