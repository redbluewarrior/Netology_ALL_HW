from numpy.ma.core import append


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade = 0
        self.course_average_grade = 0
        self.all_course_grades = []

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
            #lecturer.average_grade = sum(lecturer.grades[course]) / len(lecturer.grades[course])
            all_grades = []
            for g in lecturer.grades.values():
                all_grades += g
            lecturer.average_grade = round(sum(all_grades) / len(all_grades), 2)
        else:
            return 'Ошибка'





    def __str__(self):
        return (f'Имя: {self.name} \n'
                f'Фамилия: {self.surname} \n'
                f'Средняя оценка за домашние задания: {self.average_grade}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}\n')

    def __gt__(self, other):
        return self.average_grade > other.average_grade

    def __lt__(self, other):
        return self.average_grade < other.average_grade

    def __eq__(self, other):
        return self.average_grade == other.average_grade




class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        self.average_grade = 0

    def __gt__(self, other):
        return self.average_grade > other.average_grade

    def __lt__(self, other):
        return self.average_grade < other.average_grade

    def __eq__(self, other):
        return self.average_grade == other.average_grade



class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)




    def __str__(self):
        return (f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_grade}\n')




class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
            all_grades = []
            for g in student.grades.values():
                all_grades += g
            student.average_grade = round(sum(all_grades) / len(all_grades), 2)
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}\n'

def average_student_grade(students, course):
    all_grades = []
    for student in students:
        if isinstance(student, Student) and course in student.grades:
            all_grades.extend(student.grades[course])
    if all_grades:
        return round(sum(all_grades) / len(all_grades), 2)

def average_lecturer_grade(lecturers, course):
    all_grades = []
    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer) and course in lecturer.grades:
            all_grades.extend(lecturer.grades[course])
    if all_grades:
        return round(sum(all_grades) / len(all_grades), 2)

#Task #4
#Добавление лекторов, проверяющих и студентов
lecturer_1 = Lecturer('Станислав', 'Черчесов')
lecturer_2 = Lecturer('Василий', 'Головкин')
reviewer_1 = Reviewer('Пётр', 'Михайлович')
reviewer_2 = Reviewer('Матвей', 'Попович')
student_1 = Student('Фрося', 'Рабинович', 'Ж')
student_2 = Student('Алехандро', 'Аллерандро', 'М')

# Добавление текущих курсов
lecturer_1.courses_attached += ['Python', 'Git', ]
lecturer_2.courses_attached += ['Python', 'Java']
student_1.courses_in_progress += ['Python', 'Git']
student_2.courses_in_progress += ['Python', 'Java']
reviewer_1.courses_attached += ['Python', 'Java', 'JavaScript', 'Git', 'Вводный модуль' ]
reviewer_2.courses_attached += ['Python', 'Java', 'JavaScript', 'Git', 'Вводный модуль']

# Добавление завершенных курсов
student_1.courses_in_progress += ['Вводный модуль']
student_2.courses_in_progress += ['Java']

# Добавление оценок лекторам
student_1.rate_lecturer(lecturer_1, 'Python', 3)
student_2.rate_lecturer(lecturer_1, 'Python', 9)
student_1.rate_lecturer(lecturer_1, 'Java', 3)
student_1.rate_lecturer(lecturer_1, 'Java', 4)
student_2.rate_lecturer(lecturer_1, 'Git', 9)
student_1.rate_lecturer(lecturer_1, 'Git', 5)

student_1.rate_lecturer(lecturer_2, 'Java', 2)
student_2.rate_lecturer(lecturer_2, 'Java', 9)
student_1.rate_lecturer(lecturer_2, 'Java', 2)
student_2.rate_lecturer(lecturer_2, 'Python', 9)
student_1.rate_lecturer(lecturer_2, 'Python', 8)
student_2.rate_lecturer(lecturer_2, 'Python', 8)

# Добавление оценок студентам
reviewer_1.rate_student(student_1, 'Python', 7)
reviewer_1.rate_student(student_1, 'Python', 6)
reviewer_2.rate_student(student_1, 'Git', 8)
reviewer_1.rate_student(student_1, 'Git', 7)
reviewer_1.rate_student(student_1, 'Вводный модуль', 2)
reviewer_2.rate_student(student_1, 'Вводный модуль', 8)

