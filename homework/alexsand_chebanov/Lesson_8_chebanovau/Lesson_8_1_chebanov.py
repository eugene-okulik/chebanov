import random


# Задание 1
def zarplata():
    salary = int(input("Введи свою зарплату: "))
    bonus = random.choice([True, False])
    value_bonus = random.randrange(100, 1000)
    if bonus == True:
        print(f"${str(salary + value_bonus)}")
    else:
        print(salary)


zarplata()
