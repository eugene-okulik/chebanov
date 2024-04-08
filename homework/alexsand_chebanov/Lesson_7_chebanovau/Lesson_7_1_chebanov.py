# Задание №1 - "Угадайка"

while True:
    value_user = int(input('Введите своё значение: '))
    if value_user != 5:
        print('попробуйте снова')
        continue
    if value_user == 5:
        print('Поздравляю! Вы угадали!')
        break
