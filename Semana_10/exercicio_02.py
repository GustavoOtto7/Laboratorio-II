def check_sentences(word, file_path):
    file = open(file_path, 'r')
    lines = file.readlines()
    for index, line in enumerate(lines):
        content_line = line.replace(",", "").replace(".", "").split(" ")
        if word in content_line:
            print(f"[{index}] -> {line}")

def main():
    word = input("Digite uma palavra: ")
    check_sentences(word, 'Laboratorio-II/Semana_10/text_sentences.txt')
main()