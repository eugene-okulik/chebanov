# Задание №3

def return_value(text):
    result_1 = text.index(":")
    print(int(text[result_1 + 2::]) + 10)


return_value("результат операции: 42")
return_value("результат операции: 54")
return_value("результат работы программы: 209")
return_value("результат: 2")
