**UniversityQueries**
---
Цей застосунок UniversityQueries призначений для виконання різноманітних запитів до бази даних університету, яка зберігається у SQLite.
Він надає зручний інтерфейс для виконання таких операцій, як отримання списку студентів з найвищим середнім балом,
отримання середнього балу по групах для певного предмета, а також інші корисні запити.
---

# Використання методів #

## Ініціалізація ##

Підключення до бази даних відбувається за допомогою створення екземпляра класу UniversityQueries, передаючи шлях до файлу бази даних SQLite:

``from queries import UniversityQueries
#Ініціалізація з'єднання з базою даних
queries = UniversityQueries('db/university.db')``

## Методи запитів ##

1.  `top_5_students()`: Отримує 5 студентів з найвищим середнім балом з усіх предметів.
2.  `top_student_in_subject(subject_id)`: Отримує студента з найвищим середнім балом з певного предмета за ID предмета.
3.  `average_grade_in_groups(subject_id)`: Отримує середній бал у групах з певного предмета за ID предмета.
4.  `average_grade_overall()`: Отримує загальний середній бал на потоці (по всій таблиці оцінок).
5.  `courses_by_teacher(teacher_id)`: Отримує список курсів, які читає викладач з певним ID.
6.  `students_in_group(group_id)`: Отримує список студентів у групі з певним ID.
7.  `grades_in_group_subject(group_id, subject_id)`: Отримує оцінки студентів у групі з певного предмета за ID групи і предмета.
8.  `average_grade_by_teacher(teacher_id)`: Отримує середній бал, який ставить викладач з певним ID зі своїх предметів.
9.  `courses_by_student(student_id)`: Отримує список курсів, які відвідує студент з певним ID.
10. `courses_by_student_and_teacher(student_id, teacher_id)`: Отримує список курсів, які відвідує студент з певним ID у викладача з певним ID.

## Закриття з'єднання ##

`queries.close()`