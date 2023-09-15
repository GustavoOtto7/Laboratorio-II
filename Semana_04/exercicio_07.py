def verify(list):
    dict = {}
    repetition = int(input("Quantos números você quer adicionar? "))
    for x in range(repetition):
        list.append(int(input("Digite um número: ")))
    for i in list:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

def main():
    list = []
    dict = verify(list)
    print("Lista de repetições: ")
    print("Resultado: -> ", dict)
main()