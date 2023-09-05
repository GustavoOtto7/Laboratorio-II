def calculation(money):
    notes = []
    while money > 0:
        if money >= 100:
            money -= 100
            notes.append(100)
        elif money >= 50:
            money -= 50
            notes.append(50)
        elif money >= 20:
            money -= 20
            notes.append(20)
        elif money >= 10:
            money -= 10
            notes.append(10)
    print(f"A quantidade de notas necessárias de 100 é: {notes.count(100)}")
    print(f"A quantidade de notas necessárias de 50 é: {notes.count(50)}")
    print(f"A quantidade de notas necessárias de 20 é: {notes.count(20)}")
    print(f"A quantidade de notas necessárias de 10 é: {notes.count(10)}")

def main():
    money = int(input("Digite o valor desejado: "))
    if money % 10 != 0:
        print("Valor inválido!")
    else: 
        calculation(money)
main()