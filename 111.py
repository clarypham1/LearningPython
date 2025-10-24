class Student:
    def __init__(self, name, group, sound="I'm here"):
        self.name = name
        self.group = group
        self.sound = sound

    def say(self, times):
        for i in range(times):
            print(self.name + " says: " + self.sound)
        return

class Teacher():
    def __init__(self):
        self.students = []
    def student_here(self, student):
        self.students.append(student)
        print(student.name + " is here")
        return
    def student_not_here(self, student):
        self.students.remove(student)
        print(student.name + " is not here")
        return
    def greet_student(self):
        for student in self.students:
            print(student.name + " says: " + student.sound)
student1 = Student("Dolly", group= 1)
student2 = Student("Haley", group= 2)
student3 = Student("David", group= 1)
teacher = Teacher()
teacher.student_here(student1)
teacher.student_here(student2)
teacher.student_here(student3)
teacher.greet_student()
teacher.student_not_here(student1)
teacher.student_not_here(student2)
teacher.greet_student()


