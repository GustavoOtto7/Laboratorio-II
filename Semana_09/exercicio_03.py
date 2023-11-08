class NegativeNumberError(BaseException):
        pass

def calculate_square_root():
    try:
        num = int(input("Digite o número desejado: "))
        if num < 0:
            raise NegativeNumberError("NegativeNumberError")
        else:
             result = num ** 0.5
             print(f"A raíz quadrada de {num} é igual a {result:.2f}")
    except NegativeNumberError as error:
        print(f"[Erro] - O número não pode ser negativo! Erro: ({error})")
    except BaseException as error:
        print(f"[Erro] - Ocorreu o erro: ({error})")     

def main():
    calculate_square_root()
main()