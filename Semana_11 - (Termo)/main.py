from menu import principal_menu, new_game_menu, options_menu, game_instructions
from play_game import get_word, check_word, playing_game
from colored import colors, print_colored

def main():
    while True:
        opc = principal_menu()
        if opc == 1:
            while True:
                opc1_1 = new_game_menu()
                if opc1_1 == 1:
                    draw_word_list = []
                    attemps = 1
                    num_words = 1
                    draw_word = get_word()
                    draw_word = check_word(draw_word)
                    draw_word_list.append(draw_word)
                    playing_game(draw_word_list, attemps, num_words)
                elif opc1_1 == 2:
                    draw_word_list = []
                    attemps = 0
                    num_words = 2
                    for x in range(0, num_words):
                        draw_word = get_word()
                        draw_word = check_word(draw_word)
                        draw_word_list.append(draw_word)
                    playing_game(draw_word_list, attemps, num_words)
                elif opc1_1 == 3:
                    draw_word_list = []
                    attemps = -2
                    num_words = 4
                    for x in range(0, num_words, 1):    
                        draw_word = get_word()
                        draw_word = check_word(draw_word)
                        draw_word_list.append(draw_word)
                    playing_game(draw_word_list, attemps, num_words)
                elif opc1_1 == 4:
                    break
                
        elif opc == 2:
            while True:
                opc2 = options_menu()
                if opc2 == 1:
                    print("Palavras apagadas com sucesso!")
                    with open("Laboratorio-II\\Semana_11 - (Termo)\\used_words_list.txt", "w") as used_words_list:
                        pass
                elif opc2 == 2:
                    game_instructions()
                elif opc2 == 3:
                    break
                else:
                    print_colored("Erro!", colors.red, colors.negative, "Digite uma opção válida!")
        elif opc == 3:
            print("Você saiu! Obrigado por jogar!")
            break
        else:
            print_colored("Erro!", colors.red, colors.negative)
main()