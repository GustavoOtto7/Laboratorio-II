def division(month): 
    divi_by_4 = month % 4
    divi_by_100 = month % 100
    divi_by_400 = month % 400
    if divi_by_400 == 0: 
        result = str("Bissexto")
    elif divi_by_4 ==  0 and divi_by_100 != 0:
        result = str("Bissexto!")
    else: 
        result = str("Não Bissexto!")
    return result

def main():
    try:
        month = int(input("Digite o ano desejado: "))
        result = division(month)
        print("O ano que você digitou é: ", result)
    except ValueError:
        print("[Erro] Você digitou um valor inválido!")
main()