reviewer_1.rate_student(student_2, 'Python', 9)
reviewer_1.rate_student(student_2, 'Python', 6)
reviewer_2.rate_student(student_2, 'Java', 7)
reviewer_2.rate_student(student_2, 'Java', 5)
reviewer_1.rate_student(student_2, 'Python', 9)
reviewer_2.rate_student(student_2, 'Java', 7)


# Вывод общей информации по студентам и преподавателям
print(reviewer_1)
print(reviewer_2)
print(lecturer_1)
print(lecturer_2)
print(student_1)
print(student_2)

# Оценки Python
students_list = [student_1, student_2]
python_grade_stu = average_student_grade(students_list, 'Python')
lecturer_list = [lecturer_1, lecturer_2]
python_grade_lec = average_lecturer_grade(lecturer_list, 'Python')

print(f'Средняя оценка студента по курсу Python: {python_grade_stu}')
print(f'Средняя оценка лектора по курсу Python: {python_grade_lec}\n')

# Оценки Java
students_list = [student_1, student_2]
python_grade_stu = average_student_grade(students_list, 'Java')
lecturer_list = [lecturer_1, lecturer_2]
python_grade_lec = average_lecturer_grade(lecturer_list, 'Java')

print(f'Средняя оценка студента по курсу Java: {python_grade_stu}')
print(f'Средняя оценка лектора по курсу Java: {python_grade_lec}')

# Оценки Git
students_list = [student_1, student_2]
python_grade_stu = average_student_grade(students_list, 'Git')
lecturer_list = [lecturer_1, lecturer_2]
python_grade_lec = average_lecturer_grade(lecturer_list, 'Git')

print(f'Средняя оценка студента по курсу Git: {python_grade_stu}')
print(f'Средняя оценка лектора по курсу Git: {python_grade_lec}\n')

# Оценки Вводный модуль
students_list = [student_1, student_2]
python_grade_stu = average_student_grade(students_list, 'Git')

print(f'Средняя оценка студента по курсу Вводный модуль: {python_grade_stu}\n')


students_list = [student_1, student_2]
python_grade_stu = average_student_grade(students_list, 'Python')
lecturer_list = [lecturer_1, lecturer_2]
python_grade_lec = average_lecturer_grade(lecturer_list, 'Python')

print(f'Средняя оценка студента по курсу Python: {python_grade_stu}')
print(f'Средняя оценка лектора по курсу Python: {python_grade_lec}\n')

# Сравнение лекторов
print(lecturer_1 == lecturer_2)
print(lecturer_1 > lecturer_2)
print(lecturer_1 < lecturer_2)

# Сравнение студентов
print(student_1 == student_2)
print(student_1 > student_2)
print(student_1 < student_2)














# lecturer = Lecturer('Пётр', 'Петров', 'Python')
# print(lecturer)
# Task #2
# lecturer = Lecturer('Иван', 'Иванов')
# reviewer = Reviewer('Пётр', 'Петров')
# student = Student('Алёхина', 'Ольга', 'Ж')
#
# student.courses_in_progress += ['Python', 'Java']
# lecturer.courses_attached += ['Python', 'C++']
# reviewer.courses_attached += ['Python', 'C++']
#
# print(student.rate_lecture(lecturer, 'Python', 7))  # None
# print(student.rate_lecture(lecturer, 'Java', 8))  # Ошибка
# print(student.rate_lecture(lecturer, 'С++', 8))  # Ошибка
# print(student.rate_lecture(reviewer, 'Python', 6))  # Ошибка
#
# print(lecturer.grades)  # {'Python': [7]}

#Task #1
# lecturer = Lecturer('Иван', 'Иванов')
# reviewer = Reviewer('Пётр', 'Петров')
# print(isinstance(lecturer, Mentor)) # True
# print(isinstance(reviewer, Mentor)) # True
# print(lecturer.courses_attached)    # []
# print(reviewer.courses_attached)    # []

#0
# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
#
# cool_mentor = Reviewer('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
#
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
#
# print(best_student.grades)