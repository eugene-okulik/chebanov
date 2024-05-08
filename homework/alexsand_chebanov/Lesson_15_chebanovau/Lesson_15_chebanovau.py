import mysql.connector as mysql
import greds

with mysql.connect(
        host=greds.host,
        port=greds.port,
        username=greds.username,
        passwd=greds.passwd,
        database=greds.database
) as db:  # Подключение к базе

    """Создание студента"""
    cursor = db.cursor(dictionary=True, buffered=True)  # Cursor

    query_1 = 'INSERT INTO `students` (name, second_name) VALUES (%s, %s)'
    value_1 = ('EGOR', 'IVANOVICH')
    cursor.execute(query_1, value_1)

    student_id = cursor.lastrowid

    cursor.execute(f"""
    UPDATE students SET group_id = 2 WHERE (id = {student_id});
    """)

    db.commit()
    cursor.execute(f"SELECT*FROM students WHERE id = {student_id}")
    print(cursor.fetchall())

    """Создание книг для студента"""

    query_2 = 'INSERT INTO `books` (title, taken_by_student_id) VALUES (%s, %s)'
    value_2 = ('Рембо свежая кровь', student_id)
    cursor.execute(query_2, value_2)
    db.commit()

    query_3 = 'INSERT INTO `books` (title, taken_by_student_id) VALUES (%s, %s)'
    value_3 = ('Рембо тухла кровь', student_id)
    cursor.execute(query_3, value_3)
    db.commit()
    cursor.execute(f"SELECT*FROM books WHERE taken_by_student_id = {student_id}")
    print(cursor.fetchall())

    """Создание группы"""

    query_4 = 'INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)'
    value_4 = ('Гугл', 'june', 'august')
    cursor.execute(query_4, value_4)
    db.commit()

    """Создание предметов"""

    predmet = (['Чебанов_SQL_*'], ['Чебанов_AQA_*'], ['Чебанов_Python_*'])

    for i in predmet:
        cursor.execute('INSERT INTO `subjets` (title) VALUES (%s)', i)

    db.commit()

    """Создание уроков"""
    lesson_id = []
    lesson = (
        ['История', '1452'],
        ['Биология', '1453'],
        ['Химия', '1454'],
        ['Русский', '1452'],
        ['Матиматика', '1453'],
        ['Литиратура', '1454']
    )
    for i in lesson:
        cursor.execute('INSERT INTO `lessons` (title,subject_id) VALUES (%s, %s)', i)
        lesson_id.append(cursor.lastrowid)
    print(lesson_id)
    db.commit()
    """Создание оценок пользователя"""

    estimation = ['1', '2', '3', '4', '5', '3']

    for estimation, lesson_id in zip(estimation, lesson_id):
        cursor.execute('INSERT INTO `marks` (value,lesson_id,student_id) VALUES (%s,%s,%s)',
                       (estimation, lesson_id, student_id))
        db.commit()

    """Получение информации из базы данных"""

    cursor.execute(f"SELECT value FROM `marks` WHERE student_id = {student_id}")
    print(cursor.fetchall())
    db.commit()
    cursor.execute(f"SELECT title FROM `books` WHERE taken_by_student_id = {student_id}")
    print(cursor.fetchall())
    db.commit()

    cursor.execute(f"""
    SELECT s.name, g.title, b.title, m.value, l.title, s2.title
        FROM students s
        JOIN `groups` g
        ON s.group_id = g.id
        JOIN books b
        ON s.id = b.taken_by_student_id
        JOIN marks m
        ON s.id = m.student_id
        JOIN lessons l
        ON m.lesson_id = l.id
        JOIN subjets s2
        ON s2.id  = l.subject_id
        WHERE s.id = {student_id}
    """)
    for i in cursor.fetchall():
        print(i)
    db.commit()
    db.close()
