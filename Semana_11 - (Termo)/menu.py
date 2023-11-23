from colored import colors, print_colored

def principal_menu():
    try:
        print("""
            TERMO
        ______________
        1- Novo Jogo:
        2- Opções: 
        3- Sair: 
    """)
        #print_colored("Isso é um teste!", colors.red, colors.negative)
        opc = int(input("Digite o opção desejada: "))
        return opc
    except ValueError:
        print(f"[Erro] - Você digitou uma opção inválida!")
    except BaseException as error:
        print(f"[Erro] - Houve um erro! ({error})")

'''def new_game_menu():
    print("""
            TERMO
        ______________
        1- Solo:
        2- Dueto: 
        3- Quarteto: 
        4- Sair:
    """)'''

def options_menu():
    try:
        print("""
                TERMO
            ______________
        1- Limpar a lista de palavras:
        2- Instruções de jogo: 
        3- Voltar: 
        """)
        opc2 = int(input("Digite o opção desejada: "))
        return opc2
    except ValueError:
        print(f"[Erro] - Você digitou uma opção inválida!")
    except BaseException as error:
        print(f"[Erro] - Houve um erro! ({error})")

def main():
    principal_menu()
    options_menu()
main()