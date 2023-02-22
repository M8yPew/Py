class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecture(self, Lector, course, grade):
        if isinstance(Lector, Lecturer) \
            and course in Lector.courses_attached \
                and (course in self.courses_in_progress or course in self.finished_courses):
                    Lector.grades[course] = grade
        else:
            return 'Ошибка'

    def get_avg_grade(self):
        grade_values = self.grades.values()
        if len(grade_values) > 0:
            avg_grade = sum(grade_values) / len(grade_values)
            return round(avg_grade, 3)
        else:
            return 0

    def __str__(self):
        result = 'Имя: ' + self.name + '\n' \
                 + 'Фамилия: ' + self.surname + '\n' \
                 + 'Средняя оценка за лекции: ' + str(self.get_avg_grade())
        return result

    def __gt__(self, other):
        avg1 = self.get_avg_grade()
        avg2 = other.get_avg_grade()
        return avg1 > avg2

    def __lt__(self, other):
        return self.get_avg_grade() < other.get_avg_grade()

    def __ge__(self, other):
        return self.get_avg_grade() >= other.get_avg_grade()

    def __le__(self, other):
        return self.get_avg_grade() <= other.get_avg_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname): # не понятно как без переопределения добавить в инициализацию ещё параметров но толька для дочернего класса
        super().__init__(name, surname)
        self.grades = dict()

    def get_avg_grade(self):
        grade_values = self.grades.values()
        if len(grade_values) > 0:
            avg_grade = sum(grade_values) / len(grade_values)
            return round(avg_grade, 3)
        else:
            return 0

    def __str__(self):
        result = 'Имя: ' + self.name + '\n' \
                 + 'Фамилия: ' + self.surname + '\n' \
                 + 'Средняя оценка за лекции: ' + str(self.get_avg_grade())
        return result

    def __gt__(self, other):
        avg1 = self.get_avg_grade()
        avg2 = other.get_avg_grade()
        return avg1 > avg2

    def __lt__(self, other):
        return self.get_avg_grade() < other.get_avg_grade()

    def __ge__(self, other):
        return self.get_avg_grade() >= other.get_avg_grade()

    def __le__(self, other):
        return self.get_avg_grade() <= other.get_avg_grade()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) \
                and course in self.courses_attached \
                and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += grade
            else:
                student.grades[course] = grade
        else:
            return 'Ошибка'
    def __str__(self):
        result = 'Имя:' + self.name + '\n' \
                 + 'Фамилия:' + self.surname
        return result

# Присвоение значений
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress.append('Python')
best_student.finished_courses.append('Not Python')

not_best_student = Student('Leeroy', 'Jenkins', 'your_gender')
not_best_student.courses_in_progress.append('Python')
not_best_student.courses_in_progress.append('Not Python')

cool_Lecturer = Lecturer('Some', 'Buddy')
cool_Lecturer.courses_attached.append('Python')
cool_Lecturer.courses_attached.append('Not Python')

Lazy_Lecturer = Lecturer('Lazy', 'Lector')
Lazy_Lecturer.courses_attached.append('Not Python')

cool_Reviewer = Reviewer('Vasyan1', 'Vasyan1_surname')
cool_Reviewer.courses_attached.append('Python')
cool_Reviewer.courses_attached.append('Not Python')
cool_Reviewer.rate_hw(best_student, 'Python', 7)
cool_Reviewer.rate_hw(not_best_student, 'Python', 10)
cool_Reviewer.rate_hw(not_best_student, 'Not Python', 2)

best_student.rate_lecture(cool_Lecturer, 'Python', 5)
best_student.rate_lecture(cool_Lecturer, 'Not Python', 3)
best_student.rate_lecture(Lazy_Lecturer, 'Python', 6)

# задание 4
# 1
def avg_grade_all_student(students, course):
    total_grade = 0;
    total_count = len(students)
    student_count = 0
    if total_count == 0:
        return 0
    for student in students:
        if course in student.grades:
            total_grade = total_grade + student.grades[course]
            student_count = student_count + 1
        else:
            print('--- Студент ---' + '\n' + str(student) + '\n' + '--- не имеет оценок по курсу ' + str(course))

    if student_count == 0:
        return 0

    result = total_grade / student_count

    return result

students = list()
students.append(best_student)
#students.append(not_best_student)

#print(avg_grade_all_student(students, 'Not Python'))

# 2
def avg_grade_all_lectors(lectors, course):
    lectors_count = 0
    total_grade = 0
    total_count = len(lectors)
    if total_count == 0:
        return 0
    for lector in lectors:
        if course in lector.grades:
            total_grade = total_grade + lector.grades[course]
            lectors_count = lectors_count + 1
        else:
            print('--- Преподаватель ---' + '\n' + str(lector) + '\n' + '--- не имеет оценок по курсу ' + str(course))
    if lectors_count == 0:
        return 0
    result = total_grade / lectors_count
    return result

lectors = list()
lectors.append(cool_Lecturer)
lectors.append(Lazy_Lecturer)


#print(best_student)
#(cool_Lecturer)
#print(cool_Reviewer)

print(cool_Lecturer < best_student)

#print(avg_grade_all_lectors(lectors, 'Not Python'))
