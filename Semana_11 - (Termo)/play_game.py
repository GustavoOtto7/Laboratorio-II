import random

def get_word():
    words_list = open("Laboratorio-II\Semana_11 - (Termo)\words_list.txt", 'r')
    lines = words_list.readlines()    
    for line in lines:
        list_words = line.split()
        for word in list_words:
            print(word)

#def check_word():

def playing_game():
    for i in range(0, 5):
        word = (list([input("Digite a palavra desejada: ").upper()]))
        for letter in word:
            print(f"        {letter[0]} - {letter[1]} - {letter[2]} - {letter[3]} - {letter[4]}")


def main():
    get_word()
    playing_game()


main()