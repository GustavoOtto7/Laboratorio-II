def avaliation():
    try:
        num = int(input("Digite o valor da sua avaliação: "))
        assert num >= 0 and num <= 10, f"[Erro] - O número indicado está fora do intervalo! "
        return num
    except ValueError as error:
        print(f"[Erro] - Ocorrreu o erro {error}")
    except TypeError as error:
        print(f"[Erro] - Ocorrreu o erro {error}")
    except AssertionError as error:
        print(error)        

def main():
    num = avaliation()
    if num != None:
        print(f"Você enviou a avaliação: {num}")
main()