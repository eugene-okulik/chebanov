from datetime import datetime, timedelta


# Чтение файла и обработка дат
with open(r"C:\Okulik_AQA\chebanov\homework\eugene_okulik\hw_13\data.txt", 'r',encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines:
        parts = line.strip().split(' - ')
        date = parts[0]
        action = parts[1]

        if action.startswith('распечатать эту дату, но на неделю позже'):
            data = datetime.fromisoformat(date[3:])
            new_date = data + timedelta(weeks=1)
            print(new_date)
        elif action.startswith('распечатать какой это будет день недели'):
            data = datetime.fromisoformat(date[3:])
            print(data.strftime('%A'))
        elif action.startswith('распечатать сколько дней назад была эта дата'):
            data = datetime.fromisoformat(date[3:])
            days_ago = (datetime.now() - data).days
            print(days_ago)
