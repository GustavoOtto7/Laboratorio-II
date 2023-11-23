from menu import principal_menu, options_menu
import play_game
from colored import colors, print_colored


def main():
    opc = principal_menu()
    if opc == 1:
        play_game
    elif opc == 2:
        opc2 = options_menu()
        if opc2 == 1:
            print("Palavras apagadas com sucesso!")
            with open("Laboratorio-II\\Semana_11 - (Termo)\\used_words_list.txt", "w") as used_words_list:
                pass
        elif opc2 == 2:
            print("Instruções de jogo!!!")
        elif opc2 == 3:
            return
        else:
            print_colored("Erro!", colors.red, colors.negative, "Digite uma opcção válida!")
    elif opc == 3:
        x = 3
    else:
        print_colored("Erro!", colors.red, colors.negative)
main()