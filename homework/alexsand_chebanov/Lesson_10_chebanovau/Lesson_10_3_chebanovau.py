def finish_me(func):
    def wrapper(first, second):
        if first == second:
            return print(first + second)
        if first > second:
            return print(second - first)
        if second > first:
            return print(first / second)
        if first < 0 or second < 0:
            return func()

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


calc(1, 0)
