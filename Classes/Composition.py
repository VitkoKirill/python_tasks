# Создайте модель школы с классами School, Teacher и Student.
# Условие:
# Класс School содержит список учителей и учеников.
# Класс Teacher имеет атрибуты name и subject.
# Класс Student имеет атрибуты name и grade.
# Реализуйте метод get_students_by_teacher(teacher_name) в классе School, который возвращает всех учеников учителя.

class School():
    def __init__(self, teacher_list: list, student_list: list):
        self.teacher_list = teacher_list
        self.student_list = student_list

    def get_students_by_teacher(self, teacher) -> list:
        students = []
        for student in self.student_list:
            if teacher == student.teacher:
                students.append(student.name)
        return students


class Teacher():
    def __init__(self, name: str, subject: str):
        self.name = name
        self.subject = subject


class Student():
    def __init__(self, name: str, grade: str):
        self.teacher = None
        self.name = name
        self.grade = grade

    def set_teacher(self, teacher: Teacher):
        self.teacher = teacher


teacher1 = Teacher('Oleg', 'Python')
teacher2 = Teacher('Jack', 'Java')

student1 = Student('Mike', '7b')
student2 = Student('Bob', '8h')
student3 = Student('John', '5')

student1.set_teacher(teacher1)
student2.set_teacher(teacher1)
student3.set_teacher(teacher2)

school = School([teacher1, teacher2], [student1, student2, student3])

print(school.get_students_by_teacher(teacher1))
print(school.get_students_by_teacher(teacher2))