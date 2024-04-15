def finish_me(func):
    def wrapper(first, second):
        if first == second:
            return func(first, second, "+")
        elif first > second:
            return func(first, second, "-")
        elif second > first:
            return func(first, second, "/")
        elif first or second < 0:
            return func(first, second, "*")

    return wrapper


@finish_me
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        try:
            return first / second
        except ZeroDivisionError:
            print("На ноль делить нельзя")


def math():
    x = float(input("Введите число 1: "))
    y = float(input("Введите число 2: "))
    result = calc(x, y)
    print(f"Результат {result}")


math()
