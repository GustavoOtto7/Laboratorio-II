import random

def get_word():
    words_list = open("Laboratorio-II\Semana_11 - (Termo)\words_list.txt", 'r')
    lines = words_list.readlines()    
    words_list.close()
    num_ind = random.randint(0, 8)
    num_lines = len(lines) - 1
    print("Número aleatório sorteado: ",num_ind)
    if num_ind <= num_lines:
        word_sorted = lines[num_ind]
        print(lines[num_ind])
        return word_sorted
    else:
        print('Número muito grande!')

def check_word(word_sorted):
    used_words_list = open("C:\Users\gusta\Repositórios VS Code\Laboratório-II\Laboratorio-II\Semana_11 - (Termo)\used_words_list.txt", "r")
    list_used = used_words_list.readlines()
    used_words_list.close()
    for word in list_used():
        if word == word_sorted:
            print("Essa palavra já foi utilizada!")
            get_word()
            break
        else:
            return word_sorted


def playing_game():
    for i in range(0, 5):
        word = (list([input("Digite a palavra desejada: ").upper()]))
        for letter in word:
            print(f"        {letter[0]} - {letter[1]} - {letter[2]} - {letter[3]} - {letter[4]}")


def main():
    word_sorted = get_word()
    check_word(word_sorted)
    playing_game()


main()