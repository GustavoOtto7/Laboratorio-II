def calculation(matriz):
    soma = []
    for line in matriz:
        maior = line[0]
        for column in line:
            if column > maior:
                maior = column 
        soma.append(maior)
    return soma

def main():
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    soma = calculation(matriz)
    soma_total = sum(soma)
    print(soma_total)
main()