import sqlite3
import os


class UniversityQueries:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def execute_query_from_file(self, file_path, params=()):
        with open(file_path, 'r', encoding='utf-8') as file:
            query = file.read()
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()

    def top_5_students(self):
        query_file_path = os.path.join('queries', 'query_1.sql')
        results = self.execute_query_from_file(query_file_path)
        print("5 студентів із найбільшим середнім балом з усіх предметів:")
        for row in results:
            print(row)

    def top_student_in_subject(self, subject_id):
        query_file_path = os.path.join('queries', 'query_2.sql')
        results = self.execute_query_from_file(query_file_path, params=(subject_id,))
        print(f"\nСтудент із найвищим середнім балом з предмета з ID {subject_id}:")
        for row in results:
            print(row)

    def average_grade_in_groups(self, subject_id):
        query_file_path = os.path.join('queries', 'query_3.sql')
        results = self.execute_query_from_file(query_file_path, params=(subject_id,))
        print(f"\nСередній бал у групах з предмета з ID {subject_id}:")
        for row in results:
            print(row)

    def average_grade_overall(self):
        query_file_path = os.path.join('queries', 'query_4.sql')
        results = self.execute_query_from_file(query_file_path)
        print("\nСередній бал на потоці (по всій таблиці оцінок):")
        for row in results:
            print(row)

    def courses_by_teacher(self, teacher_id):
        query_file_path = os.path.join('queries', 'query_5.sql')
        results = self.execute_query_from_file(query_file_path, params=(teacher_id,))
        print(f"\nЯкі курси читає викладач з ID {teacher_id}:")
        for row in results:
            print(row)

    def students_in_group(self, group_id):
        query_file_path = os.path.join('queries', 'query_6.sql')
        results = self.execute_query_from_file(query_file_path, params=(group_id,))
        print(f"\nСписок студентів у групі з ID {group_id}:")
        for row in results:
            print(row)

    def grades_in_group_subject(self, group_id, subject_id):
        query_file_path = os.path.join('queries', 'query_7.sql')
        results = self.execute_query_from_file(query_file_path, params=(group_id, subject_id,))
        print(f"\nОцінки студентів у групі з ID {group_id} з предмета з ID {subject_id}:")
        for row in results:
            print(row)

    def average_grade_by_teacher(self, teacher_id):
        query_file_path = os.path.join('queries', 'query_8.sql')
        results = self.execute_query_from_file(query_file_path, params=(teacher_id,))
        print(f"\nСередній бал, який ставить викладач з ID {teacher_id} зі своїх предметів:")
        for row in results:
            print(row)

    def courses_by_student(self, student_id):
        query_file_path = os.path.join('queries', 'query_9.sql')
        results = self.execute_query_from_file(query_file_path, params=(student_id,))
        print(f"\nСписок курсів, які відвідує студент з ID {student_id}:")
        for row in results:
            print(row)

    def courses_by_student_and_teacher(self, student_id, teacher_id):
        query_file_path = os.path.join('queries', 'query_10.sql')
        results = self.execute_query_from_file(query_file_path, params=(student_id, teacher_id,))
        print(f"\nКурси, які студенту з ID {student_id} читає викладач з ID {teacher_id}:")
        for row in results:
            print(row)