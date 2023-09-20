numbers_list = [8, 7, 3, 5, 1, 4, 9, 2, 6]
for index_one in range(len(numbers_list)):
    min_index = index_one
    for index_two in range(index_one, len(numbers_list)):
        if numbers_list[index_two] < numbers_list[min_index]:
            min_index = index_two
    min_value = numbers_list[min_index]
    numbers_list[min_index] = numbers_list[index_one]
    numbers_list[index_one] = min_value
print(numbers_list)