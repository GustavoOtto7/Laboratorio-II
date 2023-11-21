"""import random

def get_word():
    words_list = open("Laboratório-II\Laboratorio-II\Semana_11 - (Termo)\words_list.txt", "r")
    used_words_list = open("Laboratório-II\Laboratorio-II\Semana_11 - (Termo)\used_words_listwords_list.txt", "w")"""


    words_list = open("Laboratorio-II\Semana_11 - (Termo)\words_list.txt", "r")
    line = words_list.readlines()
    for line in words_list:
        print(words_list[line])


(word.strip()) para tirar espaços em branco e talvez números

