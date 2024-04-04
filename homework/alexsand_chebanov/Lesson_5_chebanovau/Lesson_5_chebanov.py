# Задание 1

person = ['John', 'Doe', 'New York', '+1372829383739', 'US']

name = person[0]
last_name = person[1]
city = person[2]
phone = person[3]
country = person[4]

# Задание 2
string_1 = "результат операции: 42"
result_1 = string_1.index("4")
print(f'{int(string_1[int(result_1):]) + 10} ')

string_2 = "результат операции: 514"
result_2 = string_2.index("5")
print(f'{int(string_2[int(result_2):]) + 10} ')

string_3 = "результат работы программы: 9"
result_3 = string_3.index("9")
print(f'{int(string_3[int(result_3)]) + 10} ')

# Задание 3

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

print(f'Students {", ".join(students)} study these subjects: {", ".join(subjects)}')