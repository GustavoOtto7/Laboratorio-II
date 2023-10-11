def division(val1, val2):
    try:
        return val1/ val2
    except ZeroDivisionError:
        print("[Erro] você não pode dividir um número por zero!")
    except BaseException as error:
        print("[Erro] Ocorreu um erro:", error) 

def input_int(message, can_be_zero = True):
    while True:
        try:
            value = int(input(message))
            if not can_be_zero and value == 0:
                raise ValueError()
            return value
        except ValueError:
            print("[Erro] O número digitado é inválido!")
        except BaseException as error:
            print("[Erro] Ocorreu um erro:", error) 

def main():
    try:
        number_one = input_int("Digite o primeiro valor: ")
        number_two = input_int("Digite o segundo valor: ", can_be_zero = False)
        if number_two == 0:
            raise ValueError()
        result = division(number_one, number_two)
        print("Resultado: ", result)
    except ValueError:
        print("[Erro] Digite um número válido!")
    except BaseException as error:
        print("[Erro] Ocorreu um erro:", error) 
    else:
        print("[:] Obrigado por usar nosso sistema!")
main()