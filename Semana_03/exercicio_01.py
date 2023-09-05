import random

def validate_number(matriz, num):
    for line in range(len(matriz)):
        for column in range(len(matriz[line])):
            if matriz[line][column] == num:
                return False
    return True

def generate_bingo():
    matriz = []
    for line in range(0,5):
        matriz.append([])
        for column in range(0, 5):
            num = random.randint(0, 99)
            while not validate_number(matriz, num):
                num = random.randint(0, 99)
            matriz[line].append(num)  
    return matriz

def main():
    matriz = generate_bingo()
    for line in matriz:
        print(line)    
main()