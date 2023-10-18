def division(year): 
    divi_by_4 = year % 4
    divi_by_100 = year % 100
    divi_by_400 = year % 400
    if divi_by_400 == 0: 
        result = str("Bissexto")
    elif divi_by_4 ==  0 and divi_by_100 != 0:
        result = str("Bissexto!")
    else: 
        result = str("Não Bissexto!")
    return result
'''
def is_leap_year(year):
    if (year % 4 == 0 and not year % 100 = 0) or year % 400 == 0:
        return True
    return False
'''

def main():
    try:
        year = int(input("Digite o ano desejado: "))
        result = division(year)
        print("O ano que você digitou é: ", result)
    except ValueError:
        print("[Erro] Você digitou um valor inválido!")
    except BaseException as error:
        print("[Erro] Ocorreu um erro!", error)
main()