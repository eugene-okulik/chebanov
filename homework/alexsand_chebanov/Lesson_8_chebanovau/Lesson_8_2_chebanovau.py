import sys

# Задание 2
sys.set_int_max_str_digits(30000)


def febonachi():
    f = [1, 1]
    f1 = f2 = 1
    for i in range(1, 100000):
        f.append(f1 + f2)
        f1, f2 = f2, (f1 + f2)
    print(f[4], f[199], f[999], f[99999], sep="\n", )


febonachi()
