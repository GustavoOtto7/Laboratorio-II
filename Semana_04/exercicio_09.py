def result(students_dict):
    name = input("Digite o nome do aluno: ")
    if name == "oooo":
        highest_name = None
        highest_average = 0
        for name, data in students_dict.items():
            media = data["dados"]
            if media > highest_average:
                highest_average = media
                highest_name = name
        if highest_name:
            print(f"A maior nota média foi do aluno {highest_name} com {highest_average} pts")
        else:
            print("Nenhum aluno encontrado.")
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