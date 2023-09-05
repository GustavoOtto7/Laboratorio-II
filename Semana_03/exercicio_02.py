def verify(matriz):
    sum = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i > j:
                sum += matriz[i][j]
    print("Soma final: ", sum)

def main():
    matriz = [
        [  1,  2,  3,   4],
        [  5,  6,  7,   8],
        [  9, 10, 11,  12],
        [ 13, 14, 15 , 16]
    ]
    verify(matriz)
main()