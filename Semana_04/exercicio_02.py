def view_week():
    week = {'Segunda' : ["Foil"],
        'Terça' : ["Lab - II"],
        'Quarta' : ["Inglês"],
        'Quinta' : ["Probabilidade & estatística"],
        'Sexta' : ["Fundamentos de economia"],
        'Sábado' : ["Sem aula"],
        'Domingo' : ["Sem aula"],}
    return week

def main():
    week = view_week()
    for k, v in week.items():
        print(f"No dia de {k}, possuo aula de {v}")
main()