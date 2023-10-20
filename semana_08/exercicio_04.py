import math
def class_division(n, m):
    factorial_of_n = math.factorial(n)
    factorial_of_m = math.factorial(m)
    value = math.factorial(n - m)
    result = factorial_of_n/(factorial_of_m * value)
    return result

def main():
    try:
        n = int(input("Digite o número de alunos da turma: "))
        m = int(input("Digite o tamanho do grupo desejado: "))
        result = class_division(n, m)
        print("Quantidade de combinações possíveis: ", result)
    except ValueError:
        print("Você digitou um valor errado, verifique novamente!")
        print("Obs: O número do grupo não deve ser maior que o total de alunos!")
    except BaseException as error:
        print("[Erro] Ocorreu um erro!", error)
main()