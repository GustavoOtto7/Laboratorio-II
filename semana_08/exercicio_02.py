def main():
    lista_meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
    try:
        num_mes = int(input("Digite o número do mês desejado: "))
        print("Mês: ", lista_meses[num_mes - 1])
    except IndexError:
        print("[Erro] O número passou do índice limite!")
        return main()              
    except ValueError:
        print("[Erro] Digite um número válido!")
        return main()
    except BaseException as error:
        print("[Erro] Ocorreu um erro:", error)
        return main() 
main()