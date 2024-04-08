# Задание №1

text = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl," \
       " facilisis vitae semper at, dignissim vitae libero"
value = []
for i in text.split():
    if i[-1] == ',':
        value.append(i[0:-1] + 'ing,')
    elif i[-1] == '.':
        value.append(i[0:-1] + 'ing.')
    else:
        value.append(i + 'ing')
print(*value)

# Задание №2

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FuzzBuzz")
    elif i % 3 == 0:
        print('fuzz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)
