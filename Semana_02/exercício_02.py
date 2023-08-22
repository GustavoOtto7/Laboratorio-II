def remove_duplicates(list_1):
    new_list_clean = []
    duplicates = []
    for i in range(len(list_1)):
        if list_1[i] not in new_list_clean:
            new_list_clean.append(list_1[i])        
        else: 
            duplicates.append(list_1[i])
    return new_list_clean, duplicates

def main():
    list_1 = []
    while True:
        list_1.append(int(input("Digite um número: ")))
        r = input("Quer continuar? S/N   ").upper()
        if r == "N":
            break
    new_list_clean, duplicates = remove_duplicates(list_1)
    print("Lista limpa: ", new_list_clean)
    print("Duplicadas: ", duplicates)
main()