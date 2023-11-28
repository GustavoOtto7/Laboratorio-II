from colored import colors, print_colored, add_colored

def principal_menu():
    try:
        print("""
            TERMO
        ______________
        1- Novo Jogo:
        2- Opções: 
        3- Sair: 
    """)
        opc = int(input("Digite o opção desejada: "))
        return opc
    except ValueError:
        print(f"[Erro] - Você digitou uma opção inválida!")
    except BaseException as error:
        print(f"[Erro] - Houve um erro! ({error})")

def new_game_menu():
    try:
        print("""
                TERMO
            ______________
            1- Solo:
            2- Dueto: 
            3- Quarteto: 
            4- Sair:
        """)
        opc1_1 = int(input("Digite o opção desejada: "))
        return opc1_1
    except ValueError:
        print(f"[Erro] - Você digitou uma opção inválida!")
    except BaseException as error:
        print(f"[Erro] - Houve um erro! ({error})")

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

def game_instructions():
    verde = str(add_colored('verde', colors.green, colors.negative))
    amarelo = str(add_colored('amarelo', colors.yellow, colors.negative))
    branco = str(add_colored('branco', colors.white, colors.back_gray))
    print(f'''
        O objetivo do jogo é adivinhar uma palavra secreta, que é sorteada aleatoriamente.
        A palavra secreta escolhida possui 5 letras.
        O jogador escolhe uma palavra por vez e tenta adivinhar a palavra.
        Se a letra escolhida estiver na palavra secreta e estiver na posição correta,
        essa letra é mostrada na posição correta e destacada em {verde}.
        Se a letra escolhida estiver na palavra secreta, mas não estiver na posição correta,
        essa letra é mostrada na palavra, mas destacada em {amarelo}.
        Se a letra escolhida não estiver na palavra secreta ou já tiver sido escolhida anteriormente,
        a letra é destacada em {branco}.
        O jogo termina quando a palavra é adivinhada corretamente ou quando o número máximo de tentativas é atingido. 
          ''')

'''def main():
    principal_menu()
    options_menu()
    game_instructions()
main()'''