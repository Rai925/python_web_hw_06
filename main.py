from queries import UniversityQueries

queries = UniversityQueries('db/university.db')

queries.top_5_students()
queries.top_student_in_subject(1)
queries.average_grade_in_groups(1)
queries.average_grade_overall()
queries.courses_by_teacher(1)
queries.students_in_group(1)
queries.grades_in_group_subject(1, 1)
queries.average_grade_by_teacher(1)
queries.courses_by_student(1)
queries.courses_by_student_and_teacher(1, 1)

queries.close()
