import random
from colored import colors, print_colored, add_colored

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
        draw_word = draw_word.rstrip('\n')   
    attemps = 1
    used_words_temp_list = []
    while attemps != 6:
            word = input("Digite a palavra desejada: ").upper()
            if len(word) == 5 and word not in used_words_temp_list and word.isalpha():
                attemps += 1
                used_words_temp_list.append(word)
                result = []
                word = list(word)
                draw_word = list(draw_word)
                print(draw_word, word)
                for i in range(0, 5):
                    right_words = 0
                    if word[i] == draw_word[i]:
                        right_words += 1
                        result.append(add_colored(f"{word[i]}", colors.green, colors.negative))
                    elif word[i] in draw_word:
                            result.append(add_colored(f"{word[i]}", colors.yellow, colors.negative))
                    else:
                        result.append(add_colored(f"{word[i]}", colors.white, colors.back_gray))
                    if right_words == 5:
                        print(f"Parabéns você ganhou!")
                        return False
                for letter in result:
                    print(f"|{letter}|", end=" ") 
                print()
            else:
                print("Digite uma palavra válida! (Sem espaços, nem números e com 5 letras!)")     
                print("Ou você já digitou essa palavra!")
    print("Você não acertou a palavra, tente numa próxima!")

    with open("Laboratorio-II\\Semana_11 - (Termo)\\used_words_list.txt", "w") as used_words_list:
        pass

'''
Fazer mensagem de vitória ou derrota
Verificar contagem de tentativas = V
Verificar como fazer para o usuário não repetir palavras = V
Verificar letras repetidas
Tratar melhor os erros
Ver certinho como limpar o arquivo e oferecer essa opção no menu = V
Solo, Dueto, Quarteto
'''

def main():
    draw_word = get_word()
    draw_word = check_word(draw_word)
    playing_game(draw_word)


main()