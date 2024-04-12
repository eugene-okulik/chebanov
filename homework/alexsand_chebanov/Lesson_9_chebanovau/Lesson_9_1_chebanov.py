import datetime

# Исходная дата
date_string = "Jan 15, 2023 - 12:05:33"

# Преобразование строки в объект datetime
date_object = datetime.datetime.strptime(date_string, "%b %d, %Y - %H:%M:%S")

# Распечатать полное название месяца
month_name = date_object.strftime("%B")
print("Полное название месяца:", month_name)

# Распечатать дату в нужном формате
formatted_date = date_object.strftime("%d.%m.%Y, %H:%M")
print("Дата в нужном формате:", formatted_date)
