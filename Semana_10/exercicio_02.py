def check_sentences():
    my_file = open('Laboratorio-II/Semana_10/text_sentences.txt', 'r')
    lines_list = my_file.readline()
    for line in lines_list:
        if lines_list != '':
            words = lines_list.split(',')
            print(words)
            lines_list = my_file.readline()
    print(lines_list)
    print(words)
    ''' for line in lines_list:
        if '''


def main():
    check_sentences()
main()