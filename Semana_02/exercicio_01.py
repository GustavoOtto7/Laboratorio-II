def reverse_list(list_1):
    list_2 = []
    for i in range(len(list_1) - 1, -1, -1):
        list_2.append(list_1[i])
    return list_2

def main():
    list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    list_2 = reverse_list(list_1)
    print(list_2)
main()