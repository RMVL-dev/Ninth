first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(first_elem)-len(second_elem) for first_elem, second_elem in zip(first, second) if len(first_elem) != len(second_elem))
second_result = (len(first[index]) == len(second[index]) for index in range(len(first)))

print(list(first_result))
print(list(second_result))