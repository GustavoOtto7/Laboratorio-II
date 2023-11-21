import random

def get_word():
    with open("Laboratorio-II\\Semana_11 - (Termo)\\words_list.txt", "r") as words_list:
        lines = words_list.readlines()    
    num_ind = random.randint(0, 8) #depois colocar o tamanho do Len
    num_lines = len(lines) - 1
    print("Número aleatório sorteado: ",num_ind)
    if num_ind <= num_lines:
        draw_word = lines[num_ind]
        print(lines[num_ind])
        return draw_word
    else:
        print('Número muito grande!')

def check_word(draw_word):
    with open("Laboratorio-II\\Semana_11 - (Termo)\\used_words_list.txt", "r") as used_words_list:
        list_used = used_words_list.readlines()
    for word in list_used:
        if draw_word != word:
            print("Essa palavra já foi utilizada!")
            get_word()
            break            
        else:
            return draw_word

def playing_game(draw_word):
    with open("Laboratorio-II\\Semana_11 - (Termo)\\used_words_list.txt", "a") as used_words_list:
        used_words_list.write(draw_word)
    for i in range(0, 5):
        word = (list([input("Digite a palavra desejada: ").upper()]))
        for letter in word:
            print(f"        {letter[0]} - {letter[1]} - {letter[2]} - {letter[3]} - {letter[4]}")


def main():
    draw_word = get_word()
    check_word(draw_word)
    playing_game(draw_word)


main()