temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32,
                30, 28, 24, 23]


def temperatures_28(x):
    return x > 28


new = list(filter(temperatures_28, temperatures))

print(f"Максимальная температура: {max(new)}\n"
      f"Минимальная температура: {min(new)}\n"
      f"Средняя температура: {(sum(new) / len(new))}")
