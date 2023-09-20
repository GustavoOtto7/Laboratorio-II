my_list = [8, 7, 3, 5, 1, 4, 9, 2, 6]
for index in range(len(my_list)):            
    for index_one in range(len(my_list) - 1 - index):
        if my_list[index_one] > my_list[index_one + 1]:
            tmp = my_list[index_one]
            my_list[index_one] = my_list[index_one + 1]
            my_list[index_one + 1] = tmp
print(my_list)