def open_files():
    my_file_names = open("Laboratorio-II\\Semana_10\\students_names.txt", "r")
    names_list = my_file_names.readlines()
    my_file_names.close()
    my_file_notes = open("Laboratorio-II\\Semana_10\\students_notes.txt", "r")
    notes_list = my_file_notes.readlines()
    my_file_notes.close()
    return names_list, notes_list

def verify_grades(names_list, notes_list):
    with open("Laboratorio-II\\Semana_10\\names_and_notes.txt", "w") as my_file_names_and_notes:
        for name, notes in zip(names_list, notes_list):
            notes = list(map(int, notes.split()))
            average = sum(notes) / len(notes)
            my_file_names_and_notes.write(f"Nome: {name.strip()}, Média: {average}\n")

def main():
    names_list, notes_list = open_files()
    verify_grades(names_list, notes_list)
main()
