def view_week():
    week = {}
    week_days = ('Domingo',
                 'Segunda-feira',
                 'Terça-feira',
                 'Quarta-feira',
                 'Quinta-feira',
                 'Sexta-feira',
                 'Sábado')
    for day in week_days:
        class_day = input(f"Qual aula você tem no(a) {day}? ")
        week[day] = class_day
        
    print("\n# AULAS DA SEMANA!")
    for key in week:
        print(f"\t {key} : {week[key]}")
def main():
    week = view_week()
main()