from calculator import sum
from dif_zero import get_number_diferent_zero

def main():
    num_1 = get_number_diferent_zero("Digite um número: ")
    num_2 = get_number_diferent_zero("Digite um número: ")
    result = sum_number(num_1, num_2)
    print(f"Resultado: ", result)
main()