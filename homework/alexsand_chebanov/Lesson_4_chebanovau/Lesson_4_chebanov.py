my_dict = {}

my_dict['tuple'] = (1, 3, None, 'text', False, 2.42)
my_dict['value'] = ['text', False, 2.42, 'sdsdf', 99]
my_dict['dict'] = {"city": "Екатеренбург", 'sex': "Мужской", "age": "30", 'work': 'police', "car": "volvo"}
my_dict['set'] = {7, None, 'text', 0.7, True}

print(my_dict["tuple"][-1])  # выведет на экран последний элемент
my_dict["value"].append('Четверг')  # добавит в конец списка один элемент
my_dict["value"].pop(1)  # удалит второй элемент списка
my_dict['dict'][('i am a tuple',)] = 'am'  # добавить элемент с ключем
del my_dict['dict']['sex']  # удалить элемент
my_dict['set'].add(100)  # добавить элемент
my_dict['set'].remove('text')  # удалить элемент

print(my_dict)
