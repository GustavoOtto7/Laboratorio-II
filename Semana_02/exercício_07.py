def verify(original_numbers):
    new_list = []
    for i in range(0, 12):
        if original_numbers[i] - 1 not in original_numbers:
            new_list.append(f"[{original_numbers[i]} - ")
        elif original_numbers[i] + 1 not in original_numbers:
            new_list.append(f"{original_numbers[i]}]")
    return new_list    

def main():
    original_numbers = [100, 101, 102, 103, 104, 105, 110, 111, 113, 114, 115, 150]
    new_list = verify(original_numbers)
    print(new_list)
main()