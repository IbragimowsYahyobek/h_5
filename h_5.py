import sqlite3
from datetime import datetime

# Создание базы данных
conn = sqlite3.connect('School.db')
cursor = conn.cursor()

# Задача 1: Создание таблиц
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    age INTEGER,
    grade TEXT NOT NULL,
    enrollment_date DATE DEFAULT CURRENT_DATE)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_name TEXT NOT NULL,
    teacher_name TEXT NOT NULL)''')

conn.commit()

# Задача 2: Добавление данных
def register_student():
    full_name = input("Введите полное имя студента: ")
    age = int(input("Введите возраст студента: "))
    grade = input("Введите класс студента: ")
    cursor.execute("INSERT INTO students (full_name, age, grade) VALUES (?, ?, ?)", 
   (full_name, age, grade))
    conn.commit()
    print("Студент успешно зарегистрирован.")

def add_subject():
    subject_name = input("Введите название предмета: ")
    teacher_name = input("Введите имя учителя: ")
    cursor.execute("INSERT INTO subjects (subject_name, teacher_name) VALUES (?, ?)", 
   (subject_name, teacher_name))
    conn.commit()
    print("Предмет успешно добавлен.")

# Задача 3: Запросы и выборки данных
def get_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    for student in students:
        print(student)

def get_subjects():
    cursor.execute("SELECT * FROM subjects")
    subjects = cursor.fetchall()
    for subject in subjects:
        print(subject)

def get_students_by_grade(grade):
    cursor.execute("SELECT * FROM students WHERE grade = ?", (grade,))
    students = cursor.fetchall()
    for student in students:
        print(student)

# Задача 4: Обновление и удаление данных
def update_student_age(student_id, new_age):
    cursor.execute("UPDATE students SET age = ? WHERE id = ?", (new_age, student_id))
    conn.commit()
    print("Возраст студента успешно обновлен.")

def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    print("Студент успешно удален.")

# Задача 5: Дополнительные задания (по желанию)
def get_student_count_by_grade():
    cursor.execute("SELECT grade, COUNT(*) FROM students GROUP BY grade")
    grade_counts = cursor.fetchall()
    for grade, count in grade_counts:
        print(f"Класс: {grade}, Количество студентов: {count}")

def get_teacher_subjects(teacher_name):
    cursor.execute("SELECT subject_name FROM subjects WHERE teacher_name = ?", (teacher_name,))
    subjects = cursor.fetchall()
    for subject in subjects:
        print(subject[0])

# Закрытие соединения
def close_connection():
    conn.close()

# Пример использования:
if __name__ == "__main__":
    # Здесь можно вызвать нужные функции для тестирования
    register_student()
    add_subject()
    get_students()
    get_subjects()
    get_students_by_grade('10A')
    update_student_age(1, 18)
    delete_student(2)
    get_student_count_by_grade()
    get_teacher_subjects('Иванов Иван Иванович')

    close_connection()