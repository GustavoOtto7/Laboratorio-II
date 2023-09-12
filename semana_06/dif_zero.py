def get_number_diferent_zero(message):
    value = int(input("Digite um número: "))
    while True:
        if value != 0:
            return value
        else:
            print("Número inválido!")
            