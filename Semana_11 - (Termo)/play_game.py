import random
from colored import colors, add_colored

def get_word():
    with open("Laboratorio-II\\Semana_11 - (Termo)\\words_list.txt", "r") as words_list:
        lines = words_list.readlines()    
    num_lines = len(lines) - 1
    num_index = random.randint(0, num_lines)
    if num_index <= num_lines:
        draw_word = lines[num_index]
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

def playing_game(draw_word_list, attemps, num_words):
    used_words_temp_list = []
    right_words = 0
    while attemps != 6:
        word = input("Digite a palavra desejada: ").upper()
        if len(word) == 5 and word not in used_words_temp_list and word.isalpha():
            used_words_temp_list.append(word)
            attemps += 1
            for x in range(0, num_words):
                draw_word = draw_word_list[x]
                draw_word = draw_word.rstrip('\n')
                result = []
                word = list(word)
                draw_word = list(draw_word)
                right_letters = 0
                print()
                used_letters = set()
                for i, letter in enumerate(word):
                    if letter == draw_word[i]:
                        result.append(add_colored(f"{letter}", colors.green, colors.negative))
                        used_letters.add(letter)
                        right_letters += 1
                    elif letter in draw_word and letter != draw_word[i] and letter not in used_letters:
                        result.append(add_colored(f"{letter}", colors.yellow, colors.negative))
                        used_letters.add(letter)
                    elif letter not in draw_word or letter in used_letters:
                        result.append(add_colored(f"{word[i]}", colors.white, colors.back_gray))
                for letter in result:
                    print(f" |{letter}| -", end=" ") 
                print()
                if right_letters == 5:
                    right_words += 1
                    draw_word = ''.join(map(str, draw_word)) + '\n'
                    with open("Laboratorio-II\\Semana_11 - (Termo)\\used_words_list.txt", "a") as used_words_list:
                        used_words_list.write(draw_word)    
                    if right_words == num_words:
                        print(f"Parabéns você ganhou!")
                        return False
        else:
            print("Digite uma palavra válida! (Que não se repita, esteja sem espaços, nem números e tenha 5 letras!)")     
    else:
        print()
        print(draw_word)
        print("Você não acertou a palavra, tente numa próxima!")
