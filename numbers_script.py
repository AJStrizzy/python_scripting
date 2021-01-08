def multiply_by_two(num):
    return num * 2

with open('numbers.txt') as prime_numbers_file:
    prime_numbers = prime_numbers_file.readlines()
    for num in prime_numbers:
        print(multiply_by_two(int(num)))


with open('numbers2.txt') as numbers2:
    list_numbers = numbers2.readlines()
    result = []

    for num_txt in list_numbers:
        if 'Five' in num_txt:
            remove_break = num_txt[:-1]
            result.append(remove_break)
        elif 'Fifteen' in num_txt:
            remove_break = num_txt[:-1]
            result.append(remove_break)
    print(result)            