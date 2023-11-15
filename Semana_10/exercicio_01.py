def calculate_avg():
    my_file = open('Laboratorio-II/Semana_10/list_numbers.txt', 'r')
    file_content = my_file.read()
    numbers_list = file_content
    numbers_list = file_content.split(',')
    sum_of_numbers = 0
    for number in numbers_list:
        sum_of_numbers += int(number)
    return sum_of_numbers / len(numbers_list)

def main():
    result = calculate_avg()
    print(result)
main()