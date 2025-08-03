class student:
    def __init__(self,student_id,name,age,grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
    def __str__(self):
        return f"ID: {self.student_id},Name:{self.name},Age: {self.age}, Grade:{self.grade}"

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self,student):
        self.students.append(student)

    def display_student(self):
        for student in self.students:
            print(student)

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None
    
    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def remove_student_by_id(self, student_id):
        self.students = [student for student in self.students if student.student_id != student_id]

    def update_student_grade(self, student_id, new_grade):
        student = self.find_student_by_id(student_id)
        if student:
            student.grade = new_grade


s1= student(1, "Alice", 17 , "A")
s2=student(2, "Bobby", 16 , "A")
s3=student(3, "Jade", 17 , "A")
s4=student(4, "Mehdi", 18 , "A")
s5=student(5, "Jack", 16 , "A")


manager = StudentManager()
manager.add_student(s1)
manager.add_student(s2)
manager.add_student(s3)
manager.add_student(s4)
manager.add_student(s5)

manager.display_student()

print(manager.find_student_by_id(3))


manager.remove_student_by_id(2)
manager.display_student()

manager.update_student_grade(2, "B+")
manager.display_student()






    
    
        


    

