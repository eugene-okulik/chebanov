# Задание №1

text = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl," \
       " facilisis vitae semper at, dignissim vitae libero"
l = []
for i in text.split():
    if i[-1] == ',':
        l.append(i[0:-1] + 'ing,')
    elif i[-1] == '.':
        l.append(i[0:-1] + 'ing.')
    else:
        l.append(i + 'ing')
print(*l)

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
