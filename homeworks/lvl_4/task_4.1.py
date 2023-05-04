# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:
import sqlite3

def creat_tbl():
    connection = sqlite3.connect('teatchers.db')
    cursor = connection.cursor()
    sql_query = """CREATE TABLE IF NOT EXISTS Students (
    Student_Id INTEGER NOT NULL,
    Student_Name TEXT NOT NULL,
    School_Id INTEGER NOT NULL PRIMARY KEY);
    """
    cursor.execute(sql_query)
    connection.commit()
    connection.close()


def insert_tbl():
    connection = sqlite3.connect('teatchers.db')
    cursor = connection.cursor()
    sql_query = """INSERT INTO Students (Student_Id, Student_Name, School_Id)
    VALUES 
    (201, 'Иван', 1),
    (202, 'Петр', 2),
    (203, 'Анастасия', 3),
    (204, 'Игорь', 4); """
    cursor.execute(sql_query)
    connection.commit()
    connection.close()
# creat_tbl()
#insert_tbl()
id = int(input("Student:"))
connection = sqlite3.connect('teatchers.db')
cursor = connection.cursor()
sql_query = """SELECT Students.Student_Id,Students.Student_Name,
School.School_id, School_name
FROM Students
JOIN School ON Students.School_id = School.School_id
WHERE Student_Id = ?;"""
cursor.execute(sql_query, (id,))
records = cursor.fetchall()
for i in records:
    print(f"ID Студента: {i[0]}")
    print(f"Имя студента: {i[1]}")
    print(f"ID школы: {i[2]}")
    print(f"Название школы: {i[3]}")
connection.close()