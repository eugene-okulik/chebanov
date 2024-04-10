import sys

# Задание 2
sys.set_int_max_str_digits(30000)

count = 0
value = 100000


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


g = list(fib(value))
for i in g:
    if i == g[4] or i == g[199] or i == g[999] or i == g[99999]:
        count += 1
        print(f'{count}){i}\n')
