def open_files():
    my_file_names = open("Laboratorio-II\\Semana_10\\students_names.txt", "r")
    names_list = my_file_names.readlines()
    my_file_names.close()
    my_file_notes = open("Laboratorio-II\\Semana_10\\students_names.txt", "r")
    notes_list = my_file_notes.readlines()
    my_file_notes.close()
    return names_list, notes_list

def verify_grades(names_list, notes_list):
    for i in range(len(names_list)):
        my_file_names_and_notes = open("Laboratorio-II\\Semana_10\\names_and_notes.txt", "w")
        names_and_notes_list = my_file_names_and_notes.write(names_list[i])
        my_file_names_and_notes.close()

    for i in range(len(notes_list)):
        if len(notes_list[i][0]) > 1:
            (notes_list[i][0] + notes_list[i][1]) / 2
            
        else: 

    


def main():
    names_list, notes_list = open_files()
    names_and_notes_list = verify_grades(names_list, notes_list)

main()