from menu import principal_menu, options_menu
from play_game import get_word, check_word, playing_game
from colored import colors, print_colored

def main():
    opc = principal_menu()
    if opc == 1:
        draw_word = get_word()
        draw_word = check_word(draw_word)
        playing_game(draw_word)
    elif opc == 2:
        opc2 = options_menu()
        if opc2 == 1:
            print("Palavras apagadas com sucesso!")
            with open("Laboratorio-II\\Semana_11 - (Termo)\\used_words_list.txt", "w") as used_words_list:
                pass
            return
        elif opc2 == 2:
            print("Instruções de jogo!!!")
        elif opc2 == 3:
            return
        else:
            print_colored("Erro!", colors.red, colors.negative, "Digite uma opção válida!")
    elif opc == 3:
        print("Você saiu! Obrigado por jogar!")
    else:
        print_colored("Erro!", colors.red, colors.negative)
main()