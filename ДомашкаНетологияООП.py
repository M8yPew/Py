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
        print(self.grades)
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


cool_Lecturer = Lecturer('Some', 'Buddy')
cool_Lecturer.courses_attached.append('Python')
cool_Lecturer.courses_attached.append('Not Python')

cool_Reviewer = Reviewer('Vasyan1', 'Vasyan1_surname')
cool_Reviewer.courses_attached.append('Python')
cool_Reviewer.courses_attached.append('Not Python')
cool_Reviewer.rate_hw(best_student, 'Python', 7)


best_student.rate_lecture(cool_Lecturer, 'Python', 5)
best_student.rate_lecture(cool_Lecturer, 'Not Python', 3)


print(best_student)
print(cool_Lecturer)
print(cool_Reviewer)



