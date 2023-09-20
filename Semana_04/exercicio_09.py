def result(students_dict):
    name = str(input("Digite o nome do aluno: "))
    if name == "oooo":
        for name, media in students_dict.items():
            if students_dict[0]:
                highest_name = name(students_dict[media])
                highest_average = media(students_dict[name])
            else:
                if highest_average > media(students_dict[name]):
                    highest_average = media(students_dict[name])
                    highest_name = name(students_dict[media])
            print(f"A maior nota média foi do aluno {highest_name} com {highest_average} pts")
        return False
    else:
        g1 = float(input("Digite a primeira nota do aluno: "))
        g2 = float(input("Digite a segunda nota do aluno: "))
        media = (g1 + g2) / 2 
        students_dict[name] = {
            "dados" : media}
        return students_dict

def main():
    students_dict = {}
    while True:
        students_dict = result(students_dict)
main()