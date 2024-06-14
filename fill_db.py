import sqlite3
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker('uk_UA')

class UniversityDatabase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def insert_group(self, name):
        self.cursor.execute('INSERT INTO groups (name) VALUES (?)', (name,))
        return self.cursor.lastrowid

    def insert_teacher(self, name):
        self.cursor.execute('INSERT INTO teachers (name) VALUES (?)', (name,))
        return self.cursor.lastrowid

    def insert_subject(self, name, teacher_id):
        self.cursor.execute('INSERT INTO subjects (name, teacher_id) VALUES (?, ?)', (name, teacher_id))
        return self.cursor.lastrowid

    def insert_student(self, name, group_id):
        self.cursor.execute('INSERT INTO students (name, group_id) VALUES (?, ?)', (name, group_id))
        return self.cursor.lastrowid

    def insert_grade(self, student_id, subject_id, grade, date):
        self.cursor.execute('INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)',
                            (student_id, subject_id, grade, date))

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()

class DataGenerator:
    def __init__(self, db):
        self.db = db

    def generate_groups(self, count):
        groups = []
        for _ in range(count):
            group_name = fake.word()
            group_id = self.db.insert_group(group_name)
            groups.append(group_id)
        return groups

    def generate_teachers(self, count):
        teachers = []
        for _ in range(count):
            teacher_name = fake.name()
            teacher_id = self.db.insert_teacher(teacher_name)
            teachers.append(teacher_id)
        return teachers

    def generate_subjects(self, count, teachers):
        subjects = []
        for _ in range(count):
            subject_name = fake.word()
            teacher_id = random.choice(teachers)
            subject_id = self.db.insert_subject(subject_name, teacher_id)
            subjects.append(subject_id)
        return subjects

    def generate_students(self, count, groups):
        students = []
        for _ in range(count):
            student_name = fake.name()
            group_id = random.choice(groups)
            student_id = self.db.insert_student(student_name, group_id)
            students.append(student_id)
        return students

    def generate_grades(self, students, subjects):
        for student_id in students:
            for subject_id in subjects:
                for _ in range(random.randint(10, 20)):
                    grade = random.randint(1, 12)
                    date = fake.date_between(start_date='-1y', end_date='today')
                    self.db.insert_grade(student_id, subject_id, grade, date)

db = UniversityDatabase('db/university.db')

generator = DataGenerator(db)
groups = generator.generate_groups(3)
teachers = generator.generate_teachers(4)
subjects = generator.generate_subjects(6, teachers)
students = generator.generate_students(40, groups)
generator.generate_grades(students, subjects)

db.commit()
db.close()

print("База даних успішно заповнена випадковими даними.")
