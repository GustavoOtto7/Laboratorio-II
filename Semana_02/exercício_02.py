def remove_duplicates(list_1):
    new_list_clean = []
    duplicates = []
    for i in range(len(list_1)):
        if list_1[i] != list_1:
            new_list_clean.append(list_1[i])        
        else: 
            duplicates.append(list_1[i])

def main():
    list_1 = [1, 2, 3, 4, 4, 5, 2]
    new_list_clean = remove_duplicates(list_1)
    duplicates = remove_duplicates(list_1)
    print("Lista limpa: ", new_list_clean)
    print("Duplicadas: ", duplicates)
main()