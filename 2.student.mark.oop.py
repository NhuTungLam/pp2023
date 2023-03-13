class Student:
    def __init__(self, student_id, student_name, student_dob):
        self.student_id = student_id
        self.student_name = student_name
        self.student_dob = student_dob

    def get_info(self):
        return "Student id: {}, Student name: {}, Date of birth: {}".format(self.student_id, self.student_name,self.student_dob)
class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name

    def get_info(self):
        return "Course id: {}, Course name: {}".format(self.course_id,self.course_name)
student1 = Student(1,"A","01/01/2003")
student2 = Student(2,"B","02/02/2003")
course1 = Course(101,"Math")
course2 = Course(102,"English")
students = []
courses = {}
student_marks_list = {}

students.append(student1)
students.append(student2)
courses[course1.course_id] = course1
courses[course2.course_id] = course2
student_marks_list[(student1.student_id,course1.course_id)] = 20
student_marks_list[(student2.student_id,course2.course_id)] = 19
for student in students:
    print(student.get_info())

for course in courses.values():
    print(course.get_info())

for (student_id,course_id),mark in student_marks_list.items():
    print("Student id: {}, Course id: {}, Mark: {}".format(student_id,course_id, mark))   
