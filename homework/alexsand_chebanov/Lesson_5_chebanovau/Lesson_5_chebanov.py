# Задание 1

person = ['John', 'Doe', 'New York', '+1372829383739', 'US']

name, last_name, city, phone, country = person

# Задание 2
string_1 = "результат операции: 42"
result_1 = string_1.index(":")
print(int(string_1[result_1 + 2::]) + 10)

string_2 = "результат операции: 514"
result_2 = string_2.index(":")
print(int(string_2[result_2 + 2::]) + 10)

string_3 = "результат работы программы: 9"
result_3 = string_3.index(":")
print(int(string_3[result_3 + 2::]) + 10)

# Задание 3

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

print(f'Students {", ".join(students)} study these subjects: {", ".join(subjects)}')
