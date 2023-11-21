import random
from list_colors import colors, print_colored

def get_word():
    with open("Laboratorio-II\\Semana_11 - (Termo)\\words_list.txt", "r") as words_list:
        lines = words_list.readlines()    
    num_lines = len(lines) - 1
    num_index = random.randint(0, num_lines)
    print("Número aleatório sorteado: ",num_index)
    if num_index <= num_lines:
        draw_word = lines[num_index]
        print(lines[num_index])
        return draw_word.upper()
    else:
        print('Número muito grande!')

def check_word(draw_word):
    while True:
        with open("Laboratorio-II\\Semana_11 - (Termo)\\used_words_list.txt", "r") as used_words_list:
            list_used = used_words_list.readlines()
        for word in list_used:
            if draw_word == word or draw_word is None:
                print("Essa palavra já foi utilizada!")
                draw_word = get_word()
                break
        else:
            return draw_word

def playing_game(draw_word):
    with open("Laboratorio-II\\Semana_11 - (Termo)\\used_words_list.txt", "a") as used_words_list:
        used_words_list.write(draw_word)
    for answers in range(0, 5):
        while True:
            word = input("Digite a palavra desejada: ").upper()
            word_size = len(word)
            if word_size == 5 and word.isalpha():
                result = []
                word = list(word)
                draw_word = list(draw_word)
                print(draw_word, word)
                for i in range(0, 5):
                    if word[i] == draw_word[i]:
                        result.append(print_colored(f"{word[i]}", colors.green, colors.negative))
                    else:
                        letter = 0
                        while letter != 5:
                            for x in range(0, 5):
                                if word[letter] == draw_word[x]:
                                    result.append(print_colored(f"{word[letter]}", colors.yellow, colors.negative))
                            else:
                                result.append(print_colored(f"{word[i]}", colors.white, colors.back_gray))
                            letter += 1
                    
                        

                    
                print(result)
                '''for letter in word:
                    if letter == draw_word[i].upper():
                            print_colored(f"{letter}", colors.green, colors.negative)
                    for i in range(0, 5):
                        
        
                print(f"        {letter[0]} - {letter[1]} - {letter[2]} - {letter[3]} - {letter[4]}")'''
            else:
                print("Digite uma palavra válida! (Sem espaços, nem números!)")

    with open("Laboratorio-II\\Semana_11 - (Termo)\\used_words_list.txt", "w") as used_words_list:
        pass


'''if verde
elif amarelo
else: branco'''

def main():
    draw_word = get_word()
    draw_word = check_word(draw_word)
    playing_game(draw_word)


main()