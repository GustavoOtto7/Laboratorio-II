def result(students_dict):
    name = str(input("Digite o nome do aluno: "))
    if name == "":
        for name, media in students_dict.items():
            print(f"A nota média do aluno {name} foi: {media} pts")
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