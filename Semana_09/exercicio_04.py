def find_element(lista, num):
    try:
        print(f"O número correspondete do índice {num} é: {lista[num]}")
    except IndexError as error:
        print(f"[Erro] - O índice que você digitou é inválido! Erro: ({error})")

def main():
    lista = [0, 10, 20, 30, 40, 50]
    try:
        num = int(input("Digite o índice desejado: "))
        find_element(lista, num)
    except BaseException as error:
        print(f"[Erro] - Ocorreu o erro: {error}")
main()